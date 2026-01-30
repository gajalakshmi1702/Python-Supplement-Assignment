# Problem 51: Reverse words in a sentence
# Find and fix the error

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]   # reverse the list of words
    return " ".join(reversed_words)

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")

