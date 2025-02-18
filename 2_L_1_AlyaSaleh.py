# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:31:34 2025

@author: Alya Saleh
"""

def linear_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons # not found
 
def binary_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0

    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts at whole range
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # Calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        comparisons = comparisons + 1
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid, comparisons
  
    return -1, comparisons # not found


# Main program to test both search functions 
numbers = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "mango"]
print('NUMBERS:', numbers)
     
key = input('Enter an integer key to search for: ').strip()
print()
 
# Test linear search
key_index, comparisons = linear_search(numbers, key)      
if (key_index == -1):
    print('Linear search: %s was not found with %d comparisons.' % (key, comparisons))
else:
    print('Linear search: Found %s at index %d with %d comparisons.' % (key, key_index, comparisons))
 
# Test binary search
key_index, comparisons = binary_search(numbers, key)
if (key_index == -1):
    print('Binary search: %s was not found with %d comparisons.' % (key, comparisons))
else:
    print('Binary search: Found %s at index %d with %d comparisons.' % (key, key_index, comparisons))

