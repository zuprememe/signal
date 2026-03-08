import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def store_signals(signals: list) -> None:
    for signal in signals:
        try:
            supabase.table("signals").insert({
                "headline": signal.get("headline"),
                "source": signal.get("source"),
                "topic": "macro",
                "raw_sentiment": signal.get("raw_sentiment"),
                "disproportion_score": signal.get("disproportion_score"),
                "confidence": signal.get("confidence"),
                "direction": signal.get("direction"),
                "timeframe_days": signal.get("timeframe_days"),
                "reasoning": signal.get("reasoning"),
            }).execute()
        except Exception as e:
            print(f"Error storing signal: {e}")

def fetch_recent_signals(limit: int = 20) -> list:
    response = supabase.table("signals") \
        .select("*") \
        .order("created_at", desc=True) \
        .limit(limit) \
        .execute()
    return response.data
