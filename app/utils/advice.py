# Simple advice engine based on risk score
def generate_advice(category: str, score: float) -> str:
    advice = ""
    if category == "sleep":
        if score >= 4:
            advice = "Try consistent sleep schedule, no screens 1h before sleep, cool dark room."
        elif score >= 2:
            advice = "Improve sleep hygiene, meditate, reduce caffeine."
        else:
            advice = "Keep your good sleep habits!"
    elif category == "stress":
        if score >= 4:
            advice = "Do daily exercise, breathing exercises, and mindfulness."
        elif score >= 2:
            advice = "Take short breaks, stay active, manage tasks."
        else:
            advice = "Continue your balanced lifestyle!"
    return advice
