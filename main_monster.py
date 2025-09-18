from fasthtml.common import (
    FastHTML, Link, Style, Html, Head, Title, Meta, Body,
    Div, Header, Main, A, Span, P, H1, H2, H3, H4, Button, Script, RedirectResponse
)
import uvicorn
import os
from typing import Dict, List, Optional

# Initialize FastHTML app with MONSTER UI - Kid-Friendly Design!
# Use environment variable or default secret key for deployment
secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production-12345678901234567890')

app = FastHTML(
    secret_key=secret_key,
    key_fname=None,  # Disable file-based key storage for deployment
    hdrs=[
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(href="https://fonts.googleapis.com/css2?family=Fredoka+One:wght@400&family=Nunito:wght@400;600;700;800&display=swap", rel="stylesheet"),
        Style("""
            /* 🎨 MONSTER UI - Kid-Friendly Design! */
            * { 
                margin: 0; 
                padding: 0; 
                box-sizing: border-box; 
            }
            
            body { 
                font-family: 'Nunito', sans-serif; 
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
                background-size: 400% 400%;
                animation: gradientShift 8s ease infinite;
                min-height: 100vh;
                color: #2d3436;
                overflow-x: hidden;
            }
            
            /* 🌈 Magical Animations */
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-15px); }
                60% { transform: translateY(-8px); }
            }
            
            @keyframes wiggle {
                0%, 100% { transform: rotate(0deg) scale(1); }
                25% { transform: rotate(5deg) scale(1.02); }
                75% { transform: rotate(-5deg) scale(1.02); }
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.08); }
                100% { transform: scale(1); }
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-25px) rotate(2deg); }
            }
            
            @keyframes sparkle {
                0%, 100% { opacity: 0.7; transform: scale(0.8); }
                50% { opacity: 1; transform: scale(1.2); }
            }
            
            @keyframes slideInLeft {
                from { transform: translateX(-100px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            
            @keyframes slideInRight {
                from { transform: translateX(100px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            
            /* 🏠 Container */
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 20px; 
                animation: slideInLeft 0.8s ease-out;
            }
            
            /* 🎪 Header - Super Fun! */
            .header { 
                text-align: center; 
                margin-bottom: 3rem; 
                color: white;
                position: relative;
            }
            
            .header::before {
                content: '⭐✨🌟';
                position: absolute;
                top: -20px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 2rem;
                animation: sparkle 2s infinite;
            }
            
            .title { 
                font-family: 'Fredoka One', cursive; 
                font-size: 4rem; 
                margin: 1.5rem 0; 
                text-shadow: 4px 4px 8px rgba(0,0,0,0.3);
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #feca57);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: pulse 3s infinite;
                letter-spacing: 2px;
            }
            
            .subtitle {
                font-size: 1.8rem;
                margin-bottom: 1rem;
                font-weight: 800;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
                animation: bounce 2s infinite;
            }
            
            .fun-text {
                font-size: 1.4rem;
                font-weight: 600;
                margin: 0.5rem 0;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            }
            
            /* 🎨 Monster Cards */
            .card { 
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 2.5rem; 
                border-radius: 25px; 
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
                margin-bottom: 2rem;
                border: 5px solid transparent;
                background-clip: padding-box;
                position: relative;
                overflow: hidden;
                animation: slideInRight 1s ease-out;
            }
            
            .card::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
                border-radius: 25px;
                z-index: -1;
                animation: gradientShift 4s ease infinite;
            }
            
            /* 🚀 Super Buttons */
            .btn { 
                padding: 15px 30px; 
                border: none; 
                border-radius: 20px; 
                cursor: pointer; 
                font-weight: 700;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                text-decoration: none;
                display: inline-block;
                margin: 8px;
                font-family: 'Nunito', sans-serif;
                font-size: 1.1rem;
                position: relative;
                overflow: hidden;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            }
            
            .btn::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
                transition: left 0.5s;
            }
            
            .btn:hover::before {
                left: 100%;
            }
            
            .btn:hover { 
                transform: translateY(-5px) scale(1.05); 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                animation: wiggle 0.5s ease-in-out;
            }
            
            .btn:active {
                transform: translateY(-2px) scale(1.02);
            }
            
            /* 🎨 Monster Button Colors */
            .btn-blue { 
                background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); 
                color: white; 
                border: 3px solid #74b9ff;
            }
            .btn-green { 
                background: linear-gradient(135deg, #55efc4 0%, #00b894 100%); 
                color: white; 
                border: 3px solid #55efc4;
            }
            .btn-red { 
                background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%); 
                color: white; 
                border: 3px solid #fd79a8;
            }
            .btn-yellow { 
                background: linear-gradient(135deg, #fdcb6e 0%, #e17055 100%); 
                color: white; 
                border: 3px solid #fdcb6e;
            }
            .btn-purple { 
                background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%); 
                color: white; 
                border: 3px solid #a29bfe;
            }
            .btn-orange { 
                background: linear-gradient(135deg, #ff7675 0%, #d63031 100%); 
                color: white; 
                border: 3px solid #ff7675;
            }
            
            /* 🌟 Category Cards - Monster Style */
            .grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
                gap: 2rem; 
            }
            
            .category-card { 
                background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%);
                color: white;
                padding: 2.5rem;
                border-radius: 25px;
                text-align: center;
                cursor: pointer;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                text-decoration: none;
                border: 5px solid rgba(255,255,255,0.3);
                position: relative;
                overflow: hidden;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                animation: float 4s ease-in-out infinite;
            }
            
            .category-card::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
                transition: all 0.3s;
                transform: scale(0);
            }
            
            .category-card:hover::before {
                transform: scale(1);
            }
            
            .category-card:hover { 
                transform: translateY(-15px) scale(1.05) rotate(2deg); 
                border-color: #fff;
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
                animation-play-state: paused;
            }
            
            .category-card:nth-child(1) { animation-delay: 0s; }
            .category-card:nth-child(2) { animation-delay: 0.5s; }
            .category-card:nth-child(3) { animation-delay: 1s; }
            .category-card:nth-child(4) { animation-delay: 1.5s; }
            .category-card:nth-child(5) { animation-delay: 2s; }
            
            .category-title {
                font-size: 2rem;
                font-weight: 800;
                margin-bottom: 1rem;
                font-family: 'Fredoka One', cursive;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                letter-spacing: 1px;
            }
            
            .category-emoji {
                font-size: 4rem;
                display: block;
                margin-bottom: 1rem;
                animation: bounce 2s infinite;
            }
            
            .category-description {
                font-size: 1.2rem;
                font-weight: 600;
                opacity: 0.9;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            }
            
            /* 🦄 Word Display - Magical! */
            .word-display { 
                background: linear-gradient(135deg, #a29bfe 0%, #fd79a8 50%, #fdcb6e 100%);
                color: white;
                padding: 3rem;
                border-radius: 25px;
                text-align: center;
                margin: 2rem 0;
                border: 5px solid rgba(255,255,255,0.4);
                box-shadow: 0 20px 40px rgba(162, 155, 254, 0.4);
                position: relative;
                overflow: hidden;
                animation: pulse 3s infinite;
            }
            
            .word-display::before {
                content: '✨';
                position: absolute;
                top: 10px;
                right: 15px;
                font-size: 2rem;
                animation: sparkle 1.5s infinite;
            }
            
            .word-display::after {
                content: '🌟';
                position: absolute;
                bottom: 10px;
                left: 15px;
                font-size: 2rem;
                animation: sparkle 1.5s infinite 0.5s;
            }
            
            .word-text {
                font-size: 4rem;
                font-weight: 800;
                margin-bottom: 1rem;
                font-family: 'Fredoka One', cursive;
                text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
                letter-spacing: 2px;
            }
            
            .word-emoji {
                font-size: 5rem;
                margin-bottom: 1.5rem;
                display: block;
                animation: wiggle 2s infinite;
            }
            
            /* 🎵 Audio Controls - Fun Style */
            .audio-controls { 
                display: flex; 
                gap: 1.5rem; 
                justify-content: center; 
                margin: 2rem 0; 
                flex-wrap: wrap; 
            }
            
            /* 🧭 Navigation - Kid-Friendly */
            .navigation { 
                text-align: center; 
                margin: 3rem 0;
                padding: 2rem;
                background: rgba(255,255,255,0.9);
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                border: 3px solid rgba(116, 185, 255, 0.3);
            }
            
            .navigation span { 
                margin: 0 1.5rem; 
                font-weight: 800; 
                font-size: 1.5rem;
                color: #6c5ce7;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            }
            
            /* 📖 Monologue Section - Story Time! */
            .monologue-section { 
                margin-top: 4rem; 
                padding-top: 3rem; 
                border-top: 5px dashed rgba(255,255,255,0.6);
                position: relative;
            }
            
            .monologue-section::before {
                content: '📚✨📖';
                position: absolute;
                top: -15px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 2rem;
                background: rgba(255,255,255,0.9);
                padding: 0 1rem;
                border-radius: 15px;
            }
            
            .story-title {
                text-align: center;
                margin-bottom: 2rem;
                color: #2d3436;
                font-size: 2.2rem;
                font-weight: 800;
                font-family: 'Fredoka One', cursive;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }
            
            .monologue-text { 
                font-size: 1.4rem; 
                line-height: 2; 
                background: linear-gradient(135deg, #00b894 0%, #55efc4 100%);
                color: white;
                padding: 2.5rem;
                border-radius: 20px;
                margin: 2rem 0;
                border: 4px solid rgba(255,255,255,0.3);
                box-shadow: 0 15px 35px rgba(0, 184, 148, 0.3);
                white-space: pre-line;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
                position: relative;
            }
            
            .monologue-text::before {
                content: '👧';
                position: absolute;
                top: 15px;
                right: 20px;
                font-size: 2.5rem;
                animation: wiggle 3s infinite;
            }
            
            .back-button {
                margin-bottom: 2rem;
                animation: slideInLeft 0.8s ease-out;
            }
            
            /* 📱 Responsive Design */
            @media (max-width: 768px) {
                .title { font-size: 2.5rem; }
                .container { padding: 15px; }
                .audio-controls { 
                    flex-direction: column; 
                    align-items: center; 
                }
                .btn { 
                    margin: 5px; 
                    width: 100%;
                    max-width: 250px;
                    font-size: 1rem;
                }
                .word-text { font-size: 2.5rem; }
                .word-emoji { font-size: 3.5rem; }
                .grid {
                    grid-template-columns: 1fr;
                    gap: 1.5rem;
                }
                .category-card {
                    padding: 2rem;
                }
                .category-title {
                    font-size: 1.8rem;
                }
                .navigation span {
                    font-size: 1.3rem;
                    margin: 0 1rem;
                }
            }
            
            /* 🎪 Special Effects */
            .fun-shadow {
                box-shadow: 0 25px 50px rgba(0,0,0,0.15), 0 0 30px rgba(116, 185, 255, 0.3);
            }
            
            .glow {
                filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.5));
            }
            
            /* 🌈 Loading Animation */
            .loading {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid rgba(255,255,255,.3);
                border-radius: 50%;
                border-top-color: #fff;
                animation: spin 1s ease-in-out infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            /* 🎨 Hover Feedback */
            .interactive:hover {
                cursor: pointer;
                transform: scale(1.02);
                transition: all 0.2s ease;
            }
            
            /* 🔥 Success Feedback */
            .success-flash {
                animation: successFlash 0.6s ease-in-out;
            }
            
            @keyframes successFlash {
                0%, 100% { background-color: transparent; }
                50% { background-color: rgba(0, 184, 148, 0.3); }
            }
        """)
    ]
)

