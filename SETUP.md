# Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- Git

## Environment Variables
Create a `.env` file in `/backend`:
```
ANTHROPIC_API_KEY=your_key_here
NYT_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

## Backend Setup
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

## Frontend Setup
```powershell
cd frontend
npm install
npm run dev
```

## Running the Scraper Manually
```powershell
cd backend
python main.py
```

## Supabase Table (run this SQL in your Supabase project dashboard)
```sql
create table signals (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default now(),
  headline text,
  source text,
  topic text,
  raw_sentiment float,
  disproportion_score float,
  confidence float,
  direction text,
  timeframe_days int,
  reasoning text,
  resolved boolean default false,
  outcome text,
  was_correct boolean
);
```

## GitHub Actions Secrets
Add these in your repo Settings > Secrets > Actions:
- ANTHROPIC_API_KEY
- NYT_API_KEY
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
- SUPABASE_URL
- SUPABASE_KEY
