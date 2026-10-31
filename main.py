from fastapi import FastAPI
from pydantic import BaseModel
from classifier import score_complexity
from models import MODEL_REGISTRY
from database import init_db, log_request, get_stats
from llm_client import call_model

app = FastAPI()
init_db()

class RouteRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{"Message:" "LLM cost autopilot is running"}

@app.post("/route")
def route(request: RouteRequest):
    tier = score_complexity(request.prompt)
    chosen = next(m for m in MODEL_REGISTRY if m.tier == tier)
    answer, tokens_in, tokens_out = call_model(chosen.model_id, request.prompt)
    cost = (tokens_in * chosen.cost_per_1m_input + tokens_out * chosen.cost_per_1m_output) / 1_000_000
    biggest = next(m for m in MODEL_REGISTRY if m.tier == "high")
    baseline_cost = (tokens_in * biggest.cost_per_1m_input + tokens_out * biggest.cost_per_1m_output) / 1_000_000
    log_request(request.prompt, tier, chosen.name, tokens_in, tokens_out, cost, baseline_cost)
    return {
        "prompt": request.prompt,
        "complexity": tier,
        "chosen_model": chosen.name,
        "model_id": chosen.model_id,
        "answer": answer,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "cost": round(cost, 8),
        "baseline_cost": round(baseline_cost, 8),
        "saved": round(baseline_cost - cost, 8),
       }

@app.get("/stats")
def stats():
    total, cost, baseline = get_stats()
    saved = baseline - cost
    percent = round(saved / baseline * 100, 1) if baseline else 0
    return {
        "total_requests": total,
        "total_cost": round(cost, 8),
        "baseline_cost": round(baseline, 8),
        "total_saved": round(saved, 8),
        "percent_saved": percent,
    }