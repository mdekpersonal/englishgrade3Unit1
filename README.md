# English Class Fun Revision 🎓

A beautiful, interactive English vocabulary learning application designed specifically for Grade 3 students (8 years old). Built with **FastHTML** - **ZERO build issues, ZERO PostCSS conflicts!**

![FastHTML Version](https://img.shields.io/badge/FastHTML-v0.12.27-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Perfect for 8-Year-Old Learners!

### 📚 Features

- ✅ **5 Vocabulary Categories**: Numbers (10-20), Family, Nouns, Verbs/Abilities, Greetings
- ✅ **Interactive Audio**: Text-to-Speech with Play, Pause, Stop controls
- ✅ **Emma's Story**: Complete listening activity using all vocabulary words
- ✅ **Beautiful UI**: Child-friendly design with vibrant colors and emojis
- ✅ **Responsive Design**: Works perfectly on tablets, phones, and computers
- ✅ **Zero Build Issues**: Pure Python - no Node.js, PostCSS, or TailwindCSS conflicts!
- ✅ **Performance Optimized**: Reduced animations for older devices and slow connections

## 🚀 Quick Start

### Option 1: Simple Python Setup
```bash
# 1. Install dependencies
pip install python-fasthtml uvicorn

# 2. Run the app
python main_optimized.py

# 3. Open browser
# Visit: http://localhost:8000
```

### Option 2: Virtual Environment (Recommended)
```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python main_optimized.py
```

### Option 3: Using Docker
```bash
# Build the image
docker build -t english-vocab-app .

# Run the container
docker run -p 8000:8000 english-vocab-app
```

### Option 4: Using the Run Script
```bash
# Make script executable and run
chmod +x run.sh
./run.sh
```

## 🎮 How to Use

1. **Choose a Category**: Select from Numbers, Family, Nouns, Verbs, or Greetings
2. **Learn Words**: Each category has 8-11 words with beautiful emojis
3. **Listen & Learn**: Click buttons to hear pronunciation:
   - 🔊 **Say Word**: Hear the word spoken
   - 📢 **Spell It**: Hear each letter individually
   - 🎵 **Say Slow**: Slower pronunciation for learning
   - 🔇 **Stop**: Stop any playing audio
4. **Navigate**: Use Previous/Next buttons or click word links
5. **Emma's Story**: Listen to a complete story using all vocabulary words

## 🏗️ Project Structure

```
english-class-fun-revision/
├── main_optimized.py      # 🚀 Production-ready FastHTML app (recommended)
├── main_monster.py        # 🎨 Monster UI version with animations
├── main.py               # 📚 Original FastHTML version
├── requirements.txt      # 📦 Python dependencies
├── run.sh               # 🚀 Deployment script
├── Dockerfile          # 🐳 Docker configuration
├── README.md           # 📖 This file
├── README_FASTHTML.md  # 📚 Detailed FastHTML documentation
├── audio/              # 🔊 Audio assets directory
└── .venv/              # 🐍 Python virtual environment
```

## 🛠️ Development

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/english-class-fun-revision.git
cd english-class-fun-revision

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the optimized version
python main_optimized.py
```

## 🎨 Customization

The app is built with FastHTML and can be easily customized:

- **Colors**: Modify CSS in the `Style()` sections
- **Vocabulary**: Edit the `vocabulary_data` dictionary
- **Audio**: Adjust speech synthesis settings in JavaScript
- **UI**: Change fonts, layouts, and animations

## 📱 Browser Support

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastHTML](https://fasthtml.dev/) - Modern web apps in pure Python
- Fonts from [Google Fonts](https://fonts.google.com/)
- Icons and emojis from Unicode standard
- Designed for Grade 3 students worldwide

---

**Made with ❤️ for young learners!** 🌟
