Focus — Explain It At My Level

I built this because I kept running into the same problem: explanations exist for almost anything online, but they're rarely at my level. Either I'm drowning in jargon, or I'm being talked down to. So this tool asks you upfront how much you already know, then explains accordingly.

How it works: paste in whatever's confusing you — a paragraph from a paper, a legal clause, an error message — pick a level from "explain it like I'm 5" to "I work in an adjacent field," and it generates an explanation tuned to that.

Under the hood
You paste text and pick a level.
The Flask backend sends it to the Gemini API with a system prompt that adjusts vocabulary, analogies, and technical depth based on your choice.
The explanation renders back in the panel below.
Built with
Python + Flask on the backend
Plain HTML/CSS/JS on the frontend — no framework, nothing to build
Google Gemini (gemini-3.6-flash) for the actual explaining — free tier, no card needed
Setup
bash
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

Open http://127.0.0.1:5000 in your browser.

Project structure
explain-my-level/
├── app.py                  # Flask backend + Gemini API call
├── templates/
│   └── index.html          # Main page
├── static/
│   ├── css/style.css       # Styling
│   └── js/main.js          # Frontend logic (fetch calls, UI state)
├── requirements.txt
├── .env.example
└── README.md
What I'd add next

If I had more than 24 hours: PDF/file upload instead of paste-only, a browser extension so you can highlight text on any page and get it explained without switching tabs, and a side-by-side before/after view so you can see the original next to the explanation.

Note

Built solo for a 24-hour open-innovation hackathon.