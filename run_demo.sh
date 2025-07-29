#!/bin/bash

echo "========================================"
echo "   SensoryAI - Five Senses Demo"
echo "========================================"
echo ""
echo "Starting SensoryAI Interactive Demo..."
echo ""
echo "If this is your first time running the project,"
echo "make sure you've installed the requirements:"
echo "   pip install -r requirements.txt"
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 interactive_demo.py
elif command -v python &> /dev/null; then
    python interactive_demo.py
else
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.7 or higher"
    exit 1
fi 