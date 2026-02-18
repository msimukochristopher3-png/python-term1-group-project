def word_counter():
    """
    Count words, characters (excluding spaces), and find the longest word
    in a user-provided sentence.
    """
    # --- INPUT ---
    # Get a sentence from the user and remove leading/trailing spaces
    sentence = input("Enter a sentence: ").strip()
    
    # If the user entered nothing (or only spaces), exit gracefully
    if not sentence:
        print("No sentence entered. Exiting.")
        return

    # --- WORD COUNT ---
    # Split the sentence into a list of words using whitespace as delimiter
    words = sentence.split()
    num_words = len(words)

    # --- CHARACTER COUNT (EXCLUDING SPACES) ---
    # Remove all spaces from the sentence, then count the remaining characters
    num_chars = len(sentence.replace(" ", ""))

    # --- LONGEST WORD ---
    # Use max() with key=len to find the word with the greatest length
    # The conditional ensures we don't call max on an empty list (though words is non-empty)
    longest_word = max(words, key=len) if words else ""

    # --- OUTPUT ---
    # Display the three calculated values
    print(f"\nNumber of words: {num_words}")
    print(f"Number of characters (excluding spaces): {num_chars}")
    print(f"Longest word: {longest_word}")
if __name__ == "__main__":
    word_counter()
