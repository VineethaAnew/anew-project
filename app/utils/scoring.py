# Example scoring logic based on user answer
def calculate_risk_score(question: str, answer: str) -> float:
    """
    Simple risk scoring: 0 (low) - 5 (high)
    Map answers to risk scores based on predefined logic
    """
    mapping = {
        "rarely": 0,
        "sometimes": 2,
        "often": 4,
        "daily": 5
    }
    return mapping.get(answer.lower(), 0)
