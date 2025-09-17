
import React from 'react';
import { VocabularyCategory } from '../types';

interface CategorySelectorProps {
  categories: VocabularyCategory[];
  onSelectCategory: (category: VocabularyCategory) => void;
}

const CategorySelector: React.FC<CategorySelectorProps> = ({ categories, onSelectCategory }) => {
  const colors = [
    'bg-red-400 hover:bg-red-500',
    'bg-orange-400 hover:bg-orange-500',
    'bg-yellow-400 hover:bg-yellow-500',
    'bg-green-400 hover:bg-green-500',
    'bg-blue-400 hover:bg-blue-500',
    'bg-indigo-400 hover:bg-indigo-500',
    'bg-purple-400 hover:bg-purple-500',
    'bg-pink-400 hover:bg-pink-500',
  ];

  return (
    <div>
      <h2 className="text-3xl font-bold text-center mb-6 text-gray-700 font-fredoka">Choose a Topic to Revise!</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {categories.map((category, index) => (
          <button
            key={category.name}
            onClick={() => onSelectCategory(category)}
            className={`p-6 rounded-xl text-white text-2xl font-bold shadow-lg transform transition-transform hover:scale-105 hover:shadow-2xl focus:outline-none focus:ring-4 focus:ring-opacity-75 ${colors[index % colors.length]} font-fredoka`}
          >
            {category.name}
          </button>
        ))}
      </div>
    </div>
  );
};

export default CategorySelector;
