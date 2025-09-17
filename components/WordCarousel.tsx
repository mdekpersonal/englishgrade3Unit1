import React from 'react';
import { VocabularyItem } from '../types';

interface WordCarouselProps {
  items: VocabularyItem[];
  currentIndex: number;
}

const WordCarousel: React.FC<WordCarouselProps> = ({ items, currentIndex }) => {
  return (
    <div className="w-full h-64 overflow-hidden relative">
      <div
        className="flex transition-transform duration-500 ease-in-out h-full"
        style={{ transform: `translateX(-${currentIndex * 100}%)` }}
      >
        {items.map((item) => (
          <div key={item.word} className="w-full flex-shrink-0 h-full flex flex-col items-center justify-center p-4">
            <div className="text-8xl mb-4" role="img" aria-label={item.word}>
              {item.emoji}
            </div>
            <p className="text-3xl font-bold text-gray-800 capitalize font-fredoka">{item.word}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WordCarousel;
