export interface VocabularyItem {
  word: string;
  emoji: string;
}

export interface VocabularyCategory {
  name: string;
  items: VocabularyItem[];
  audioSrc?: string;
}
