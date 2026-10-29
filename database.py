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
            chosen_model TEXT
        )
    """)
    conn.commit()
    conn.close()


def log_request(prompt, complexity, chosen_model):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO requests (created_at, prompt, complexity, chosen_model) VALUES (?, ?, ?, ?)",
        (datetime.now().isoformat(), prompt, complexity, chosen_model),
    )
    conn.commit()
    conn.close()