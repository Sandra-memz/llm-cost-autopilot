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
    ModelConfig("small-model", "gemini", "gemma-4-26b-a4b-it", 0.10, 0.40, "low"),
    ModelConfig("mid-model", "gemini", "gemma-4-26b-a4b-it", 0.10, 0.40, "medium"),
    ModelConfig("big-model", "gemini", "gemma-4-31b-it", 0.30, 1.20, "high"),
]