import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("KIMI_API_KEY"),
    base_url="https://api.moonshot.cn/v1"
)

SYSTEM_PROMPT = """You are a financial sentiment analyst specializing in macro news.
Analyze news articles and determine whether the market's likely emotional reaction 
is PROPORTIONATE or DISPROPORTIONATE to what the underlying data actually supports.

You are helping an options seller who profits when markets OVERREACT and then mean-revert.

Respond ONLY with a valid JSON object, no markdown, no preamble:
{
  "raw_sentiment": float (-1.0 very bearish to 1.0 very bullish),
  "disproportion_score": float (0.0 = perfectly proportionate, 1.0 = massively overblown),
  "confidence": float (0.0 to 1.0),
  "direction": "bullish_overcorrection" | "bearish_overcorrection" | "proportionate",
  "timeframe_days": int (days until likely mean reversion, 1-10),
  "reasoning": "2 sentences max, plain english"
}"""

def analyze_articles(articles: list) -> list:
    signals = []
    for article in articles:
        try:
            prompt = f"Headline: {article['headline']}\nSource: {article['source']}\nSummary: {article['summary'][:500]}\n\nAnalyze this macro news article."

            response = client.chat.completions.create(
                model="moonshot-v1-8k",
                max_tokens=300,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )

            result = json.loads(response.choices[0].message.content)
            signals.append({**article, **result})
        except Exception as e:
            print(f"Error analyzing '{article.get('headline', '')[:40]}': {e}")
    return signals
