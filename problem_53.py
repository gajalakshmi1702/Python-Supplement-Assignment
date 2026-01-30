# Problem 53: Check if two strings are anagrams
# Find and fix the error

def are_anagrams(str1, str2):
    # Normalize by converting to lowercase and removing spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

word1 = "Listen"
word2 = "Silent"
print(f"Are anagrams: {are_anagrams(word1, word2)}")
