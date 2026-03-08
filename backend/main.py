import asyncio
from scrapers.rss_scraper import scrape_all_feeds
from analysis.sentiment_analyzer import analyze_articles
from db.supabase_client import store_signals
from alerts.telegram_alert import send_alert

async def run_pipeline():
    print("Scraping news feeds...")
    articles = scrape_all_feeds()
    
    print(f"Found {len(articles)} articles. Analyzing...")
    signals = analyze_articles(articles)
    
    print(f"Storing {len(signals)} signals...")
    store_signals(signals)
    
    high_confidence = [s for s in signals if s.get('confidence', 0) >= 0.75]
    for signal in high_confidence:
        await send_alert(signal)
        print(f"Alert sent: {signal['headline'][:60]}...")

    print("Pipeline complete.")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
