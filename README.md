# Movie Rating Prediction (Sentiment Analysis)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Project Overview
This project predicts the sentiment (Positive/Negative) of a movie review using a Logistic Regression model trained on the IMDB dataset of 50K movie reviews.

## Features
- **Real-time Sentiment Analysis**: Type a review and get instant feedback
- **Confidence Score**: See how confident the model is in its prediction
- **Modern UI**: Dark themed, glassmorphism design
- **RESTful API**: FastAPI backend with automatic documentation
- **Easy Deployment**: Simple setup scripts included

## Project Structure
```
Movies_rating_prediction/
├── app/                    # FastAPI backend
│   ├── __init__.py
│   ├── main.py            # API endpoints
│   ├── model.pkl          # Trained model (generated)
│   └── vectorizer.pkl     # TF-IDF vectorizer (generated)
├── frontend/              # Web interface
│   ├── index.html         # Main HTML file
│   ├── style.css          # Styling
│   └── script.js          # Frontend logic
├── src/                   # Training scripts
│   ├── __init__.py
│   └── train_model.py     # Model training script
├── archive/               # Dataset directory
│   ├── README.md          # Dataset instructions
│   └── .gitkeep          # Keeps directory in Git
├── .gitignore            # Git ignore rules
├── .gitattributes        # Git LFS configuration
├── CONTRIBUTING.md       # Contribution guidelines
├── requirements.txt      # Python dependencies
├── setup.sh              # Setup script
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AIMindCrafter/Movies_rating_prediction.git
   cd Movies_rating_prediction
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh  # Make script executable (Unix/Linux/Mac)
   ./setup.sh         # Run setup
   ```
   
   Or manually:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Download the dataset** (Required for training)
   - Visit [IMDB Dataset on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
   - Download and extract `IMDB Dataset.csv`
   - Place it in the `archive/` directory

4. **Train the model** (First time only)
   ```bash
   cd src
   python train_model.py
   ```

## Running the Application

### 1. Start the Backend (API)
The backend serves the model at `http://localhost:8000`.
```bash
# From the root directory
uvicorn app.main:app --reload --port 8000
```

API documentation available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 2. Start the Frontend
The frontend provides a user interface for sentiment analysis.
```bash
cd frontend
python -m http.server 8081
```

Open http://localhost:8081 in your browser.

## API Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `POST /predict` - Predict sentiment of a review
  ```json
  {
    "text": "This movie was absolutely amazing!"
  }
  ```
  Response:
  ```json
  {
    "sentiment": "Positive",
    "confidence": 0.95
  }
  ```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Setting up your development environment
- Resolving permission issues
- Making code contributions
- Creating pull requests

### Common Permission Issues

If you encounter permission errors when trying to deploy or push files:

1. **Fork the repository** - You cannot push directly to the main repository
2. **Clone your fork** - Work on your own copy
3. **Create a Pull Request** - Submit changes for review

For detailed troubleshooting, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Technologies Used

- **Backend**: FastAPI, scikit-learn, pandas
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **ML Model**: Logistic Regression with TF-IDF vectorization
- **Dataset**: IMDB 50K Movie Reviews

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- IMDB Dataset from [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- FastAPI framework for the backend API
- scikit-learn for machine learning capabilities
