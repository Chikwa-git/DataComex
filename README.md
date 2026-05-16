# DataComex

A Brazilian foreign trade analysis tool powered by artificial intelligence.

Query real export and import data by product (NCM code) and receive AI-generated
insights on geographic patterns, trends, and opportunities.

## Tech Stack

- Python + Flask
- ComexStat public API (Brazilian Ministry of Trade)
- Groq (Llama 3.3 70B)
- SQLite for local caching
- Bootstrap 5

## Getting Started

1. Clone the repository
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Create a .env file in the root directory:
   GROQ_API_KEY=your_key_here
5. Run the server:
   python run.py
6. Open http://127.0.0.1:5000

## Features

- Query by NCM code, year, and trade flow (export or import)
- Top 10 destination/origin countries with FOB value
- Monthly trade evolution
- AI-generated analysis with contextual insights beyond the raw data
- Local SQLite cache to avoid redundant API calls
