from fasthtml.common import *
import uvicorn
import os
from typing import Dict, List, Optional

# Initialize FastHTML app with performance-optimized styles
# Use environment variable or default secret key for deployment
secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production-12345678901234567890')

app = FastHTML(
    secret_key=secret_key,
    hdrs=[
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(href="https://fonts.googleapis.com/css2?family=Fredoka+One:wght@400&family=Nunito:wght@400;600;700&display=swap", rel="stylesheet"),
        Style("""
            /* 🚀 Performance-optimized styles for older devices */
            * { 
                margin: 0; 
                padding: 0; 
                box-sizing: border-box; 
            }
            
            /* Reduced animations - only essential ones */
            @media (prefers-reduced-motion: reduce) {
                *, *::before, *::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                }
            }
            
            body { 
                font-family: 'Nunito', Arial, sans-serif; 
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                min-height: 100vh;
                font-size: 16px;
                line-height: 1.5;
                color: #2d3748;
                /* Optimized rendering */
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 15px; 
            }
            
            .header { 
                text-align: center; 
                margin-bottom: 2rem; 
                color: white; 
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }
            
            .title { 
                font-family: 'Fredoka One', cursive; 
                font-size: clamp(1.8rem, 4vw, 3rem);
                margin: 1rem 0; 
                color: #fff;
            }
            
            .subtitle {
                font-size: clamp(1rem, 2.5vw, 1.3rem);
                margin-bottom: 1rem;
                font-weight: 600;
                color: rgba(255,255,255,0.95);
            }
            
            .card { 
                background: white; 
                padding: 1.5rem; 
                border-radius: 20px; 
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                margin-bottom: 1rem;
            }
            
            /* Simple, performance-friendly buttons */
            .btn { 
                padding: 12px 20px; 
                border: none; 
                border-radius: 12px; 
                cursor: pointer; 
                font-weight: 600;
                font-size: 16px;
                text-decoration: none;
                display: inline-block;
                margin: 5px;
                font-family: 'Nunito', sans-serif;
                /* Simple transition - very lightweight */
                transition: all 0.2s ease;
                /* Prevent text selection for better mobile experience */
                user-select: none;
                -webkit-tap-highlight-color: transparent;
                min-height: 48px;
                text-align: center;
            }
            
            .btn:hover, .btn:focus { 
                filter: brightness(1.1);
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            
            .btn:active {
                transform: translateY(0);
            }
            
            /* Color schemes - solid colors for better performance */
            .btn-blue { background: #3b82f6; color: white; }
            .btn-green { background: #10b981; color: white; }
            .btn-red { background: #ef4444; color: white; }
            .btn-yellow { background: #f59e0b; color: white; }
            .btn-purple { background: #8b5cf6; color: white; }
            .btn-pink { background: #ec4899; color: white; }
            .btn-orange { background: #f97316; color: white; }
            
            /* Grid layout with better mobile support */
            .grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                gap: 1rem; 
                margin: 1rem 0;
            }
            
            .category-card { 
                background: white;
                color: #2d3748;
                padding: 1.5rem;
                border-radius: 16px;
                text-align: center;
                cursor: pointer;
                text-decoration: none;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                border: 3px solid transparent;
                /* Simple hover effect */
                transition: all 0.2s ease;
            }
            
            .category-card:hover { 
                border-color: #4facfe;
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            }
            
            .category-emoji {
                font-size: 3rem;
                margin-bottom: 0.5rem;
                display: block;
            }
            
            .category-title {
                font-size: 1.3rem;
                margin-bottom: 0.5rem;
                color: #2d3748;
                font-weight: 700;
            }
            
            .category-description {
                color: #718096;
                font-size: 0.95rem;
            }
            
            /* Word display with solid background for better readability */
            .word-display { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                border-radius: 16px;
                text-align: center;
                margin: 1rem 0;
                box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
            }
            
            .word-emoji {
                font-size: 4rem;
                margin-bottom: 1rem;
                display: block;
            }
            
            .word-text {
                font-size: clamp(2rem, 5vw, 3rem);
                font-weight: 700;
                margin-bottom: 1rem;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
                font-family: 'Fredoka One', cursive;
            }
            
            /* Carousel - streaming content */
            .carousel-container {
                position: relative;
                overflow: hidden;
                border-radius: 16px;
                margin: 1rem 0;
                background: white;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            }
            
            .carousel-track {
                display: flex;
                transition: transform 0.3s ease;
                width: 100%;
            }
            
            .carousel-slide {
                min-width: 100%;
                padding: 2rem;
                text-align: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .carousel-controls {
                position: absolute;
                bottom: 15px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 8px;
            }
            
            .carousel-dot {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: rgba(255,255,255,0.5);
                cursor: pointer;
                transition: background 0.2s ease;
            }
            
            .carousel-dot.active {
                background: white;
            }
            
            .carousel-nav {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                background: rgba(255,255,255,0.9);
                border: none;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                cursor: pointer;
                font-size: 18px;
                transition: all 0.2s ease;
                z-index: 10;
            }
            
            .carousel-nav:hover {
                background: white;
                transform: translateY(-50%) scale(1.1);
            }
            
            .carousel-nav.prev {
                left: 10px;
            }
            
            .carousel-nav.next {
                right: 10px;
            }
            
            /* Audio controls - enhanced */
            .audio-controls { 
                display: flex; 
                gap: 0.8rem; 
                justify-content: center; 
                margin: 1.5rem 0;
                flex-wrap: wrap;
            }
            
            .audio-player {
                background: rgba(255,255,255,0.95);
                padding: 1rem;
                border-radius: 12px;
                margin: 1rem 0;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }
            
            .audio-progress {
                width: 100%;
                height: 6px;
                background: #e2e8f0;
                border-radius: 3px;
                margin: 10px 0;
                overflow: hidden;
            }
            
            .audio-progress-bar {
                height: 100%;
                background: linear-gradient(90deg, #4facfe, #00f2fe);
                width: 0%;
                transition: width 0.1s ease;
            }
            
            .navigation { 
                text-align: center; 
                margin: 1.5rem 0;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
            }
            
            .word-counter {
                background: #f7fafc;
                padding: 8px 16px;
                border-radius: 20px;
                font-weight: 600;
                color: #2d3748;
                border: 2px solid #e2e8f0;
            }
            
            /* Monologue section */
            .monologue-section { 
                margin-top: 2rem; 
                padding-top: 2rem; 
                border-top: 3px solid #e2e8f0;
            }
            
            .story-title {
                text-align: center;
                margin-bottom: 1rem;
                color: #2d3748;
                font-size: 1.5rem;
                font-weight: 700;
            }
            
            .monologue-text { 
                font-size: clamp(1rem, 2.5vw, 1.2rem);
                line-height: 1.7;
                background: linear-gradient(135deg, #00b894 0%, #55efc4 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                white-space: pre-line;
                text-shadow: 0 1px 2px rgba(0,0,0,0.1);
            }
            
            .back-button {
                margin-bottom: 1rem;
            }
            
            /* Mobile optimizations */
            @media (max-width: 768px) {
                .container { padding: 10px; }
                .card { padding: 1rem; }
                .btn { 
                    padding: 14px 18px;
                    font-size: 16px;
                    min-height: 48px; /* Better touch targets */
                    width: 100%;
                    max-width: 280px;
                }
                .audio-controls { 
                    flex-direction: column; 
                    align-items: center; 
                }
                .navigation {
                    flex-direction: column;
                    gap: 0.5rem;
                }
                .grid {
                    grid-template-columns: 1fr;
                    gap: 0.8rem;
                }
                .word-text { font-size: 2.5rem; }
                .word-emoji { font-size: 3rem; }
            }
            
            /* Focus styles for accessibility */
            .btn:focus, .category-card:focus {
                outline: 3px solid #ffd700;
                outline-offset: 2px;
            }
            
            /* Loading state - simple and lightweight */
            .loading {
                opacity: 0.7;
                pointer-events: none;
            }
            
            /* High contrast mode support */
            @media (prefers-contrast: high) {
                .btn { border: 2px solid currentColor; }
                .card { border: 2px solid #333; }
            }
        """)
    ]
)

