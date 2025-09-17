# Audio Files

This folder is for the MP3 audio files for the English Class Fun Revision app.

The app is now designed to play a single audio file for each vocabulary category. If this file is missing, the app will automatically fall back to using a computer-generated voice for each word individually.

## Required Folder Structure:

Place one `.mp3` file inside a subfolder for each category. The audio file should contain the narration for all words in that category, in order. The file paths must match those defined in the `constants.ts` file.

- `audio/`
  - `numbers/`
    - `numbers.mp3` (contains audio for "ten", "eleven", "twelve"...)
  - `family/`
    - `family.mp3` (contains audio for "mother", "father", "brother"...)
  - `nouns/`
    - `nouns.mp3` (contains audio for "dog", "cat", "bike"...)
  - `verbs/`
    - `verbs.mp3` (contains audio for "play", "sing", "swim"...)
  - `greetings/`
    - `greetings.mp3` (contains audio for "hello", "hi", "bye"...)
