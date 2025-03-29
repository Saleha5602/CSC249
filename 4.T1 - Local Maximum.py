# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:11:21 2025

@author: Alya Saleh
"""
"in the video you showed us different examples how to find the global max ,I don't think we have to do all of them, am I right?"
def find_global_max(arr):
    if not arr:
        return None  # Handle empty list case
    
    current_max = arr[0]  # Initialize with the first element

    for num in arr:
        if num > current_max:
            current_max = num

    return current_max

# Example usage:
arr = [0,1, 4, 7, 5, 3, 4]
print("Global max:", find_global_max(arr))
