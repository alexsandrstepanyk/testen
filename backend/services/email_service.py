"""
Email sending service using SMTP.

Required environment variables:
  SMTP_HOST     — e.g. smtp.gmail.com
  SMTP_PORT     — e.g. 587
  SMTP_USER     — sender email address
  SMTP_PASS     — SMTP password / app password
  SMTP_FROM     — display "From" address (defaults to SMTP_USER)
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def _get_smtp_config():
    host = os.environ.get("SMTP_HOST", "")
    port = int(os.environ.get("SMTP_PORT", "587"))
    user = os.environ.get("SMTP_USER", "")
    password = os.environ.get("SMTP_PASS", "")
    from_addr = os.environ.get("SMTP_FROM", user)
    return host, port, user, password, from_addr


def is_email_configured() -> bool:
    host, _, user, password, _ = _get_smtp_config()
    return bool(host and user and password)


def send_email_with_pdf(
    to_email: str,
    subject: str,
    body_html: str,
    pdf_bytes: bytes,
    pdf_filename: str,
) -> None:
    """Send an email with a PDF attachment. Raises on failure."""
    host, port, user, password, from_addr = _get_smtp_config()
    if not (host and user and password):
        raise RuntimeError(
            "SMTP not configured. Set SMTP_HOST, SMTP_USER, SMTP_PASS environment variables."
        )

    msg = MIMEMultipart("mixed")
    msg["From"] = from_addr
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body_html, "html", "utf-8"))

    part = MIMEBase("application", "pdf")
    part.set_payload(pdf_bytes)
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{pdf_filename}"',
    )
    msg.attach(part)

    with smtplib.SMTP(host, port, timeout=20) as server:
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(from_addr, to_email, msg.as_string())
