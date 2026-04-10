"""Expo Push Notification servisi.

Mobil kullanıcılara analiz tamamlandığında bildirim gönderir.
"""
import http.client
import json
import logging

log = logging.getLogger(__name__)

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"


def _send_expo_push(messages: list[dict]) -> dict | None:
    """Expo push API'ye istek gönderir.

    messages format:
    [{"to": "ExponentPushToken[...]", "title": "...", "body": "...", "data": {...}}]
    """
    if not messages:
        return None
    payload = json.dumps({"messages": messages}).encode("utf-8")
    try:
        conn = http.client.HTTPSConnection("exp.host", timeout=10)
        conn.request(
            "POST",
            "/--/api/v2/push/send",
            body=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        resp = conn.getresponse()
        data = json.loads(resp.read().decode("utf-8"))
        conn.close()
        return data
    except Exception as e:
        log.warning("Expo push send failed: %s", e)
        return None


def send_analysis_complete_notification(
    push_token: str,
    user_name: str = "",
    analysis_id: int | None = None,
) -> dict | None:
    """Analiz tamamlandığında kullanıcıya bildirim gönderir."""
    name = user_name or "Kullanıcı"
    title = "Analiz Tamamlandı"
    body = f"{name}, tahlil analiziniz hazır. Uygulamayı açarak detayları görüntüleyin."
    messages = [
        {
            "to": push_token,
            "title": title,
            "body": body,
            "data": {
                "type": "analysis_complete",
                "analysis_id": analysis_id,
            },
            "sound": "default",
        }
    ]
    result = _send_expo_push(messages)
    if result:
        log.info("Push notification sent to %s: %s", push_token[:20], result)
    return result