# 🌟 MAGICAL VOCABULARY DATA - Monster Fun!
vocabulary_data = {
    "numbers": {
        "title": "Numbers 10-20",
        "emoji": "🔢",
        "description": "Count like a monster!",
        "words": [
            {"word": "ten", "emoji": "🔟"},
            {"word": "eleven", "emoji": "1️⃣1️⃣"},
            {"word": "twelve", "emoji": "1️⃣2️⃣"},
            {"word": "thirteen", "emoji": "1️⃣3️⃣"},
            {"word": "fourteen", "emoji": "1️⃣4️⃣"},
            {"word": "fifteen", "emoji": "1️⃣5️⃣"},
            {"word": "sixteen", "emoji": "1️⃣6️⃣"},
            {"word": "seventeen", "emoji": "1️⃣7️⃣"},
            {"word": "eighteen", "emoji": "1️⃣8️⃣"},
            {"word": "nineteen", "emoji": "1️⃣9️⃣"},
            {"word": "twenty", "emoji": "2️⃣0️⃣"}
        ]
    },
    "family": {
        "title": "Family Members",
        "emoji": "👨‍👩‍👧‍👦",
        "description": "Meet the monster family!",
        "words": [
            {"word": "mother", "emoji": "👩"},
            {"word": "father", "emoji": "👨"},
            {"word": "sister", "emoji": "👧"},
            {"word": "brother", "emoji": "👦"},
            {"word": "grandmother", "emoji": "👵"},
            {"word": "grandfather", "emoji": "👴"},
            {"word": "baby", "emoji": "👶"},
            {"word": "aunt", "emoji": "👩‍🦰"},
            {"word": "uncle", "emoji": "👨‍🦲"},
            {"word": "cousin", "emoji": "👫"}
        ]
    },
    "nouns": {
        "title": "Common Nouns",
        "emoji": "🎈",
        "description": "Awesome monster things!",
        "words": [
            {"word": "book", "emoji": "📚"},
            {"word": "cat", "emoji": "🐱"},
            {"word": "dog", "emoji": "🐶"},
            {"word": "house", "emoji": "🏠"},
            {"word": "car", "emoji": "🚗"},
            {"word": "tree", "emoji": "🌳"},
            {"word": "sun", "emoji": "☀️"},
            {"word": "moon", "emoji": "🌙"},
            {"word": "star", "emoji": "⭐"},
            {"word": "flower", "emoji": "🌸"},
            {"word": "apple", "emoji": "🍎"},
            {"word": "water", "emoji": "💧"}
        ]
    },
    "verbs": {
        "title": "Verbs & Abilities",
        "emoji": "🏃‍♂️",
        "description": "Monster action words!",
        "words": [
            {"word": "run", "emoji": "🏃‍♂️"},
            {"word": "jump", "emoji": "🦘"},
            {"word": "sing", "emoji": "🎤"},
            {"word": "dance", "emoji": "💃"},
            {"word": "read", "emoji": "📖"},
            {"word": "write", "emoji": "✏️"},
            {"word": "play", "emoji": "🎮"},
            {"word": "eat", "emoji": "🍴"},
            {"word": "sleep", "emoji": "😴"},
            {"word": "swim", "emoji": "🏊‍♀️"},
            {"word": "fly", "emoji": "🕊️"},
            {"word": "laugh", "emoji": "😂"}
        ]
    },
    "greetings": {
        "title": "Greetings & Manners",
        "emoji": "👋",
        "description": "Monster politeness!",
        "words": [
            {"word": "hello", "emoji": "👋"},
            {"word": "goodbye", "emoji": "👋"},
            {"word": "please", "emoji": "🙏"},
            {"word": "thank you", "emoji": "😊"},
            {"word": "sorry", "emoji": "😔"},
            {"word": "excuse me", "emoji": "🤚"},
            {"word": "good morning", "emoji": "🌅"},
            {"word": "good night", "emoji": "🌙"},
            {"word": "nice to meet you", "emoji": "🤝"},
            {"word": "how are you", "emoji": "❓"}
        ]
    }
}

