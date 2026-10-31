import sqlite3
import pandas as pd
import streamlit as st

st.title("LLM Cost Autopilot")

conn = sqlite3.connect("autopilot.db")
df = pd.read_sql_query("SELECT * FROM requests", conn)
conn.close()

if df.empty:
    st.info("No requests yet. Send some prompts to /route first.")
else:
    df["saved"] = df["baseline_cost"] - df["cost"]
    total_saved = df["saved"].sum()
    percent = total_saved / df["baseline_cost"].sum() * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Requests", len(df))
    col2.metric("Total saved", f"${total_saved:.6f}")
    col3.metric("Percent saved", f"{percent:.1f}%")

    st.subheader("Requests per model")
    st.bar_chart(df["chosen_model"].value_counts())

    st.subheader("Recent requests")
    recent = df.sort_values("id", ascending=False)
    st.dataframe(recent[["created_at", "prompt", "complexity", "chosen_model", "cost", "saved"]])