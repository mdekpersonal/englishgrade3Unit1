from fasthtml.common import *
import uvicorn
from typing import Dict, List, Optional

# Initialize FastHTML app with beautiful styling matching the original React version
app = FastHTML(
    hdrs=[
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Roboto:wght@400;700&display=swap", rel="stylesheet"),
        Style("""
            /* Reset and Base Styles - Matching Original */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            
            h1, h2, h3, .font-fredoka {
                font-family: 'Fredoka One', cursive;
            }
            
            /* Container and Layout - Exact Match */
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
            }
            
            .text-center { text-align: center; }
            .text-white { color: white; }
            .text-xl { font-size: 1.25rem; }
            .text-2xl { font-size: 1.5rem; }
            .text-3xl { font-size: 1.875rem; }
            .text-4xl { font-size: 2.25rem; }
            .font-bold { font-weight: 700; }
            
            /* Spacing - Exact Match */
            .mb-2 { margin-bottom: 0.5rem; }
            .mb-4 { margin-bottom: 1rem; }
            .mb-6 { margin-bottom: 1.5rem; }
            .mb-8 { margin-bottom: 2rem; }
            .mt-4 { margin-top: 1rem; }
            .mt-8 { margin-top: 2rem; }
            .p-4 { padding: 1rem; }
            .p-6 { padding: 1.5rem; }
            .px-4 { padding-left: 1rem; padding-right: 1rem; }
            .py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
            .py-3 { padding-top: 0.75rem; padding-bottom: 0.75rem; }
            
            /* Background and Colors - Exact Match */
            .bg-white { background-color: white; }
            .bg-blue-500 { background-color: #3b82f6; }
            .bg-blue-600 { background-color: #2563eb; }
            .bg-green-500 { background-color: #10b981; }
            .bg-green-600 { background-color: #059669; }
            .bg-purple-500 { background-color: #8b5cf6; }
            .bg-purple-600 { background-color: #7c3aed; }
            .bg-yellow-400 { background-color: #fbbf24; }
            .bg-yellow-500 { background-color: #f59e0b; }
            .bg-red-500 { background-color: #ef4444; }
            .bg-red-600 { background-color: #dc2626; }
            .bg-gray-100 { background-color: #f3f4f6; }
            .bg-gray-200 { background-color: #e5e7eb; }
            
            /* Border and Rounded - Exact Match */
            .rounded-lg { border-radius: 0.5rem; }
            .rounded-xl { border-radius: 0.75rem; }
            .border { border: 1px solid #d1d5db; }
            
            /* Shadow - Exact Match */
            .shadow-lg { 
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); 
            }
            .shadow-xl { 
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04); 
            }
            
            /* Flex - Exact Match */
            .flex { display: flex; }
            .items-center { align-items: center; }
            .justify-center { justify-content: center; }
            .justify-between { justify-content: space-between; }
            .flex-wrap { flex-wrap: wrap; }
            .gap-2 { gap: 0.5rem; }
            .gap-3 { gap: 0.75rem; }
            .gap-4 { gap: 1rem; }
            
            /* Grid - Exact Match */
            .grid { display: grid; }
            .grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
            .grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
            
            /* Button Styles - Enhanced from Original */
            .btn {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.75rem 1.5rem;
                border: none;
                border-radius: 0.5rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.2s;
                text-decoration: none;
                font-family: 'Roboto', sans-serif;
                font-size: 1rem;
                margin: 0.25rem;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }
            
            .btn:active {
                transform: translateY(0);
            }
            
            .btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
                transform: none;
            }
            
            /* Button Color Classes */
            .btn-blue { background-color: #3b82f6; color: white; }
            .btn-green { background-color: #10b981; color: white; }
            .btn-red { background-color: #ef4444; color: white; }
            .btn-yellow { background-color: #f59e0b; color: white; }
            .btn-purple { background-color: #8b5cf6; color: white; }
            
            /* Hover effects - Exact Match */
            .hover\\:bg-blue-600:hover { background-color: #2563eb; }
            .hover\\:bg-green-600:hover { background-color: #059669; }
            .hover\\:bg-purple-600:hover { background-color: #7c3aed; }
            .hover\\:bg-yellow-500:hover { background-color: #f59e0b; }
            .hover\\:bg-red-600:hover { background-color: #dc2626; }
            
            /* Category Cards - Beautiful Design */
            .category-card {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                border-radius: 0.75rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                border: 3px solid transparent;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }
            
            .category-card:hover {
                transform: translateY(-4px) scale(1.02);
                border-color: #fff;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            }
            
            .category-emoji {
                font-size: 3rem;
                display: block;
                margin-bottom: 1rem;
            }
            
            .category-title {
                font-size: 1.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
                font-family: 'Fredoka One', cursive;
            }
            
            /* Word Display - Matching Original Purple Design */
            .word-display {
                background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
                color: white;
                padding: 2.5rem;
                border-radius: 0.75rem;
                text-align: center;
                margin: 1.5rem 0;
                border: 3px solid #9333ea;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            }
            
            .word-emoji {
                font-size: 4rem;
                display: block;
                margin-bottom: 1rem;
            }
            
            .word-text {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 1rem;
                font-family: 'Fredoka One', cursive;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            /* Audio Controls */
            .audio-controls {
                display: flex;
                gap: 1rem;
                justify-content: center;
                margin: 1.5rem 0;
                flex-wrap: wrap;
            }
            
            /* Navigation */
            .navigation {
                text-align: center;
                margin: 2rem 0;
                padding: 1rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 0.5rem;
                backdrop-filter: blur(10px);
            }
            
            .navigation span {
                margin: 0 1rem;
                font-weight: bold;
                font-size: 1.2rem;
                color: white;
            }
            
            /* Monologue Section */
            .monologue-section {
                margin-top: 3rem;
                padding-top: 2rem;
                border-top: 3px solid rgba(255, 255, 255, 0.2);
            }
            
            .monologue-text {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                padding: 2rem;
                border-radius: 0.75rem;
                margin: 1rem 0;
                border: 3px solid #059669;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
                font-size: 1.1rem;
                line-height: 1.6;
                white-space: pre-line;
            }
            
            /* Header Styling */
            .header {
                text-align: center;
                margin-bottom: 2rem;
                color: white;
            }
            
            .title {
                font-family: 'Fredoka One', cursive;
                font-size: 3rem;
                margin: 1rem 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .subtitle {
                font-size: 1.2rem;
                margin-bottom: 0.5rem;
                font-weight: bold;
            }
            
            /* Card Container */
            .card {
                background: white;
                padding: 2rem;
                border-radius: 0.75rem;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
                margin-bottom: 2rem;
            }
            
            /* Responsive Design */
            @media (min-width: 640px) {
                .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
                .sm\\:text-3xl { font-size: 1.875rem; }
            }
            
            @media (min-width: 768px) {
                .md\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
                .md\\:text-4xl { font-size: 2.25rem; }
            }
            
            @media (max-width: 768px) {
                .title { font-size: 2rem; }
                .container { padding: 1rem; }
                .audio-controls { 
                    flex-direction: column; 
                    align-items: center; 
                }
                .btn { 
                    margin: 0.25rem; 
                    width: 100%;
                    max-width: 250px;
                }
                .word-text { font-size: 2rem; }
                .word-emoji { font-size: 3rem; }
                .grid {
                    grid-template-columns: 1fr;
                }
                .category-card {
                    margin-bottom: 1rem;
                }
            }
            
            /* Utilities */
            .w-full { width: 100%; }
            .h-6 { height: 1.5rem; }
            .w-6 { width: 1.5rem; }
            .min-h-screen { min-height: 100vh; }
            .cursor-pointer { cursor: pointer; }
            .select-none { user-select: none; }
            
            /* Focus styles for accessibility */
            .focus\\:outline-none:focus { outline: none; }
            .focus\\:ring-2:focus { box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.5); }
            
            /* Transform and animations */
            .transform { transform: translateX(var(--tw-translate-x, 0)) translateY(var(--tw-translate-y, 0)) rotate(var(--tw-rotate, 0)) skewX(var(--tw-skew-x, 0)) skewY(var(--tw-skew-y, 0)) scaleX(var(--tw-scale-x, 1)) scaleY(var(--tw-scale-y, 1)); }
            .transition-all { transition: all 0.2s; }
            .duration-200 { transition-duration: 0.2s; }
        """)
    ]
)

