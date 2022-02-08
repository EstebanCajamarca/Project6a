# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/7/2022
#
# Write a function named find_median that takes as a parameter a list of numbers. The function should return the
# statistical median of those numbers, which will require it to sort the list.

def find_median(some_nums):
    """Finds the median given some values."""
    n = len(some_nums)
    # Assigning value to n variable. n is the number of elements of the list.
    s = sorted(some_nums)
    # s is a sorted version for some_nums list.
    return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None


"""Testing 
some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)"""
