def score_complexity(prompt: str) -> str:
    """Return 'low', 'medium' or 'high' depending on how hard the prompt looks."""
    text = prompt.lower()
    points = 0

    # Longer prompts tend to be harder
    if len(text.split()) > 50:
        points += 1
    if len(text.split()) > 150:
        points += 1

    # Words that suggest deeper thinking
    hard_words = ["analyze", "compare", "explain why", "step by step",
                  "design", "debug", "prove", "optimize", "trade-off"]
    for word in hard_words:
        if word in text:
            points += 1

    # Code usually needs a stronger model
    if "```" in prompt or "def " in text or "function" in text:
        points += 2

    if points >= 3:
        return "high"
    if points >= 1:
        return "medium"
    return "low"