# Vocabulary data converted from your constants.ts
VOCABULARY_DATA = {
    'numbers': {
        'name': 'Numbers (10-20)',
        'emoji': '🔢',
        'items': [
            {'word': 'ten', 'emoji': '🔟'},
            {'word': 'eleven', 'emoji': '⭐'},
            {'word': 'twelve', 'emoji': '🕛'},
            {'word': 'thirteen', 'emoji': '🍀'},
            {'word': 'fourteen', 'emoji': '❤️'},
            {'word': 'fifteen', 'emoji': '🏀'},
            {'word': 'sixteen', 'emoji': '🎂'},
            {'word': 'seventeen', 'emoji': '🦋'},
            {'word': 'eighteen', 'emoji': '🐞'},
            {'word': 'nineteen', 'emoji': '☀️'},
            {'word': 'twenty', 'emoji': '🎉'},
        ]
    },
    'family': {
        'name': 'Family',
        'emoji': '👨‍👩‍👧‍👦',
        'items': [
            {'word': 'mother', 'emoji': '👩‍🦰'},
            {'word': 'father', 'emoji': '👨‍🦱'},
            {'word': 'brother', 'emoji': '👦'},
            {'word': 'sister', 'emoji': '👧'},
            {'word': 'grandfather', 'emoji': '👴'},
            {'word': 'grandmother', 'emoji': '👵'},
        ]
    },
    'nouns': {
        'name': 'Nouns',
        'emoji': '🎾',
        'items': [
            {'word': 'dog', 'emoji': '🐶'},
            {'word': 'cat', 'emoji': '🐱'},
            {'word': 'bike', 'emoji': '🚲'},
            {'word': 'computer', 'emoji': '💻'},
            {'word': 'frog', 'emoji': '🐸'},
            {'word': 'hat', 'emoji': '👒'},
            {'word': 'clock', 'emoji': '⏰'},
            {'word': 'lollipop', 'emoji': '🍭'},
            {'word': 'car', 'emoji': '🚗'},
            {'word': 'tambourine', 'emoji': '🪘'},
            {'word': 'piano', 'emoji': '🎹'},
            {'word': 'ball', 'emoji': '⚽'},
        ]
    },
    'verbs': {
        'name': 'Verbs/Abilities',
        'emoji': '🏃',
        'items': [
            {'word': 'play', 'emoji': '🤸'},
            {'word': 'sing', 'emoji': '🎤'},
            {'word': 'swim', 'emoji': '🏊'},
            {'word': 'draw', 'emoji': '🎨'},
            {'word': 'run', 'emoji': '🏃'},
        ]
    },
    'greetings': {
        'name': 'Greetings',
        'emoji': '👋',
        'items': [
            {'word': 'hello', 'emoji': '👋'},
            {'word': 'hi', 'emoji': '😊'},
            {'word': 'bye', 'emoji': '👋'},
            {'word': "what's your name?", 'emoji': '❓'},
            {'word': 'how do you spell?', 'emoji': '🔤'},
            {'word': 'nice to meet you', 'emoji': '🤝'},
        ]
    }
}

