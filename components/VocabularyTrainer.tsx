import React, { useState, useEffect, useRef, useCallback } from 'react';
import { VocabularyCategory } from '../types';
import WordCarousel from './WordCarousel';
import PlayIcon from './icons/PlayIcon';
import PauseIcon from './icons/PauseIcon';
import StopIcon from './icons/StopIcon';
import SpeakerIcon from './icons/SpeakerIcon';

interface VocabularyTrainerProps {
  category: VocabularyCategory;
}

type Status = 'stopped' | 'playing' | 'paused';

const VocabularyTrainer: React.FC<VocabularyTrainerProps> = ({ category }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [status, setStatus] = useState<Status>('stopped');
  const [useTTSFallback, setUseTTSFallback] = useState(false);
  
  const intervalRef = useRef<number | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  const speak = useCallback((text: string) => {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 0.9; // A bit slower for clarity
      window.speechSynthesis.cancel(); // Stop any previous speech
      window.speechSynthesis.speak(utterance);
    } else {
      console.warn("Browser does not support speech synthesis.");
    }
  }, []);

  // Effect for handling the word carousel interval
  useEffect(() => {
    if (status === 'playing') {
      intervalRef.current = window.setInterval(() => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % category.items.length);
      }, 2000); // Change word every 2 seconds
    } else {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    }
    
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [status, category.items.length]);
  
  // Effect for playing audio using TTS fallback
  useEffect(() => {
    if (status === 'playing' && useTTSFallback) {
      speak(category.items[currentIndex].word);
    }
  }, [currentIndex, status, useTTSFallback, speak, category.items]);

  const handleStop = useCallback(() => {
    setStatus('stopped');
    setCurrentIndex(0);
    window.speechSynthesis.cancel();
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
  }, []);

  const handleStart = () => {
    handleStop(); // Ensure a clean state before starting
    setStatus('playing');

    if (category.audioSrc) {
      setUseTTSFallback(false);
      const audio = new Audio(category.audioSrc);
      audioRef.current = audio;
      
      const handleAudioError = () => {
        console.warn(`Could not play category audio file ${category.audioSrc}. Falling back to TTS.`);
        if (audioRef.current) {
            audioRef.current.removeEventListener('error', handleAudioError);
            audioRef.current.removeEventListener('ended', handleStop);
        }
        setUseTTSFallback(true);
      };
      
      audio.addEventListener('error', handleAudioError);
      audio.addEventListener('ended', handleStop); // Stop when the category audio finishes
      
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.catch(handleAudioError);
      }
    } else {
      setUseTTSFallback(true); // No audio file, use TTS from the start
    }
  };

  const handlePause = () => {
    if (status === 'playing') {
      setStatus('paused');
      window.speechSynthesis.pause();
      if (audioRef.current && !useTTSFallback) {
        audioRef.current.pause();
      }
    } else if (status === 'paused') {
      setStatus('playing');
      window.speechSynthesis.resume();
      if (audioRef.current && !useTTSFallback && !audioRef.current.ended) {
        audioRef.current.play();
      }
    }
  };
  
  const handleRepeatAudio = () => {
    // Always use TTS for repeating a single word for consistency and simplicity
    speak(category.items[currentIndex].word);
  };
  
  // Cleanup effect when component unmounts or category changes
  useEffect(() => {
    return () => {
      handleStop();
    }
  }, [category, handleStop]);
  
  const isPlaying = status === 'playing';

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-3xl font-bold mb-4 text-center text-gray-700 font-fredoka">{category.name}</h2>
      <div className="w-full max-w-md p-4 bg-blue-100 rounded-2xl shadow-inner relative">
         <button 
            onClick={handleRepeatAudio}
            className={`absolute top-4 right-4 text-blue-500 transition-transform transform hover:scale-125 focus:outline-none ${isPlaying ? 'animate-pulse' : ''}`}
            aria-label="Repeat word audio"
          >
          <SpeakerIcon />
         </button>
        <WordCarousel items={category.items} currentIndex={currentIndex} />
      </div>
      <div className="flex space-x-4 mt-6">
        <button 
          onClick={handleStart} 
          disabled={status === 'playing' || status === 'paused'}
          className="p-4 bg-green-500 text-white rounded-full shadow-lg hover:bg-green-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-transform transform hover:scale-110"
          aria-label="Start"
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

export default VocabularyTrainer;
