import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

DIRECTION_EMOJI = {
    "bullish_overcorrection": "🟢",
    "bearish_overcorrection": "🔴",
    "proportionate": "⚪"
}

async def send_alert(signal: dict) -> None:
    emoji = DIRECTION_EMOJI.get(signal.get("direction"), "⚪")
    confidence_pct = int(signal.get("confidence", 0) * 100)
    disproportion_pct = int(signal.get("disproportion_score", 0) * 100)
    direction_label = signal.get("direction", "N/A").replace("_", " ").title()

    message = (
        f"{emoji} *SIGNAL DETECTED*\n\n"
        f"📰 *{signal.get('source')}*\n"
        f"{signal.get('headline')}\n\n"
        f"📊 *Disproportion:* {disproportion_pct}%\n"
        f"🎯 *Confidence:* {confidence_pct}%\n"
        f"📈 *Direction:* {direction_label}\n"
        f"⏱ *Timeframe:* ~{signal.get('timeframe_days', '?')} days\n\n"
        f"💭 _{signal.get('reasoning', '')}_"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    })
