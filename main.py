from fastapi import FastAPI
from pydantic import BaseModel
from classifier import score_complexity
from models import MODEL_REGISTRY
from database import init_db, log_request

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
    log_request(request.prompt, tier, chosen.name)
    return {
        "prompt": request.prompt,
        "complexity": tier,
         "chosen_model": chosen.name,
        "model_id": chosen.model_id,
       }
