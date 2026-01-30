# Problem 77: Check if number is perfect square
# Find and fix the error

import math

def is_perfect_square(n):
    if n < 0:  # negative numbers can't be perfect squares
        return False
    root = math.isqrt(n)  # integer square root
    return root * root == n

print(f"Is 16 perfect square? {is_perfect_square(16)}")
print(f"Is 15 perfect square? {is_perfect_square(15)}")

