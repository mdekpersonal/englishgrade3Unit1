#!/bin/bash

echo "🚀 English Vocabulary FastHTML App - Deployment Script"
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ and try again."
    exit 1
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Run the application
echo ""
echo "🌟 Starting FastHTML application..."
echo "📚 App will be available at: http://localhost:8000"
echo "🎯 Perfect for Grade 3 students (8 years old)!"
echo ""
echo "Features:"
echo "✅ 5 Vocabulary Categories (Numbers, Family, Nouns, Verbs, Greetings)"
echo "✅ Interactive Audio with Text-to-Speech"
echo "✅ Emma's Story Listening Activity" 
echo "✅ Beautiful, Child-Friendly UI"
echo "✅ Zero Build Issues - Pure Python!"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

python main.py