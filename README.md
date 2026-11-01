# LLM Cost Autopilot

A routing layer that sits in front of LLM calls. It scores how complex each prompt is, sends it to the cheapest model that can handle it, and logs the cost so you can see how much was saved compared with always using the biggest model.

## What it does

- Scores each prompt as low, medium or high complexity (rule-based classifier)
- Routes it to a matching model from a registry (currently free Gemma models via the Gemini API)
- Returns the model's answer, token counts, cost, and the amount saved
- Logs every request in SQLite
- Shows totals on a Streamlit dashboard

## Tech stack

Python, FastAPI, SQLite, Streamlit, Google Gemini API

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project folder:
   ```
   GEMINI_API_KEY=your-key-here
   ```
   Get a key from https://aistudio.google.com/api-keys

## Run

API server:
```
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000/docs and try `POST /route`.

Dashboard (in a second terminal):
```
streamlit run dashboard.py
```

## Endpoints

- `POST /route`: send `{"prompt": "..."}` and get the answer plus cost details
- `GET /stats`: total requests, cost, and percent saved

## Notes

- Prices in the model registry are placeholder values used to calculate savings. Real usage on the free tier costs nothing.
- The classifier is keyword-based, so some hard prompts may be routed to a cheaper model than ideal. Planned improvements: a quality-check step and a trained classifier.