# 📚 EMMA'S MAGICAL MONOLOGUE - Special Story!
emma_monologue = """Hi! I'm Emma! 🌟

Welcome to our MONSTER vocabulary adventure! Today we learned so many awesome words together! 

I love learning with you because every word is like a magical treasure! ✨

When we count from ten to twenty, it's like counting monster cookies! 🍪
My family is full of love - mother, father, sister, and brother! 👨‍👩‍👧‍👦
We see amazing things like books, cats, dogs, and beautiful flowers! 📚🐱🐶🌸
We can do incredible things like run, jump, sing, and dance! 🏃‍♂️🦘🎤💃
And we're always polite with hello, please, and thank you! 👋🙏😊

Remember: Every word you learn makes you stronger and smarter! 
You're doing AMAZING! Keep being curious and keep learning! 

I'm so proud of you! Let's continue our vocabulary adventure together! 🚀✨

Love,
Emma 💝"""

# Routes for the Monster UI App! 🚀
@app.get("/")
def home():
    """🏠 Welcome to Monster Vocabulary Land!"""
    category_cards = []
    
    for key, category in vocabulary_data.items():
        card = A(
            Span(category["emoji"], cls="category-emoji"),
            H3(category["title"], cls="category-title"),
            P(category["description"], cls="category-description"),
            href=f"/category/{key}",
            cls="category-card"
        )
        category_cards.append(card)
    
    return Div(
        # 🎪 Super Fun Header
        Div(
            H3("EXCELLENCE JUNIOR SCHOOL", style="text-align: center; color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-bottom: 0.5rem; font-weight: 600; letter-spacing: 1px;"),
            H1("🦄 MONSTER VOCABULARY 🦄", cls="title"),
            H2("Grade 3 English Adventure!", cls="subtitle"),
            H3("UNIT 1", style="text-align: center; color: #FFD700; font-size: 1.4rem; margin-top: 0.5rem; margin-bottom: 1rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);"),
            P("Welcome to the most FUN way to learn English! 🌟", cls="fun-text"),
            P("Click on any category below to start your magical journey! ✨", cls="fun-text"),
            cls="header"
        ),
        
        # 🌟 Category Grid
        Div(
            *category_cards,
            cls="grid"
        ),
        
        # 📚 Special Story Section
        Div(
            H2("📖 Emma's Special Message", cls="story-title"),
            A(
                "🎭 Read Emma's Story! 📚",
                href="/monologue",
                cls="btn btn-purple"
            ),
            cls="monologue-section"
        ),
        
        cls="container"
    )

