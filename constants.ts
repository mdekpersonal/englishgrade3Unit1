import { VocabularyCategory } from './types';

export const VOCABULARY_DATA: VocabularyCategory[] = [
  {
    name: 'Numbers (10-20)',
    audioSrc: '/audio/numbers/numbers.mp3',
    items: [
      { word: 'ten', emoji: '🔟' },
      { word: 'eleven', emoji: '⭐' },
      { word: 'twelve', emoji: '🕛' },
      { word: 'thirteen', emoji: '🍀' },
      { word: 'fourteen', emoji: '❤️' },
      { word: 'fifteen', emoji: '🏀' },
      { word: 'sixteen', emoji: '🎂' },
      { word: 'seventeen', emoji: '🦋' },
      { word: 'eighteen', emoji: '🐞' },
      { word: 'nineteen', emoji: '☀️' },
      { word: 'twenty', emoji: '🎉' },
    ],
  },
  {
    name: 'Family',
    audioSrc: '/audio/family/family.mp3',
    items: [
      { word: 'mother', emoji: '👩‍🦰' },
      { word: 'father', emoji: '👨‍🦱' },
      { word: 'brother', emoji: '👦' },
      { word: 'sister', emoji: '👧' },
      { word: 'grandfather', emoji: '👴' },
      { word: 'grandmother', emoji: '👵' },
    ],
  },
  {
    name: 'Nouns',
    audioSrc: '/audio/nouns/nouns.mp3',
    items: [
      { word: 'dog', emoji: '🐶' },
      { word: 'cat', emoji: '🐱' },
      { word: 'bike', emoji: '🚲' },
      { word: 'computer', emoji: '💻' },
      { word: 'frog', emoji: '🐸' },
      { word: 'hat', emoji: '👒' },
      { word: 'clock', emoji: '⏰' },
      { word: 'lollipop', emoji: '🍭' },
      { word: 'car', emoji: '🚗' },
      { word: 'tambourine', emoji: '🪘' },
      { word: 'piano', emoji: '🎹' },
      { word: 'ball', emoji: '⚽' },
    ],
  },
   {
    name: 'Verbs/Abilities',
    audioSrc: '/audio/verbs/verbs.mp3',
    items: [
      { word: 'play', emoji: '🤸' },
      { word: 'sing', emoji: '🎤' },
      { word: 'swim', emoji: '🏊' },
      { word: 'draw', emoji: '🎨' },
      { word: 'run', emoji: '🏃' },
    ],
  },
   {
    name: 'Greetings',
    audioSrc: '/audio/greetings/greetings.mp3',
    items: [
      { word: 'hello', emoji: '👋' },
      { word: 'hi', emoji: '😊' },
      { word: 'bye', emoji: '👋' },
      { word: "what's your name?", emoji: '❓' },
      { word: 'how do you spell?', emoji: '🔤' },
      { word: 'nice to meet you', emoji: '🤝' },
    ],
  }
];
