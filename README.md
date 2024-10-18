# Madlibs Generator

This is a simple Python program that generates a Madlibs-style story by replacing placeholders in a text file with user-provided input. The placeholders are identified by angle brackets (`<placeholder>`), and the program prompts the user to input words for each placeholder. The modified story is then saved back to the file and printed to the console.

## How It Works

1. **Read the Original Story:**
   - The program reads a text file (`story.txt`) containing a story with placeholders in angle brackets (e.g., `<noun>`, `<verb>`).
   
2. **Identify Placeholders:**
   - It scans through the story and identifies words that start with `<` (i.e., placeholders).
   
3. **Collect User Input:**
   - For each placeholder, the program prompts the user to enter a word.
   
4. **Replace Placeholders:**
   - The program replaces each placeholder in the story with the corresponding user input.
   
5. **Save and Display the Updated Story:**
   - The modified story is saved back into the `story.txt` file, and the updated story is printed to the console.



