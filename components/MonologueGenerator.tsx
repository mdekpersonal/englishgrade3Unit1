import React, { useState, useEffect } from 'react';
import PlayIcon from './icons/PlayIcon';
import PauseIcon from './icons/PauseIcon';
import StopIcon from './icons/StopIcon';

const monologueText = `Hello! My name is Emma. I am ten years old.

This is my family. I have a father, a mother, a brother, and a sister. I love my family!

I have a dog and a cat. I like to play with my ball. I can run and swim. I can sing and draw too!

I have eleven toys, twelve books, and thirteen crayons. I can count to twenty!

Nice to meet you. Bye!`;

const MonologueGenerator: React.FC = () => {
  const [status, setStatus] = useState<'stopped' | 'playing' | 'paused'>('stopped');

  // This handles cleanup when the component unmounts
  useEffect(() => {
    return () => {
      // Ensure any speech is stopped when the user navigates away
      window.speechSynthesis.cancel();
    };
  }, []);

  const handlePlay = () => {
    // Safety check to ensure we're not already speaking
    if (window.speechSynthesis.speaking) {
      return;
    }
    const utterance = new SpeechSynthesisUtterance(monologueText);
    utterance.lang = 'en-US';
    utterance.rate = 0.8; // Slightly slower for better comprehension
    // When the speech finishes naturally, reset the status
    utterance.onend = () => {
      setStatus('stopped');
    };
    
    window.speechSynthesis.speak(utterance);
    setStatus('playing');
  };

  const handlePause = () => {
    if (status === 'playing') {
      window.speechSynthesis.pause();
      setStatus('paused');
    } else if (status === 'paused') {
      window.speechSynthesis.resume();
      setStatus('playing');
    }
  };
  
  const handleStop = () => {
    window.speechSynthesis.cancel();
    setStatus('stopped');
  };

  const isPlaying = status === 'playing';

  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold text-purple-600 mb-2 font-fredoka drop-shadow-sm">Complete Lesson Monologue</h2>
      <p className="text-gray-600 mb-6">Listen to Emma's story and read along! She uses all the vocabulary we've learned today.</p>
      
      <div className="mt-6 p-6 bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl shadow-inner border-2 border-purple-200 text-left">
          <p className="text-gray-800 text-lg whitespace-pre-wrap leading-relaxed font-medium">{monologueText}</p>
      </div>

      <div className="flex justify-center space-x-4 mt-6">
        <button 
          onClick={handlePlay} 
          disabled={status === 'playing' || status === 'paused'}
          className="p-4 bg-green-500 text-white rounded-full shadow-lg hover:bg-green-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-transform transform hover:scale-110"
          aria-label="Play"
        >
          <PlayIcon />
        </button>
        <button 
          onClick={handlePause} 
          disabled={status === 'stopped'}
          className="p-4 bg-yellow-500 text-white rounded-full shadow-lg hover:bg-yellow-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-transform transform hover:scale-110"
          aria-label={isPlaying ? "Pause" : "Resume"}
        >
          { isPlaying ? <PauseIcon /> : <PlayIcon/> }
        </button>
        <button 
          onClick={handleStop} 
          disabled={status === 'stopped'}
          className="p-4 bg-red-500 text-white rounded-full shadow-lg hover:bg-red-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-transform transform hover:scale-110"
          aria-label="Stop"
        >
          <StopIcon />
        </button>
      </div>

    </div>
  );
};

export default MonologueGenerator;
