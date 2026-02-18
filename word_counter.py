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