# Emma's monologue from your component
MONOLOGUE_TEXT = """Hello! My name is Emma. I am ten years old.

This is my family. I have a father, a mother, a brother, and a sister. I love my family!

I have a dog and a cat. I like to play with my ball. I can run and swim. I can sing and draw too!

I have eleven toys, twelve books, and thirteen crayons. I can count to twenty!

Nice to meet you. Bye!"""

@app.get("/")
def home():
    """Home page with category selection"""
    return Html(
        Head(
            Title("English Class Fun Revision - Grade 3 Vocabulary"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(name="description", content="Interactive English vocabulary learning for Grade 3 students")
        ),
        Body(
            Div(
                Header(
                    H2("EXCELLENCE JUNIOR SCHOOL", cls="subtitle"),
                    H1("English Vocabulary Fun", cls="title"),
                    P("🎯 Perfect for 8-year-old learners!", style="font-size: 1.1rem; margin-bottom: 0.5rem;"),
                    P("Choose a category to start learning!", style="font-size: 1rem;"),
                    cls="header"
                ),
                Main(
                    H3("Choose a Learning Category", style="text-align: center; margin-bottom: 2rem; color: #4f46e5; font-size: 1.8rem;"),
                    Div(
                        *[A(
                            Div(
                                Span(data['emoji'], style="font-size: 3rem; display: block; margin-bottom: 1rem;"),
                                H4(data['name'], cls="category-title"),
                                P(f"{len(data['items'])} words to learn", style="opacity: 0.9;")
                            ),
                            href=f"/category/{category_key}",
                            cls="category-card"
                        ) for category_key, data in VOCABULARY_DATA.items()],
                        cls="grid"
                    ),
                    cls="card"
                ),
                cls="container"
            )
        )
    )

@app.get("/category/{category}")
def vocabulary_trainer(category: str):
    """Vocabulary training page for a specific category"""
    if category not in VOCABULARY_DATA:
        return RedirectResponse("/")
    
    category_data = VOCABULARY_DATA[category]
    words = category_data['items']
    first_word = words[0]
    
    return Html(
        Head(
            Title(f"Learning {category_data['name']} - English Vocabulary"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0")
        ),
        Body(
            Div(
                Header(
                    H2("EXCELLENCE JUNIOR SCHOOL", cls="subtitle"),
                    H1("English Vocabulary Fun", cls="title"),
                    P(f"Learning: {category_data['name']} {category_data['emoji']}", style="font-size: 1.2rem;"),
                    cls="header"
                ),
                Main(
                    Div(
                        A("← Back to Categories", href="/", cls="btn btn-blue"),
                        cls="back-button"
                    ),
                    
                    # Current word display
                    Div(
                        Span(first_word['emoji'], cls="word-emoji"),
                        H2(first_word['word'].title(), id="current-word", cls="word-text"),
                        cls="word-display"
                    ),
                    
                    # Audio controls
                    Div(
                        Button("▶️ Play Word", cls="btn btn-green", onclick=f"speakWord()"),
                        Button("⏸️ Pause", cls="btn btn-yellow", onclick="togglePause()", id="pause-btn"),
                        Button("⏹️ Stop", cls="btn btn-red", onclick="stopSpeech()"),
                        cls="audio-controls"
                    ),
                    
                    # Navigation
                    Div(
                        Button("⬅️ Previous", cls="btn btn-blue", onclick="navigateWord(-1)"),
                        Span(
                            Span("1", id="current-index"),
                            " / ",
                            Span(str(len(words)), id="total-words")
                        ),
                        Button("Next ➡️", cls="btn btn-blue", onclick="navigateWord(1)"),
                        cls="navigation"
                    ),
                    
                    # Monologue Section
                    Div(
                        H3("📖 Listen to Emma's Story", style="text-align: center; margin-bottom: 1.5rem; color: #059669; font-size: 1.8rem;"),
                        P("Emma uses all the vocabulary words in her story!", style="text-align: center; margin-bottom: 1rem; color: #6b7280;"),
                        Div(
                            P(MONOLOGUE_TEXT, style="white-space: pre-line;"),
                            cls="monologue-text"
                        ),
                        Div(
                            Button("▶️ Play Story", cls="btn btn-green", onclick="speakMonologue()"),
                            Button("⏸️ Pause Story", cls="btn btn-yellow", onclick="toggleMonologuePause()", id="monologue-pause-btn"),
                            Button("⏹️ Stop Story", cls="btn btn-red", onclick="stopMonologue()"),
                            cls="audio-controls"
                        ),
                        cls="monologue-section"
                    ),
                    
                    cls="card"
                ),
                cls="container"
            ),
            
            # JavaScript for interactivity
            Script(f"""
                // Global variables
                let currentWordIndex = 0;
                let currentUtterance = null;
                let monologueUtterance = null;
                let isPaused = false;
                let isMonologuePaused = false;
                
                // Vocabulary data for current category
                const vocabularyData = {words};
                const categoryName = '{category_data["name"]}';
                const monologueText = `{MONOLOGUE_TEXT}`;
                
                // Speech synthesis functions
                function speakText(text, rate = 0.8) {{
                    if (currentUtterance) {{
                        speechSynthesis.cancel();
                    }}
                    
                    currentUtterance = new SpeechSynthesisUtterance(text);
                    currentUtterance.rate = rate;
                    currentUtterance.volume = 1;
                    currentUtterance.lang = 'en-US';
                    
                    currentUtterance.onend = function() {{
                        isPaused = false;
                        document.getElementById('pause-btn').textContent = '⏸️ Pause';
                    }};
                    
                    speechSynthesis.speak(currentUtterance);
                    return currentUtterance;
                }}
                
                function speakWord() {{
                    const currentWord = vocabularyData[currentWordIndex];
                    const text = currentWord.word;
                    
                    if (isPaused && speechSynthesis.paused) {{
                        speechSynthesis.resume();
                        isPaused = false;
                        document.getElementById('pause-btn').textContent = '⏸️ Pause';
                        return;
                    }}
                    
                    speakText(text);
                    isPaused = false;
                    document.getElementById('pause-btn').textContent = '⏸️ Pause';
                }}
                
                function togglePause() {{
                    if (speechSynthesis.speaking && !speechSynthesis.paused) {{
                        speechSynthesis.pause();
                        isPaused = true;
                        document.getElementById('pause-btn').textContent = '▶️ Resume';
                    }} else if (speechSynthesis.paused) {{
                        speechSynthesis.resume();
                        isPaused = false;
                        document.getElementById('pause-btn').textContent = '⏸️ Pause';
                    }}
                }}
                
                function stopSpeech() {{
                    speechSynthesis.cancel();
                    isPaused = false;
                    document.getElementById('pause-btn').textContent = '⏸️ Pause';
                }}
                
                // Navigation functions
                function navigateWord(direction) {{
                    currentWordIndex = (currentWordIndex + direction + vocabularyData.length) % vocabularyData.length;
                    updateWordDisplay();
                    stopSpeech();
                }}
                
                function updateWordDisplay() {{
                    const currentWord = vocabularyData[currentWordIndex];
                    document.getElementById('current-word').textContent = currentWord.word.charAt(0).toUpperCase() + currentWord.word.slice(1);
                    document.querySelector('.word-emoji').textContent = currentWord.emoji;
                    document.getElementById('current-index').textContent = currentWordIndex + 1;
                }}
                
                // Monologue functions
                function speakMonologue() {{
                    if (isMonologuePaused && speechSynthesis.paused) {{
                        speechSynthesis.resume();
                        isMonologuePaused = false;
                        document.getElementById('monologue-pause-btn').textContent = '⏸️ Pause Story';
                        return;
                    }}
                    
                    if (monologueUtterance) {{
                        speechSynthesis.cancel();
                    }}
                    
                    monologueUtterance = new SpeechSynthesisUtterance(monologueText);
                    monologueUtterance.rate = 0.8;
                    monologueUtterance.volume = 1;
                    monologueUtterance.lang = 'en-US';
                    
                    monologueUtterance.onend = function() {{
                        isMonologuePaused = false;
                        document.getElementById('monologue-pause-btn').textContent = '⏸️ Pause Story';
                    }};
                    
                    speechSynthesis.speak(monologueUtterance);
                    isMonologuePaused = false;
                    document.getElementById('monologue-pause-btn').textContent = '⏸️ Pause Story';
                }}
                
                function toggleMonologuePause() {{
                    if (speechSynthesis.speaking && !speechSynthesis.paused) {{
                        speechSynthesis.pause();
                        isMonologuePaused = true;
                        document.getElementById('monologue-pause-btn').textContent = '▶️ Resume Story';
                    }} else if (speechSynthesis.paused) {{
                        speechSynthesis.resume();
                        isMonologuePaused = false;
                        document.getElementById('monologue-pause-btn').textContent = '⏸️ Pause Story';
                    }}
                }}
                
                function stopMonologue() {{
                    speechSynthesis.cancel();
                    isMonologuePaused = false;
                    document.getElementById('monologue-pause-btn').textContent = '⏸️ Pause Story';
                }}
                
                // Initialize on page load
                document.addEventListener('DOMContentLoaded', function() {{
                    console.log('English Vocabulary FastHTML App loaded successfully!');
                    console.log('Category:', categoryName);
                    console.log('Words:', vocabularyData.length);
                }});
                
                // Cleanup on page unload
                window.addEventListener('beforeunload', function() {{
                    speechSynthesis.cancel();
                }});
            """)
        )
    )

if __name__ == "__main__":
    print("🚀 Starting English Vocabulary FastHTML App...")
    print("📚 Features:")
    print("  ✅ 5 Vocabulary Categories")
    print("  ✅ Interactive Audio with Text-to-Speech") 
    print("  ✅ Emma's Story Listening Activity")
    print("  ✅ Beautiful, Child-Friendly UI")
    print("  ✅ Zero Build Issues - Pure Python!")
    print("")
    print("🎯 Perfect for Grade 3 students (8 years old)")
    print("📱 Visit: http://localhost:8000")
    print("")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)