# 📊 DataComex - Brazilian Foreign Trade Intelligence

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-black)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange)](https://console.groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]()

> **AI-powered query tool for Brazilian export/import data (ComexStat)** — transform raw government trade data into actionable business insights.

---

## 🎯 The Problem

Brazilian foreign trade professionals, analysts, and small exporters face a common challenge: **ComexStat data is powerful but difficult to access and interpret**. Raw spreadsheets, complex APIs, and lack of contextual analysis make quick decision-making nearly impossible.

**DataComex solves this** by combining real government data with AI-generated insights — turning numbers into business intelligence.

---

## ✨ Features

- 🔍 **Query by NCM code** (Brazilian product classification)
- 📈 **Trade flow analysis**: Export or import, any year (1989–present)
- 🌎 **Geographic intelligence**: Top 10 destination/origin countries with FOB values
- 📅 **Monthly evolution tracking** — spot seasonal patterns
- 🤖 **AI-powered insights** (Llama 3.3 via Groq):
  - Market trend analysis
  - Opportunity identification
  - Context beyond raw numbers
- 💾 **Smart caching** with SQLite — avoids redundant API calls
- 📱 **Responsive design** with Bootstrap 5

---

## 🖼️ Preview

*(Add a screenshot here! I recommend showing: search form + results page with AI analysis)*

**Example query and AI insight:**

```
NCM: 0901.11.10 (Coffee, not roasted)
Flow: Export
Year: 2024

AI Insight:
"Brazilian coffee exports to Germany increased 23% in Q3 2024, driven by...
Potential opportunity: Premium coffee segments to Scandinavia..."
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.10+ / Flask |
| **Frontend** | Bootstrap 5 + Jinja2 templates |
| **External API** | ComexStat (Brazilian Ministry of Trade) |
| **AI Provider** | Groq (Llama 3.3 70B) |
| **Cache** | SQLite (24h TTL) |
| **HTTP Client** | Requests |
| **Config** | python-dotenv |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Groq API key ([free tier at console.groq.com](https://console.groq.com/))

### Installation

```bash
# Clone the repository
git clone https://github.com/Chikwa-git/DataComex.git
cd DataComex

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API key
echo "GROQ_API_KEY=your_api_key_here" > .env

# Run the application
python run.py
```

Open http://127.0.0.1:5000 in your browser.

---

## 📖 How It Works

1. User inputs NCM code, year, and trade flow (export/import)
2. Flask backend queries the ComexStat API with caching
3. Data is processed and displayed in tables (top countries + monthly evolution)
4. AI analysis is generated on-demand via Groq (Llama 3.3)
5. Results are cached for 24 hours to minimize API calls

---

## 📁 Project Structure

```
DataComex/
├── app/
│   ├── __init__.py      # Flask app factory
│   ├── routes.py        # Main endpoints
│   ├── comex_api.py     # ComexStat API wrapper
│   ├── ai_service.py    # Groq integration
│   ├── cache.py         # SQLite caching logic
│   └── templates/       # HTML templates
├── .env                 # API keys (not committed)
├── requirements.txt     # Python dependencies
├── run.py               # Entry point
└── README.md            # This file
```

---

## 🧪 Example Use Cases

| User | How DataComex helps |
|------|---------------------|
| Small exporter | Find best destination countries for your product |
| Trade analyst | Track monthly trends and seasonality |
| Student | Learn NCM codes and trade flows interactively |
| Researcher | Validate hypotheses about Brazilian trade patterns |

---

## 🔮 Future Improvements

- Compare multiple NCM codes side by side
- Historical trend charts with Plotly
- PDF report export
- Alert system for trade flow changes
- Docker containerization

---

## 👤 Author

**Lincoln Okoti Neves**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/lincoln-neves100/)
[![GitHub](https://img.shields.io/badge/GitHub-Chikwa--git-lightgrey)](https://github.com/Chikwa-git)

Former foreign trade professional turned developer — building tools at the intersection of trade data and AI.

---

## 📚 Part of My Portfolio

- [Radar Político](https://github.com/Chikwa-git/political-tracker) — Parliamentary transparency with AI
- **DataComex** — Brazilian foreign trade intelligence *(you are here)*
- [Nucleus](https://github.com/Chikwa-git/nucleus) — Multi-provider document summarizer

---

## 📄 License

MIT — feel free to use, modify, and contribute.

---

## 🙏 Acknowledgments

- [ComexStat API](https://comexstat.mdic.gov.br/) — Brazilian Ministry of Trade
- [Groq](https://console.groq.com/) — Lightning-fast Llama inference
- [CS50x](https://cs50.harvard.edu/x/) — Where this journey began

---

*Made with ☕ and Python — because trade data shouldn't be locked in spreadsheets.*
