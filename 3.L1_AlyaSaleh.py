# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 01:30:14 2025

@author: Alya Saleh
"""

class Stack:
    # Initializes the stack. If the optional_max_length argument is omitted or 
    # negative, the stack is unbounded. If optional_max_length is non-negative, 
    # the stack is bounded.
    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length

    # Gets the length of the stack
    def __len__(self):
        return len(self.stack_list)

    # Pops and returns the stack's top item.
    # Handle the case where the stack is empty 
    # The code given worked well and because it was not specified what to change in the code 
    # I just implemented the pop(), pop() now checks if the stack is empty before trying to pop.

    def pop(self):
        if len(self.stack_list) == 0:
            print("Error: Stack is empty, cannot pop.")
            return None  # or raise an error if desired
        return self.stack_list.pop()

    # Pushes an item, provided the push doesn't exceed bounds. Does nothing 
    # otherwise. Returns True if the push occurred, False otherwise.
    def push(self, item):
        # If at max length, return false
        if self.max_length >= 0 and len(self.stack_list) == self.max_length:
            return False
        # If unbounded, or bounded and not yet at max length, then push
        self.stack_list.append(item)
        return True

# Make two stacks, one bounded to 4 items and the other bounded
bounded_stack = Stack(4)
unbounded_stack = Stack()

# Push 8 items to each
values_to_push = list(range(1, 9))
print("Pushing values 1 through 8 to each stack")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)

# Pop two items off each stack
print("Popping twice")
for i in range(2):
    bounded_stack.pop()
    unbounded_stack.pop()
    

# Push 4 more items onto each stack
values_to_push = list(range(10, 50, 10))
print(f"Pushing values to each stack: {values_to_push}")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)

# Display contents of each stack
print(f"Bounded stack (max_length={bounded_stack.max_length}) contents:")
while len(bounded_stack) > 0:
    print(f"  {bounded_stack.pop()}")
print("Unbounded stack contents:")
while len(unbounded_stack) > 0:
    print(f"  {unbounded_stack.pop()}")
    
# Try to pop from an empty stack
print("Popping from an empty stack:")
result = bounded_stack.pop()  
print("Pop result when stack is empty:", result)  