# 🌟 VOCABULARY DATA - Optimized for Performance
vocabulary_data = {
    "numbers": {
        "title": "Numbers 10-20",
        "emoji": "🔢",
        "description": "Count like a champion!",
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
        "description": "Meet your family!",
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
        "description": "Things around us!",
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
        "description": "Action words!",
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
        "description": "Be polite!",
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

# 📚 EMMA'S SIMPLE STORY - Easy for Grade 3
emma_monologue = """Hi! I'm Emma! 

I am ten years old. 
I love my family! 
I have a mother, father, sister, and brother. 

We have pets! 
A dog and a cat! 
They are so cute!

I can count: ten, eleven, twelve, thirteen! 
I like to play and read books! 
I can run and jump! 

Thank you for learning with me! 
You are amazing! 

Bye bye! """

# Routes for the Optimized App! 🚀
@app.get("/")
def home():
    """🏠 Welcome to Optimized Vocabulary Land!"""
    category_cards = []
    
    for key, category in vocabulary_data.items():
        card = A(
            Span(category["emoji"], cls="category-emoji"),
            H4(category["title"], cls="category-title"),
            P(category["description"], cls="category-description"),
            href=f"/category/{key}",
            cls="category-card"
        )
        category_cards.append(card)
    
    return Div(
        # 🎪 Header
        Div(
            H1("🌟 VOCABULARY FUN 🌟", cls="title"),
            H2("Grade 3 English Adventure!", cls="subtitle"),
            P("Learn new words with fun activities! 🎉", style="font-size: 1.1rem; color: rgba(255,255,255,0.9);"),
            cls="header"
        ),
        
        # 🌟 Category Grid
        Div(
            H3("🎯 Choose Your Adventure!", style="text-align: center; margin-bottom: 1.5rem; color: #2d3748; font-size: 1.5rem;"),
            Div(
                *category_cards,
                cls="grid"
            ),
            cls="card"
        ),
        
        # 📚 Special Story Section
        Div(
            H3("📖 Emma's Special Message", cls="story-title"),
            A(
                "🎭 Read Emma's Story! 📚",
                href="/monologue",
                cls="btn btn-purple"
            ),
            cls="monologue-section card"
        ),
        
        cls="container"
    )

@app.get("/category/{category_name}")
def category_view(category_name: str, word_index: int = 0):
    """🎨 Carousel-Enhanced Category Viewer"""
    if category_name not in vocabulary_data:
        return Div(
            H1("🚫 Oops! Category not found!", cls="title"),
            A("🏠 Go Home", href="/", cls="btn btn-blue"),
            cls="container"
        )
    
    category = vocabulary_data[category_name]
    words = category["words"]
    
    # Create carousel slides for all words
    carousel_slides = []
    for i, word in enumerate(words):
        slide = Div(
            Span(word["emoji"], cls="word-emoji"),
            H2(word["word"].upper(), cls="word-text"),
            P(f"Word {i + 1} of {len(words)}", style="opacity: 0.8; font-size: 1rem;"),
            cls="carousel-slide",
            id=f"slide-{i}"
        )
        carousel_slides.append(slide)
    
    # Create carousel dots
    carousel_dots = []
    for i in range(len(words)):
        dot = Span(
            cls="carousel-dot" + (" active" if i == word_index else ""),
            onclick=f"goToSlide({i})",
            id=f"dot-{i}"
        )
        carousel_dots.append(dot)
    
    return Div(
        # 🔙 Back button
        A("🏠 Back to Categories", href="/", cls="btn btn-blue back-button"),
        
        # 🎪 Category Header
        Div(
            H1(f"{category['emoji']} {category['title']}", cls="title"),
            H2(category["description"], cls="subtitle"),
            cls="header"
        ),
        
        # 🎠 Word Carousel
        Div(
            Div(
                *carousel_slides,
                cls="carousel-track",
                id="carousel-track",
                style=f"transform: translateX(-{word_index * 100}%)"
            ),
            Button("‹", cls="carousel-nav prev", onclick="previousSlide()"),
            Button("›", cls="carousel-nav next", onclick="nextSlide()"),
            Div(
                *carousel_dots,
                cls="carousel-controls"
            ),
            cls="carousel-container"
        ),
        
        # 🎵 Simple Audio Player
        Div(
            H3("🎵 Listen to Words", style="text-align: center; margin-bottom: 1rem; color: #2d3748;"),
            Div(
                Button(
                    "▶️ START",
                    onclick="startAudio()",
                    cls="btn btn-green",
                    id="start-btn"
                ),
                Button(
                    "⏸️ PAUSE",
                    onclick="pauseAudio()",
                    cls="btn btn-yellow",
                    id="pause-btn"
                ),
                Button(
                    "⏹️ STOP",
                    onclick="stopAudio()",
                    cls="btn btn-red",
                    id="stop-btn"
                ),
                cls="audio-controls"
            ),
            Div(
                Div(cls="audio-progress-bar", id="progress-bar"),
                cls="audio-progress"
            ),
            P("Press START to hear the word!", 
              style="text-align: center; color: #718096; font-size: 0.9rem;"),
            cls="audio-player"
        ),
        
        # 🎮 Auto-play Controls
        Div(
            H3("🎮 Auto-Play Mode", style="text-align: center; margin-bottom: 1rem; color: #2d3748;"),
            Div(
                Button(
                    "▶️ Start Auto-Play",
                    onclick="startAutoPlay()",
                    cls="btn btn-green",
                    id="autoplay-btn"
                ),
                Button(
                    "⏸️ Pause",
                    onclick="pauseAutoPlay()",
                    cls="btn btn-yellow"
                ),
                Button(
                    "⏹️ Stop Auto-Play",
                    onclick="stopAutoPlay()",
                    cls="btn btn-red"
                ),
                cls="audio-controls"
            ),
            P("Auto-play will say each word and move to the next!", 
              style="text-align: center; color: #718096; font-size: 0.9rem;"),
            cls="card"
        ),
        
        # 📚 Quick Word Navigation
        Div(
            H3("📚 Quick Jump to Word:", style="text-align: center; margin-bottom: 1rem; color: #2d3748;"),
            Div(
                *[Button(
                    f"{word['emoji']} {word['word'].title()}",
                    onclick=f"goToSlide({i})",
                    cls="btn btn-blue" if i != word_index else "btn btn-green",
                    id=f"word-btn-{i}"
                ) for i, word in enumerate(words)],
                cls="audio-controls"
            ),
            cls="card"
        ),
        
        # 🎭 Enhanced JavaScript with Simple Audio Controls
        Script(f"""
            // 🎠 CAROUSEL & SIMPLIFIED AUDIO SYSTEM
            let currentSlide = {word_index};
            let autoPlayInterval = null;
            let isAutoPlaying = false;
            let currentUtterance = null;
            let progressInterval = null;
            let isPlaying = false;
            let isPaused = false;
            
            const words = {[word["word"] for word in words]};
            const totalSlides = {len(words)};
            
            // 🎠 Carousel Functions
            function goToSlide(index) {{
                currentSlide = index;
                updateCarousel();
                updateUI();
                stopAudio(); // Stop any current speech
            }}
            
            function nextSlide() {{
                currentSlide = (currentSlide + 1) % totalSlides;
                updateCarousel();
                updateUI();
            }}
            
            function previousSlide() {{
                currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
                updateCarousel();
                updateUI();
            }}
            
            function updateCarousel() {{
                const track = document.getElementById('carousel-track');
                track.style.transform = `translateX(-${{currentSlide * 100}}%)`;
                
                // Update dots
                document.querySelectorAll('.carousel-dot').forEach((dot, index) => {{
                    dot.classList.toggle('active', index === currentSlide);
                }});
                
                // Update word buttons
                document.querySelectorAll('[id^="word-btn-"]').forEach((btn, index) => {{
                    btn.className = index === currentSlide ? 'btn btn-green' : 'btn btn-blue';
                }});
            }}
            
            // 🔊 Simplified Audio Functions
            function startAudio() {{
                if (isPaused) {{
                    resumeAudio();
                    return;
                }}
                
                const word = words[currentSlide];
                speakText(word, 0.8);
                isPlaying = true;
                isPaused = false;
                updateButtonStates();
            }}
            
            function pauseAudio() {{
                if (speechSynthesis.speaking && !speechSynthesis.paused) {{
                    speechSynthesis.pause();
                    isPaused = true;
                    isPlaying = false;
                    stopProgressBar();
                    updateButtonStates();
                }}
            }}
            
            function resumeAudio() {{
                if (speechSynthesis.paused) {{
                    speechSynthesis.resume();
                    isPaused = false;
                    isPlaying = true;
                    startProgressBar();
                    updateButtonStates();
                }}
            }}
            
            function stopAudio() {{
                if (speechSynthesis.speaking || speechSynthesis.paused) {{
                    speechSynthesis.cancel();
                }}
                isPlaying = false;
                isPaused = false;
                stopProgressBar();
                updateButtonStates();
            }}
            
            function speakText(text, rate = 0.8) {{
                stopAudio();
                currentUtterance = new SpeechSynthesisUtterance(text);
                currentUtterance.rate = rate;
                currentUtterance.pitch = 1.1;
                currentUtterance.volume = 1.0;
                
                // Progress bar animation
                startProgressBar();
                
                currentUtterance.onend = function() {{
                    isPlaying = false;
                    isPaused = false;
                    stopProgressBar();
                    updateButtonStates();
                }};
                
                speechSynthesis.speak(currentUtterance);
                isPlaying = true;
                updateButtonStates();
            }}
            
            function updateButtonStates() {{
                const startBtn = document.getElementById('start-btn');
                const pauseBtn = document.getElementById('pause-btn');
                const stopBtn = document.getElementById('stop-btn');
                
                if (isPlaying) {{
                    startBtn.textContent = '🔄 PLAYING...';
                    startBtn.disabled = true;
                    pauseBtn.disabled = false;
                    stopBtn.disabled = false;
                }} else if (isPaused) {{
                    startBtn.textContent = '▶️ RESUME';
                    startBtn.disabled = false;
                    pauseBtn.disabled = true;
                    stopBtn.disabled = false;
                }} else {{
                    startBtn.textContent = '▶️ START';
                    startBtn.disabled = false;
                    pauseBtn.disabled = true;
                    stopBtn.disabled = true;
                }}
            }}
            
            // 📊 Progress Bar
            function startProgressBar() {{
                const progressBar = document.getElementById('progress-bar');
                let width = 0;
                progressInterval = setInterval(() => {{
                    if (width >= 100) {{
                        stopProgressBar();
                    }} else {{
                        width += 2;
                        progressBar.style.width = width + '%';
                    }}
                }}, 50);
            }}
            
            function stopProgressBar() {{
                if (progressInterval) {{
                    clearInterval(progressInterval);
                    progressInterval = null;
                }}
                document.getElementById('progress-bar').style.width = '0%';
            }}
            
            // 🎮 Auto-Play Functions (simplified)
            function startAutoPlay() {{
                if (isAutoPlaying) return;
                
                isAutoPlaying = true;
                document.getElementById('autoplay-btn').textContent = '🔄 Auto-Playing...';
                document.getElementById('autoplay-btn').disabled = true;
                
                playCurrentAndNext();
            }}
            
            function playCurrentAndNext() {{
                if (!isAutoPlaying) return;
                
                startAudio();
                
                // Wait for speech to finish, then move to next
                setTimeout(() => {{
                    if (isAutoPlaying) {{
                        nextSlide();
                        // Continue with next word after a short pause
                        setTimeout(() => {{
                            if (isAutoPlaying) {{
                                playCurrentAndNext();
                            }}
                        }}, 1000);
                    }}
                }}, 2500); // Adjust timing based on word length
            }}
            
            function pauseAutoPlay() {{
                isAutoPlaying = false;
                stopAudio();
                document.getElementById('autoplay-btn').textContent = '▶️ Start Auto-Play';
                document.getElementById('autoplay-btn').disabled = false;
            }}
            
            function stopAutoPlay() {{
                pauseAutoPlay();
                currentSlide = 0;
                updateCarousel();
                updateUI();
            }}
            
            function updateUI() {{
                updateButtonStates();
            }}
            
            // 🎹 Keyboard Navigation
            document.addEventListener('keydown', function(e) {{
                switch(e.key) {{
                    case 'ArrowLeft':
                        previousSlide();
                        break;
                    case 'ArrowRight':
                        nextSlide();
                        break;
                    case ' ': // Spacebar
                        e.preventDefault();
                        if (isPlaying) {{
                            pauseAudio();
                        }} else {{
                            startAudio();
                        }}
                        break;
                    case 'Enter':
                        startAudio();
                        break;
                    case 'Escape':
                        stopAudio();
                        break;
                }}
            }});
            
            // 📱 Touch/Swipe Support
            let startX = 0;
            const carousel = document.getElementById('carousel-track');
            
            carousel.addEventListener('touchstart', function(e) {{
                startX = e.touches[0].clientX;
            }});
            
            carousel.addEventListener('touchend', function(e) {{
                const endX = e.changedTouches[0].clientX;
                const diff = startX - endX;
                
                if (Math.abs(diff) > 50) {{ // Minimum swipe distance
                    if (diff > 0) {{
                        nextSlide();
                    }} else {{
                        previousSlide();
                    }}
                }}
            }});
            
            // Initialize
            updateCarousel();
            updateButtonStates();
        """),
        
        cls="container"
    )

@app.get("/monologue")
def monologue_view():
    """📚 Emma's Optimized Story!"""
    return Div(
        # 🔙 Back button
        A("🏠 Back to Home", href="/", cls="btn btn-blue back-button"),
        
        # 🎪 Story Header
        Div(
            H1("📚 Emma's Story 📚", cls="title"),
            H2("A Special Message Just for You! ✨", cls="subtitle"),
            cls="header"
        ),
        
        # 📖 Story Content with Audio Placeholder
        Div(
            # Audio Status Placeholder
            Div(
                Span("🔊", id="story-audio-icon", style="font-size: 2rem; margin-right: 10px;"),
                Span("Ready to read Emma's story!", id="story-status", style="font-size: 1.1rem; font-weight: 600; color: #4a5568;"),
                style="text-align: center; padding: 15px; background: rgba(116, 185, 255, 0.1); border-radius: 10px; margin-bottom: 15px; border: 2px dashed #74b9ff;"
            ),
            Div(
                emma_monologue,
                cls="monologue-text"
            ),
            
            # 🎵 Story Audio Controls
            Div(
                Button(
                    "▶️ START STORY",
                    onclick="startStory()",
                    cls="btn btn-green",
                    id="story-start-btn"
                ),
                Button(
                    "⏸️ PAUSE STORY",
                    onclick="pauseStory()",
                    cls="btn btn-yellow",
                    id="story-pause-btn"
                ),
                Button(
                    "⏹️ STOP STORY",
                    onclick="stopStory()",
                    cls="btn btn-red",
                    id="story-stop-btn"
                ),
                cls="audio-controls"
            ),
            
            # Progress indicator for story
            Div(
                Div(cls="audio-progress-bar", id="story-progress-bar"),
                cls="audio-progress"
            ),
            
            cls="card"
        ),
        
        # 🎭 JavaScript for Story Audio - With Placeholder Updates
        Script(f"""
            let storyUtterance = null;
            let isStoryPlaying = false;
            let isStoryPaused = false;
            let storyProgressInterval = null;
            
            function updateStoryStatus(message, icon = "🔊") {{
                document.getElementById('story-status').textContent = message;
                document.getElementById('story-audio-icon').textContent = icon;
            }}
            
            function startStory() {{
                if (isStoryPaused) {{
                    resumeStory();
                    return;
                }}
                
                stopStory(); // Stop any current story
                updateStoryStatus("Loading story...", "⏳");
                
                const text = `{emma_monologue.replace('`', "'")}`;
                storyUtterance = new SpeechSynthesisUtterance(text);
                storyUtterance.rate = 0.8;
                storyUtterance.pitch = 1.1;
                storyUtterance.volume = 1.0;
                
                storyUtterance.onstart = function() {{
                    updateStoryStatus("Now reading Emma's story!", "📖");
                    startStoryProgressBar();
                }};
                
                storyUtterance.onend = function() {{
                    isStoryPlaying = false;
                    isStoryPaused = false;
                    updateStoryStatus("Story finished! Great job listening!", "⭐");
                    stopStoryProgressBar();
                    updateStoryButtonStates();
                }};
                
                speechSynthesis.speak(storyUtterance);
                isStoryPlaying = true;
                isStoryPaused = false;
                updateStoryButtonStates();
            }}
            
            function pauseStory() {{
                if (speechSynthesis.speaking && !speechSynthesis.paused) {{
                    speechSynthesis.pause();
                    isStoryPlaying = false;
                    isStoryPaused = true;
                    updateStoryStatus("Story paused. Press START to continue!", "⏸️");
                    stopStoryProgressBar();
                    updateStoryButtonStates();
                }}
            }}
            
            function resumeStory() {{
                if (speechSynthesis.paused) {{
                    speechSynthesis.resume();
                    isStoryPlaying = true;
                    isStoryPaused = false;
                    updateStoryStatus("Continuing Emma's story!", "📖");
                    startStoryProgressBar();
                    updateStoryButtonStates();
                }}
            }}
            
            function stopStory() {{
                if (speechSynthesis.speaking || speechSynthesis.paused) {{
                    speechSynthesis.cancel();
                }}
                isStoryPlaying = false;
                isStoryPaused = false;
                updateStoryStatus("Ready to read Emma's story!", "🔊");
                stopStoryProgressBar();
                updateStoryButtonStates();
            }}
            
            function startStoryProgressBar() {{
                const progressBar = document.getElementById('story-progress-bar');
                let width = 0;
                storyProgressInterval = setInterval(() => {{
                    if (width >= 100) {{
                        stopStoryProgressBar();
                    }} else {{
                        width += 1;
                        progressBar.style.width = width + '%';
                    }}
                }}, 100);
            }}
            
            function stopStoryProgressBar() {{
                if (storyProgressInterval) {{
                    clearInterval(storyProgressInterval);
                    storyProgressInterval = null;
                }}
                document.getElementById('story-progress-bar').style.width = '0%';
            }}
            
            function updateStoryButtonStates() {{
                const startBtn = document.getElementById('story-start-btn');
                const pauseBtn = document.getElementById('story-pause-btn');
                const stopBtn = document.getElementById('story-stop-btn');
                
                if (isStoryPlaying) {{
                    startBtn.textContent = '🔄 READING...';
                    startBtn.disabled = true;
                    pauseBtn.disabled = false;
                    stopBtn.disabled = false;
                }} else if (isStoryPaused) {{
                    startBtn.textContent = '▶️ RESUME STORY';
                    startBtn.disabled = false;
                    pauseBtn.disabled = true;
                    stopBtn.disabled = false;
                }} else {{
                    startBtn.textContent = '▶️ START STORY';
                    startBtn.disabled = false;
                    pauseBtn.disabled = true;
                    stopBtn.disabled = true;
                }}
            }}
            
            // Initialize story buttons and status
            updateStoryButtonStates();
            updateStoryStatus("Ready to read Emma's story!", "🔊");
        """),
        
        cls="container"
    )

# 🚀 Launch the Optimized App!
if __name__ == "__main__":
    print("🚀 Starting OPTIMIZED Vocabulary App...")
    print("📱 Performance-optimized for older devices and slow connections!")
    print("🎨 Access at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)