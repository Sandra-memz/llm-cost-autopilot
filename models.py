from dataclasses import dataclass
@dataclass
class ModelConfig:
    name: str
    provider: str
    model_id: str
    cost_per_1m_input: float   
    cost_per_1m_output: float  
    tier: str 

MODEL_REGISTRY = [
    ModelConfig("small-model", "gemini", "gemini-3.5-flash-lite", 0.30, 2.50, "low"),
    ModelConfig("mid-model", "gemini", "gemini-3.8-flash", 0.75, 3.75, "medium"),
    ModelConfig("big-model", "gemini", "gemini-3.8-flash", 0.75, 3.75, "high"),
]