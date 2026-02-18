def word_counter():
    """
    Count words, characters (excluding spaces), and find the longest word
0    in a user-provided sentence.
    """
    # Get sentence from user; ensure it's not just whitespace
sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("No sentence entered. Exiting.")
    return
# Find the longest word
longest_word = max(words, key=len) if words else ""
