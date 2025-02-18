# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:07:05 2025

@author: Alya Saleh
"""


def binary_search(words, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0

    # Variables to hold the low, middle, and high indices
    # of the area being searched. Starts at whole range
    low = 0
    high = len(words) - 1

    # Loop until "low" passes "high"
    while (high >= low):
        # Calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless words[mid] is the key
        comparisons = comparisons + 1
        if (words[mid] < key):
            low = mid + 1
        elif (words[mid] > key):
            high = mid - 1
        else:
            return mid, comparisons
    return -1, comparisons # not found


# Main program to test binary search 
words = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "mango"]
print('WORDS:', words)

# Ask for a string key to search for
key = input('Enter a string key to search for: ').strip()  # Take input as a string
print()

# Test binary search
key_index, comparisons = binary_search(words, key)
if (key_index == -1):
    print('Binary search: "%s" was not found with %d comparisons.' % (key, comparisons))
else:
    print('Binary search: Found "%s" at index %d with %d comparisons.' % (key, key_index, comparisons))
