# Focus — Explain It At My Level

**Problem:** Confusing text (research papers, legal clauses, error messages, dense
news articles) is often technically "explained" somewhere online — but at the
wrong level for the reader. A beginner gets jargon; an expert gets condescension.

**Solution:** Paste any confusing text, pick how much you already know
(5-year-old / high schooler / college student / adjacent professional), and get
an explanation tailored to exactly that level — powered by Claude.

## How it works

1. You paste text into the box and choose a level.
2. The Flask backend sends your text to the Gemini API with a system prompt
   that adapts vocabulary, analogies, and technical depth to the chosen level.
3. The explanation comes back and renders in a clean reveal panel.

## Tech stack

- **Backend:** Python, Flask, Google Gen AI SDK (Interactions API)
- **Frontend:** vanilla HTML/CSS/JS (no build step, no framework — fast to run anywhere)
- **AI:** Google Gemini (`gemini-3.6-flash`) — free tier, no credit card required

## Setup

```bash
# 1. Clone the repo and enter it
git clone <your-repo-url>
cd explain-my-level

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key (free, no credit card — sign in with a Google account)
cp .env.example .env
# then open .env and paste your key from https://aistudio.google.com/apikey

# 5. Run it
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## Project structure

```
explain-my-level/
├── app.py                  # Flask backend + Claude API call
├── templates/
│   └── index.html          # Main page
├── static/
│   ├── css/style.css       # Styling
│   └── js/main.js          # Frontend logic (fetch calls, UI state)
├── requirements.txt
├── .env.example
└── README.md
```

## Future potential

- Support file/PDF uploads instead of paste-only
- Save explanation history per user
- Browser extension: highlight text on any page → right-click → "Focus"
- Side-by-side "before/after" comparison view
- Multi-language explanations

## Built for

24-hour open-innovation hackathon — built solo.
