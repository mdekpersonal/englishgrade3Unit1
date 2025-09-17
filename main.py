from fasthtml.common import *
import uvicorn
from typing import Dict, List, Optional

# Initialize FastHTML app with beautiful styling
app = FastHTML(
    hdrs=[
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Roboto:wght@400;700&display=swap", rel="stylesheet"),
        Style("""
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
            
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 20px; 
            }
            
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
            
            .card { 
                background: white; 
                padding: 2rem; 
                border-radius: 15px; 
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                margin-bottom: 2rem;
            }
            
            .btn { 
                padding: 12px 24px; 
                border: none; 
                border-radius: 8px; 
                cursor: pointer; 
                font-weight: bold;
                transition: all 0.3s ease;
                text-decoration: none;
                display: inline-block;
                margin: 5px;
                font-family: 'Roboto', sans-serif;
                font-size: 1rem;
            }
            
            .btn:hover { 
                transform: translateY(-2px); 
                box-shadow: 0 5px 15px rgba(0,0,0,0.2); 
            }
            
            .btn-blue { background: #3b82f6; color: white; }
            .btn-green { background: #10b981; color: white; }
            .btn-red { background: #ef4444; color: white; }
            .btn-yellow { background: #f59e0b; color: white; }
            .btn-purple { background: #8b5cf6; color: white; }
            
            .btn:active {
                transform: translateY(0);
            }
            
            .grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                gap: 1.5rem; 
            }
            
            .category-card { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                border: 3px solid transparent;
            }
            
            .category-card:hover { 
                transform: scale(1.05); 
                border-color: #fff;
                box-shadow: 0 15px 30px rgba(0,0,0,0.2);
            }
            
            .category-title {
                font-size: 1.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
                font-family: 'Fredoka One', cursive;
            }
            
            .word-display { 
                background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
                color: white;
                padding: 2.5rem;
                border-radius: 15px;
                text-align: center;
                margin: 1.5rem 0;
                border: 3px solid #9333ea;
                box-shadow: 0 10px 25px rgba(168, 85, 247, 0.3);
            }
            
            .word-text {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 1rem;
                font-family: 'Fredoka One', cursive;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .word-emoji {
                font-size: 4rem;
                margin-bottom: 1rem;
                display: block;
            }
            
            .audio-controls { 
                display: flex; 
                gap: 1rem; 
                justify-content: center; 
                margin: 1.5rem 0; 
                flex-wrap: wrap; 
            }
            
            .navigation { 
                text-align: center; 
                margin: 2rem 0;
                padding: 1rem;
                background: #f8fafc;
                border-radius: 10px;
            }
            
            .navigation span { 
                margin: 0 1rem; 
                font-weight: bold; 
                font-size: 1.2rem;
                color: #4f46e5;
            }
            
            .monologue-section { 
                margin-top: 3rem; 
                padding-top: 2rem; 
                border-top: 3px solid #e5e7eb; 
            }
            
            .monologue-text { 
                font-size: 1.2rem; 
                line-height: 1.8; 
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                margin: 1rem 0;
                border: 3px solid #059669;
                box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);
            }
            
            .back-button {
                margin-bottom: 2rem;
            }
            
            @media (max-width: 768px) {
                .title { font-size: 2rem; }
                .container { padding: 10px; }
                .audio-controls { 
                    flex-direction: column; 
                    align-items: center; 
                }
                .btn { 
                    margin: 3px; 
                    width: 100%;
                    max-width: 200px;
                }
                .word-text { font-size: 2rem; }
                .word-emoji { font-size: 3rem; }
                .grid {
                    grid-template-columns: 1fr;
                }
            }
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