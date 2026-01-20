"""
FastAPI backend for Movie Rating Prediction

This module provides the API endpoints for sentiment analysis of movie reviews.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os

# Initialize FastAPI app
app = FastAPI(
    title="Movie Rating Prediction API",
    description="Sentiment analysis API for movie reviews",
    version="1.0.0"
)

# Configure CORS
# WARNING: In production, replace "*" with specific allowed origins
# For development only - allows all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: In production, specify exact origins: ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Review(BaseModel):
    text: str

# Response model
class PredictionResponse(BaseModel):
    sentiment: str
    confidence: float

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Movie Rating Prediction API",
        "status": "running",
        "endpoints": {
            "predict": "/predict",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(review: Review):
    """
    Predict sentiment of a movie review
    
    Args:
        review: Review object containing the text to analyze
        
    Returns:
        PredictionResponse with sentiment and confidence score
        
    Note:
        This is currently a PLACEHOLDER implementation.
        The actual model needs to be trained first using src/train_model.py
    """
    # TODO: Load and use the trained model
    # Uncomment the following when model files are available:
    # try:
    #     model = pickle.load(open('app/model.pkl', 'rb'))
    #     vectorizer = pickle.load(open('app/vectorizer.pkl', 'rb'))
    #     text_vectorized = vectorizer.transform([review.text])
    #     prediction = model.predict(text_vectorized)[0]
    #     confidence = model.predict_proba(text_vectorized).max()
    #     sentiment = "Positive" if prediction == 1 else "Negative"
    #     return PredictionResponse(sentiment=sentiment, confidence=float(confidence))
    # except FileNotFoundError:
    #     raise HTTPException(status_code=503, detail="Model not trained yet. Run src/train_model.py first.")
    
    # PLACEHOLDER response for testing without trained model
    return PredictionResponse(
        sentiment="Positive",
        confidence=0.85
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
