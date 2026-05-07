from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import ipaddress
import os
import socket
from urllib.parse import parse_qs, urlsplit, urlunsplit

# Get the backend directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Support both SQLite (local) and PostgreSQL (Render)
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(BASE_DIR, 'test_results.db')}"
)


def is_ip_host(host: str) -> bool:
    if not host:
        return False
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def choose_postgres_driver(url: str) -> str:
    """Choose SQLAlchemy PostgreSQL driver with safe production defaults."""
    forced_driver = (os.environ.get("DB_DRIVER") or "").strip().lower()
    if forced_driver in {"psycopg", "psycopg2"}:
        return forced_driver

    parsed = urlsplit(url)
    host = parsed.hostname or ""

    # Raw IP endpoints are often more stable with psycopg2 on managed platforms.
    if is_ip_host(host):
        return "psycopg2"

    return "psycopg"


def apply_postgres_driver(url: str, driver: str) -> str:
    """Normalize URL to a SQLAlchemy postgres URL with explicit driver."""
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    if not url.startswith("postgresql"):
        return url

    parsed = urlsplit(url)
    scheme_prefix = f"{parsed.scheme}://"
    target_prefix = f"postgresql+{driver}://"
    return url.replace(scheme_prefix, target_prefix, 1)


def normalize_render_postgres_url(url: str) -> str:
    """Fix truncated Render host IDs in DATABASE_URL when present.

    Some environments accidentally provide only a service id host like
    `dpg-xxxxx-a` instead of a full DNS hostname. For Render PostgreSQL,
    reconstruct the host using region information.
    """
    if not url.startswith("postgres"):
        return url

    parsed = urlsplit(url)
    host = parsed.hostname or ""
    if not host:
        return url

    running_on_render = bool(
        os.environ.get("RENDER")
        or os.environ.get("RENDER_SERVICE_ID")
        or os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    )
    use_internal_render_host = os.environ.get("RENDER_USE_INTERNAL_DB_HOST", "1").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }

    # If DB host is Render external FQDN, prefer internal short host to keep
    # traffic private and avoid external TLS issues.
    if use_internal_render_host and host.endswith(".render.com") and host.startswith("dpg-"):
        internal_host = host.split(".", 1)[0]
        userinfo = ""
        if parsed.username:
            userinfo = parsed.username
            if parsed.password:
                userinfo += f":{parsed.password}"
            userinfo += "@"

        port = f":{parsed.port}" if parsed.port else ""
        netloc = f"{userinfo}{internal_host}{port}"
        return urlunsplit((parsed.scheme, netloc, parsed.path, parsed.query, parsed.fragment))

    # Repair short Render DB host IDs such as dpg-...-a.
    # On Render we keep internal host as-is to avoid fallback to external TLS path.
    if host.startswith("dpg-") and "." not in host:
        if running_on_render and use_internal_render_host:
            return url
        try:
            socket.getaddrinfo(host, parsed.port or 5432)
            return url
        except OSError:
            # Fall through to fully qualified regional hostname.
            pass

        region = os.environ.get("RENDER_REGION", "frankfurt").strip() or "frankfurt"
        fixed_host = f"{host}.{region}-postgres.render.com"

        userinfo = ""
        if parsed.username:
            userinfo = parsed.username
            if parsed.password:
                userinfo += f":{parsed.password}"
            userinfo += "@"

        port = f":{parsed.port}" if parsed.port else ""
        netloc = f"{userinfo}{fixed_host}{port}"
        return urlunsplit((parsed.scheme, netloc, parsed.path, parsed.query, parsed.fragment))

    return url


def get_postgres_connect_args(url: str) -> dict:
    """Build safe psycopg2 connect args for PostgreSQL URLs.

    For Render-hosted DB endpoints we default to sslmode=require unless the
    user explicitly overrides via DB_SSLMODE.
    """
    parsed = urlsplit(url)
    host = parsed.hostname or ""
    query = parse_qs(parsed.query)
    running_on_render = bool(
        os.environ.get("RENDER")
        or os.environ.get("RENDER_SERVICE_ID")
        or os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    )

    # Priority: explicit env var -> URL query -> inferred default.
    # This lets operators override provider URLs without rewriting DATABASE_URL.
    sslmode = os.environ.get("DB_SSLMODE") or (query.get("sslmode") or [None])[0]
    if not sslmode:
        is_local_host = host in {"", "localhost", "127.0.0.1", "::1"}
        if host.startswith("dpg-") and "." not in host:
            # Render internal DB endpoint
            sslmode = "disable"
        elif is_local_host:
            sslmode = "disable"
        elif is_ip_host(host):
            # For raw IP endpoints, prefer TLS but allow fallback to non-TLS
            # when providers terminate SSL in non-standard ways.
            sslmode = "prefer"
        elif running_on_render or "render.com" in host:
            # Managed/cloud postgres commonly expects TLS.
            sslmode = "require"
        else:
            # Safe default for non-local hosts; override via DB_SSLMODE if needed.
            sslmode = "require"
    return {
        "sslmode": sslmode,
        "connect_timeout": int(os.environ.get("DB_CONNECT_TIMEOUT", "15")),
    }

if DATABASE_URL.startswith("postgres"):
    DATABASE_URL = apply_postgres_driver(
        DATABASE_URL,
        choose_postgres_driver(DATABASE_URL),
    )

DATABASE_URL = normalize_render_postgres_url(DATABASE_URL)

if DATABASE_URL.startswith("postgresql"):
    parsed_db = urlsplit(DATABASE_URL)
    db_host = parsed_db.hostname or "unknown"
    db_scheme = parsed_db.scheme
    db_driver = db_scheme.split("+", 1)[1] if "+" in db_scheme else "default"
    db_sslmode = get_postgres_connect_args(DATABASE_URL).get("sslmode", "unknown")
    print(f"[db] Using PostgreSQL host: {db_host} (driver={db_driver}, sslmode={db_sslmode})")

# PostgreSQL requires different engine settings
if DATABASE_URL.startswith("postgresql"):
    postgres_connect_args = get_postgres_connect_args(DATABASE_URL)
    engine = create_engine(
        DATABASE_URL,
        connect_args=postgres_connect_args,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
    )
else:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
