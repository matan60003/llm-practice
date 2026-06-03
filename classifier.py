def classifier_text(text: str) -> str:
    if "מחיר" in text or "כסף" in text:
        return "פיננסי"
    return "כללי"