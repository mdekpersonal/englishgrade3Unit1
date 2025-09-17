import React, { useState } from 'react';
import CategorySelector from './components/CategorySelector';
import MonologueGenerator from './components/MonologueGenerator';
import VocabularyTrainer from './components/VocabularyTrainer';
import { VOCABULARY_DATA } from './constants';
import { VocabularyCategory } from './types';

const App: React.FC = () => {
  const [selectedCategory, setSelectedCategory] = useState<VocabularyCategory | null>(null);

  const handleSelectCategory = (category: VocabularyCategory) => {
    setSelectedCategory(category);
  };

  const handleGoBack = () => {
    setSelectedCategory(null);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-4 sm:p-6 md:p-8 font-sans">
      <div className="w-full max-w-4xl mx-auto">
        <header className="text-center mb-8">
          <h2 className="text-2xl sm:text-3xl font-bold text-gray-600 tracking-wider uppercase mb-2">
            EXCELLENCE JUNIOR SCHOOL
          </h2>
          <h1 className="text-4xl sm:text-5xl font-bold text-blue-600 tracking-tight font-fredoka">
            English Vocabulary Fun
          </h1>
          <p className="text-gray-500 mt-2 text-lg">
            Learn new words with fun activities!
          </p>
        </header>

        <main className="bg-white p-6 sm:p-8 rounded-2xl shadow-xl">
          {selectedCategory ? (
            <div>
              <button
                onClick={handleGoBack}
                className="mb-6 bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-lg transition-colors"
              >
                &larr; Back to Topics
              </button>
              <VocabularyTrainer category={selectedCategory} />
            </div>
          ) : (
            <div>
              <CategorySelector categories={VOCABULARY_DATA} onSelectCategory={handleSelectCategory} />
              <hr className="my-8 border-t-2 border-gray-200" />
              <MonologueGenerator />
            </div>
          )}
        </main>

        <footer className="text-center mt-8 text-gray-500">
          <p>&copy; 2025 EXCELLENCE JUNIOR SCHOOL. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
};

export default App;