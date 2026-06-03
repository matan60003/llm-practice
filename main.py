from fastapi import FastAPI
from pydantic import BaseModel
from classifier import classifier_text  # מייבאים את הפונקציה היציבה שלנו!

# 1. יצירת האפליקציה של השרת
app = FastAPI(title="Text Classification Service")

# 2. הגדרת המודל של הבקשה (Validation עם Pydantic)
# אנחנו מגדירים לשרת בדיוק איזה JSON אנחנו מצפים לקבל מהמשתמש
class ClassifyRequest(BaseModel):
    text: str

# 3. יצירת נקודת הקצה (Endpoint) מסוג POST
@app.post("/classify")
def classify_endpoint(request_data: ClassifyRequest):
    # אקסוורט (חילוץ) הטקסט מתוך ה-JSON שהמשתמש שלח
    user_text = request_data.text
    
    # הפעלת הלוגיקה שבנינו קודם לכן
    category = classifier_text(user_text)
    
    # החזרת תשובה מובנית בפורמט JSON למשתמש
    return {
        "original_text": user_text,
        "category": category
    }