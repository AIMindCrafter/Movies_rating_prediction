#!/bin/bash

# Deployment script for Movie Rating Prediction project
# This script helps set up and deploy the project

set -e  # Exit on error

echo "========================================"
echo "Movie Rating Prediction - Setup Script"
echo "========================================"

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Check if dataset exists
if [ ! -f "archive/IMDB Dataset.csv" ]; then
    echo ""
    echo "⚠️  Warning: Dataset not found!"
    echo "Please download the IMDB dataset from:"
    echo "https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews"
    echo "and place it in the archive/ directory"
    echo ""
fi

# Check if model exists
if [ ! -f "app/model.pkl" ]; then
    echo ""
    echo "⚠️  Model not found. You need to train the model first."
    echo "Run: python src/train_model.py"
    echo ""
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start the application:"
echo "  1. Backend:  uvicorn app.main:app --reload --port 8000"
echo "  2. Frontend: cd frontend && python -m http.server 8081"
echo ""
echo "For more information, see CONTRIBUTING.md"
echo "========================================"
