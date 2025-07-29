#!/bin/bash

echo "========================================"
echo "   SensoryAI - Streamlit Web App"
echo "========================================"
echo ""
echo "Starting SensoryAI Web Interface..."
echo ""
echo "The web app will open in your browser at:"
echo "   http://localhost:8501"
echo ""
echo "If this is your first time running the project,"
echo "make sure you've installed the requirements:"
echo "   pip install -r requirements.txt"
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 -m streamlit run streamlit_app.py
elif command -v python &> /dev/null; then
    python -m streamlit run streamlit_app.py
else
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.7 or higher"
    exit 1
fi 