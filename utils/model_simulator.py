def predict_risk(text):
    if not text or not text.strip():
        return "Unknown"
    text = text.lower()
    if "chest pain" in text:
        return "HighRisk"
    elif "fever" in text:
        return "MediumRisk"
    return "LowRisk"