@app.get("/category/{category_name}")
def category_view(category_name: str, word_index: int = 0):
    """🎨 Monster Category Viewer with Super Fun Words!"""
    if category_name not in vocabulary_data:
        return Div(
            H1("🚫 Oops! Category not found!", cls="title"),
            A("🏠 Go Home", href="/", cls="btn btn-blue"),
            cls="container"
        )
    
    category = vocabulary_data[category_name]
    words = category["words"]
    current_word = words[word_index]
    
    # 🧭 Navigation buttons
    prev_index = (word_index - 1) % len(words)
    next_index = (word_index + 1) % len(words)
    
    return Div(
        # 🔙 Back button
        A("🏠 Back to Categories", href="/", cls="btn btn-blue back-button"),
        
        # 🎪 Category Header
        Div(
            H1(f"{category['emoji']} {category['title']} {category['emoji']}", cls="title"),
            H2(category["description"], cls="subtitle"),
            cls="header"
        ),
        
        # 🦄 Current Word Display
        Div(
            Span(current_word["emoji"], cls="word-emoji"),
            H2(current_word["word"].upper(), cls="word-text"),
            cls="word-display"
        ),
        
        # 🎵 Audio Controls
        Div(
            Button(
                "🔊 Say Word",
                onclick=f"speak('{current_word['word']}')",
                cls="btn btn-green"
            ),
            Button(
                "📢 Spell It",
                onclick=f"spell('{current_word['word']}')",
                cls="btn btn-yellow"
            ),
            Button(
                "🎵 Say Slow",
                onclick=f"speakSlow('{current_word['word']}')",
                cls="btn btn-purple"
            ),
            Button(
                "🔇 Stop",
                onclick="stopSpeaking()",
                cls="btn btn-red"
            ),
            cls="audio-controls"
        ),
        
        # 🧭 Navigation
        Div(
            A("⬅️ Previous", href=f"/category/{category_name}?word_index={prev_index}", cls="btn btn-orange"),
            Span(f"Word {word_index + 1} of {len(words)}", cls="navigation-text"),
            A("Next ➡️", href=f"/category/{category_name}?word_index={next_index}", cls="btn btn-orange"),
            cls="navigation"
        ),
        
        # 📚 All Words in Category
        Div(
            H3("🌟 All Words in This Category:", cls="story-title"),
            Div(
                *[A(
                    f"{word['emoji']} {word['word'].title()}",
                    href=f"/category/{category_name}?word_index={i}",
                    cls="btn btn-blue" if i != word_index else "btn btn-green"
                ) for i, word in enumerate(words)],
                cls="audio-controls"
            ),
            cls="card"
        ),
        
        # 🎭 JavaScript for Speech
        Script("""
            // 🎵 MONSTER SPEECH FUNCTIONS!
            function speak(word) {
                const utterance = new SpeechSynthesisUtterance(word);
                utterance.rate = 0.8;
                utterance.pitch = 1.2;
                speechSynthesis.speak(utterance);
            }
            
            function spell(word) {
                const letters = word.split('').join(', ');
                const utterance = new SpeechSynthesisUtterance(letters);
                utterance.rate = 0.6;
                utterance.pitch = 1.1;
                speechSynthesis.speak(utterance);
            }
            
            function speakSlow(word) {
                const utterance = new SpeechSynthesisUtterance(word);
                utterance.rate = 0.4;
                utterance.pitch = 1.3;
                speechSynthesis.speak(utterance);
            }
            
            function stopSpeaking() {
                speechSynthesis.cancel();
            }
        """),
        
        cls="container"
    )

