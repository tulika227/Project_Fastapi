from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(
    title="Smart Text Classifier API",
    description="Classifies business text into Technical, Billing, or General",
    version="1.0"
)

class TextRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    category: str

@app.post("/predict", response_model=PredictionResponse)
def predict_category(request: TextRequest):
    prediction = model.predict([request.text])[0]
    return {"category": prediction}
