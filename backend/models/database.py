from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from urllib.parse import urlsplit, urlunsplit

# Get the backend directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Support both SQLite (local) and PostgreSQL (Render)
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(BASE_DIR, 'test_results.db')}"
)


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

    # Repair short Render DB host IDs such as dpg-...-a
    if host.startswith("dpg-") and "." not in host:
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
    sslmode = os.environ.get("DB_SSLMODE")
    if not sslmode:
        sslmode = "require" if "render.com" in host else "prefer"
    return {
        "sslmode": sslmode,
        "connect_timeout": int(os.environ.get("DB_CONNECT_TIMEOUT", "15")),
    }

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if DATABASE_URL.startswith("postgresql://"):
    # Prefer psycopg v3 driver for better TLS compatibility on managed hosts.
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

DATABASE_URL = normalize_render_postgres_url(DATABASE_URL)

if DATABASE_URL.startswith("postgresql"):
    parsed_db = urlsplit(DATABASE_URL)
    db_host = parsed_db.hostname or "unknown"
    db_sslmode = os.environ.get("DB_SSLMODE") or ("require" if "render.com" in db_host else "prefer")
    print(f"[db] Using PostgreSQL host: {db_host} (sslmode={db_sslmode})")

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
