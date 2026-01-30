# Problem 37: Check if year is leap year
# Find and fix the error

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(f"Is 1900 a leap year? {is_leap_year(1900)}")
print(f"Is 2000 a leap year? {is_leap_year(2000)}")
print(f"Is 2024 a leap year? {is_leap_year(2024)}")
