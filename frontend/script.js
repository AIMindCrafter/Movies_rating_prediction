// API endpoint configuration
const API_URL = 'http://localhost:8000';

// Element references
const reviewText = document.getElementById('reviewText');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultDiv = document.getElementById('result');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');
const sentimentLabel = document.getElementById('sentimentLabel');
const confidenceScore = document.getElementById('confidenceScore');

/**
 * Analyze sentiment of the review
 */
async function analyzeSentiment() {
    const text = reviewText.value.trim();
    
    // Validate input
    if (!text) {
        showError('Please enter a movie review to analyze.');
        return;
    }

    // Hide previous results and errors
    hideAll();
    
    // Show loading state
    loadingDiv.classList.remove('hidden');
    analyzeBtn.disabled = true;

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Display result
        displayResult(data.sentiment, data.confidence);
        
    } catch (error) {
        console.error('Error:', error);
        showError('Failed to analyze sentiment. Make sure the backend server is running at ' + API_URL);
    } finally {
        loadingDiv.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
}

/**
 * Display the analysis result
 */
function displayResult(sentiment, confidence) {
    sentimentLabel.textContent = sentiment;
    sentimentLabel.className = 'sentiment-label ' + sentiment.toLowerCase();
    
    confidenceScore.textContent = `Confidence: ${(confidence * 100).toFixed(1)}%`;
    
    resultDiv.classList.remove('hidden');
}

/**
 * Show error message
 */
function showError(message) {
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

/**
 * Hide all result sections
 */
function hideAll() {
    resultDiv.classList.add('hidden');
    errorDiv.classList.add('hidden');
    loadingDiv.classList.add('hidden');
}

// Allow Enter key to submit (with Ctrl/Cmd modifier)
reviewText.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
        e.preventDefault();
        analyzeSentiment();
    }
});
