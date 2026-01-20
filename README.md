# Task 4: Movie Rating Prediction (Sentiment Analysis)

## Project Overview
This project predicts the sentiment (Positive/Negative) of a movie review using a Logistic Regression model trained on the standard IMDB dataset.

## Structure
- `app/`: Contains the FastAPI backend (`main.py`)
- `frontend/`: Contains the HTML/CSS/JS frontend
- `src/`: Training scripts
- `app/`: Contains the trained `.pkl` models
- `archive/`: Contains the dataset

## How to Run

### 1. Backend (API)
The backend serves the model at `http://localhost:8000`.
```bash
# Run from the root directory
uvicorn app.main:app --port 8000 --reload
```

### 2. Frontend
The frontend allows you to interact with the API.
```bash
cd frontend
python -m http.server 8081
```
Open [http://localhost:8081](http://localhost:8081) in your browser.

## Features
- **Real-time Sentiment Analysis**: Type a review and get instant feedback.
- **Confidence Score**: See how sure the model is.
- **Modern UI**: Dark themed, glassmorphism design.