@app.get("/monologue")
def monologue_view():
    """📚 Emma's Special Magical Story!"""
    return Div(
        # 🔙 Back button
        A("🏠 Back to Home", href="/", cls="btn btn-blue back-button"),
        
        # 🎪 Story Header
        Div(
            H1("📚 Emma's Magical Story 📚", cls="title"),
            H2("A Special Message Just for You! ✨", cls="subtitle"),
            cls="header"
        ),
        
        # 📖 Story Content
        Div(
            Div(
                emma_monologue,
                cls="monologue-text"
            ),
            
            # 🎵 Audio Controls for Story
            Div(
                Button(
                    "🎭 Read Story Aloud",
                    onclick="speakMonologue()",
                    cls="btn btn-green"
                ),
                Button(
                    "🔇 Stop Reading",
                    onclick="stopSpeaking()",
                    cls="btn btn-red"
                ),
                cls="audio-controls"
            ),
            
            cls="card"
        ),
        
        # 🎭 JavaScript for Story Speech
        Script(f"""
            function speakMonologue() {{
                const text = `{emma_monologue.replace('`', "'")}`;
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.rate = 0.7;
                utterance.pitch = 1.1;
                speechSynthesis.speak(utterance);
            }}
            
            function stopSpeaking() {{
                speechSynthesis.cancel();
            }}
        """),
        
        cls="container"
    )

# 🚀 Launch the Monster App!
if __name__ == "__main__":
    print("🦄 Starting Monster Vocabulary App...")
    print("🌟 Kid-friendly design with amazing animations!")
    print("🎨 Access at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)