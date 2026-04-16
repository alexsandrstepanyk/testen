import os
import httpx


def _get_config():
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "312248641").strip()
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


def send_video(video_bytes, filename, caption="", content_type="video/mp4"):
    """Upload video to Telegram and return file_id if successful"""
    token, chat_id = _get_config()
    if not (token and chat_id):
        return None
    url = f"https://api.telegram.org/bot{token}/sendVideo"
    try:
        with httpx.Client(timeout=30.0) as client:
            res = client.post(
                url,
                data={"chat_id": chat_id, "caption": caption[:1024]},
                files={"video": (filename, video_bytes, content_type or "application/octet-stream")},
            )
            res.raise_for_status()
            result = res.json()
            if result.get("ok") and result.get("result"):
                return result["result"].get("video", {}).get("file_id")
        return None
    except Exception as e:
        print(f"Error sending video to Telegram: {str(e)[:100]}")
        return None


def get_file_download_url(file_id):
    token, _chat_id = _get_config()
    if not token or not file_id:
        return None
    url = f"https://api.telegram.org/bot{token}/getFile"
    try:
        with httpx.Client(timeout=15.0) as client:
            res = client.get(url, params={"file_id": file_id})
            res.raise_for_status()
            payload = res.json()
        if not payload.get("ok"):
            return None
        file_path = payload.get("result", {}).get("file_path")
        if not file_path:
            return None
        return f"https://api.telegram.org/file/bot{token}/{file_path}"
    except Exception:
        return None
