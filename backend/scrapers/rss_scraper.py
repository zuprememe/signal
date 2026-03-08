import feedparser
from datetime import datetime, timezone

FEEDS = {
    "Reuters": "https://feeds.reuters.com/reuters/businessNews",
    "BBC": "http://feeds.bbci.co.uk/news/business/rss.xml",
    "NYT Economy": "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
}

MACRO_KEYWORDS = [
    "fed", "inflation", "interest rate", "gdp", "tariff", "recession",
    "employment", "jobs", "cpi", "fomc", "treasury", "yield", "s&p",
    "nasdaq", "market", "geopolit", "sanctions", "war", "trade",
    "bank", "debt", "deficit", "china", "oil", "supply chain"
]

def is_macro_relevant(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(kw in text for kw in MACRO_KEYWORDS)

def scrape_all_feeds() -> list:
    articles = []
    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                if is_macro_relevant(title, summary):
                    articles.append({
                        "source": source,
                        "headline": title,
                        "summary": summary,
                        "url": entry.get("link", ""),
                        "published": entry.get("published", str(datetime.now(timezone.utc)))
                    })
        except Exception as e:
            print(f"Error scraping {source}: {e}")
    return articles
