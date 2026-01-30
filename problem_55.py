# Problem 55: Count frequency of each element
# Find and fix the error

from collections import Counter

def count_frequency(lst):
    return dict(Counter(lst))

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Frequency: {count_frequency(numbers)}")
