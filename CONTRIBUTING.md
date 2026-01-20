# Contributing to Movies Rating Prediction

Thank you for your interest in contributing to this project! This guide will help you set up the project and resolve common permission issues.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

### Setup Instructions

1. **Fork the Repository**
   - Go to https://github.com/AIMindCrafter/Movies_rating_prediction
   - Click the "Fork" button in the top right corner

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Movies_rating_prediction.git
   cd Movies_rating_prediction
   ```

3. **Set Up Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Resolving Permission Issues

### Common Issues and Solutions

#### 1. **Cannot Push to Repository**
If you see "Permission denied" when trying to push:
- **Solution**: Fork the repository and push to your fork, then create a Pull Request
- Never try to push directly to the main repository unless you're a collaborator

#### 2. **Large Files (Models/Datasets)**
Models (`.pkl`) and datasets (`.csv`, `.zip`) are excluded from Git by default via `.gitignore`:
- **Solution**: Use Git LFS (Large File Storage) for large files
  ```bash
  git lfs install
  git lfs track "*.pkl"
  git lfs track "*.csv"
  git add .gitattributes
  ```
- Alternatively, provide download links or instructions to obtain these files

#### 3. **Directory Structure Not Present**
The repository needs the following structure:
```
Movies_rating_prediction/
├── app/
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── src/
│   └── train_model.py
├── archive/
│   └── (dataset files - not tracked in git)
├── requirements.txt
└── README.md
```

## Project Structure Setup

### Creating the Directory Structure

Run these commands to create the necessary directories:
```bash
mkdir -p app frontend src archive
```

### Adding Placeholder Files

Create placeholder files to maintain directory structure:
```bash
touch app/__init__.py
touch frontend/index.html
touch src/__init__.py
touch archive/.gitkeep
```

## Making Contributions

### Workflow

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow Python PEP 8 style guidelines
   - Add docstrings to functions
   - Update README if needed

3. **Test your changes**
   ```bash
   # Test backend
   uvicorn app.main:app --port 8000
   
   # Test frontend
   cd frontend && python -m http.server 8081
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "Pull Request"
   - Describe your changes

## File Permissions

### Setting Execute Permissions on Scripts

If you add shell scripts, make them executable:
```bash
chmod +x scripts/deploy.sh
```

### File Ownership Issues

If you encounter file ownership issues in deployment:
```bash
# Fix permissions for all files
chmod -R 755 .
# Fix ownership (if needed)
sudo chown -R $USER:$USER .
```

## Deployment Guidelines

### Local Development
```bash
# Backend
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend && python -m http.server 8081
```

### Docker Deployment (Future)
```bash
docker build -t movie-rating-prediction .
docker run -p 8000:8000 movie-rating-prediction
```

## Getting Help

If you encounter issues:
1. Check existing Issues on GitHub
2. Create a new Issue with:
   - Description of the problem
   - Steps to reproduce
   - Error messages
   - Your environment (OS, Python version)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow

Thank you for contributing! 🎬
