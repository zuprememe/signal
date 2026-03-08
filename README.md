# Signal 📡
> AI-powered macro news sentiment analyzer for options traders

Signal scrapes macro news across multiple outlets, strips media bias using Claude AI, and detects whether market reactions are overblown or legitimate — giving options traders an edge before Monday open.

## How It Works
1. **Scraper** pulls headlines from Reuters, AP, BBC, NYT across macro/geopolitical topics
2. **Kimi AI** strips bias and scores sentiment disproportion (is the reaction warranted?)
3. **Supabase** stores predictions with timestamps for accuracy tracking
4. **Dashboard** displays live signals and historical prediction accuracy
5. **Telegram** alerts when a high-confidence overcorrection is detected

## Stack
- Frontend: React + Vite → GitHub Pages
- Backend: Python (scraper + Claude API + Telegram)
- Database: Supabase
- Scheduler: GitHub Actions (free, no server needed)
- News: RSS feeds + NYT Developer API

## Setup
See SETUP.md for full environment setup instructions.
