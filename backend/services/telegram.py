import os
import httpx


def _get_config():
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    return token, chat_id


def is_enabled():
    token, chat_id = _get_config()
    return bool(token and chat_id)


def send_message(text):
    token, chat_id = _get_config()
    if not (token and chat_id):
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        with httpx.Client(timeout=8.0) as client:
            res = client.post(url, data={"chat_id": chat_id, "text": text})
            res.raise_for_status()
        return True
    except Exception:
        return False


def send_pdf_document(pdf_bytes, filename, caption=""):
    token, chat_id = _get_config()
    if not (token and chat_id):
        return False
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    try:
        with httpx.Client(timeout=15.0) as client:
            res = client.post(
                url,
                data={"chat_id": chat_id, "caption": caption[:1024]},
                files={"document": (filename, pdf_bytes, "application/pdf")},
            )
            res.raise_for_status()
        return True
    except Exception:
        return False
