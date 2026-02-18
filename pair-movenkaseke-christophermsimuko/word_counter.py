def word_counter():
    """
    Count words, characters (excluding spaces), and find the longest word
    in a user-provided sentence.
    """
   # Get sentence from user; ensure it's not just whitespace
sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("No sentence entered. Exiting.")
    return
# Split sentence into words (by whitespace)
words = sentence.split()
num_words = len(words)

# Count characters excluding spaces
num_chars = len(sentence.replace(" ", ""))
