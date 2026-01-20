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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
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
    """
    # TODO: Load and use the trained model
    # This is a placeholder implementation
    # When you add the actual model, load it here:
    # model = pickle.load(open('model.pkl', 'rb'))
    # vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    
    # Placeholder response
    # Replace this with actual model prediction
    return PredictionResponse(
        sentiment="Positive",
        confidence=0.85
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
