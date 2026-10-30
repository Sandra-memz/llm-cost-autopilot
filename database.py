import sqlite3
from datetime import datetime

DB_FILE = "autopilot.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            prompt TEXT,
            complexity TEXT,
            chosen_model TEXT,
            tokens_in INTEGER,
            tokens_out INTEGER,
            cost REAL,
            baseline_cost REAL
        )
    """)
    conn.commit()
    conn.close()


def log_request(prompt, complexity, chosen_model, tokens_in, tokens_out, cost, baseline_cost):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO requests (created_at, prompt, complexity, chosen_model, tokens_in, tokens_out, cost, baseline_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), prompt, complexity, chosen_model, tokens_in, tokens_out, cost, baseline_cost),
    )
    conn.commit()
    conn.close()