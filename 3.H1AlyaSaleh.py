# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 02:06:32 2025

@author: Alya Saleh
"""

class ArrayQueue:
    def __init__(self, maximum_length=-1):
        self.queue_list = [0]
        self.front_index = 0
        self.length = 0
        self.max_length = maximum_length
    
    def get_length(self):
        return self.length
    
    def get_max_length(self):
        return self.max_length
    
    def enqueue(self, item):
        # If at max length, return False
        if self.length == self.max_length:
            return False
        
        # Resize if length equals allocation size
        if self.length == len(self.queue_list):
            self.resize()
        
        # Enqueue the item
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True
    
    # EXPERIMENTAL:
    # Implementation of enqueue that never requires a resize
    def enqueue_noresize(self, item):
        # If at max length, return False
        if self.length == self.max_length:
            return False
        
        if self.length < len(self.queue_list):
            # Space already exists in the list
            item_index = (self.front_index + self.length) % len(self.queue_list)
            self.queue_list[item_index] = item
        else:
            if self.front_index > 0:
                # Reorganize the list so that front_index is 0
                self.queue_list = self.queue_list[self.front_index:] + self.queue_list[0:self.front_index]
                self.front_index = 0
            # Append the item
            self.queue_list.append(item)
        # All cases above enqueue the item, so length must be incremented
        self.length += 1
        return True
    
    def dequeue(self):
        # Get the item at the front of the queue
        to_return = self.queue_list[self.front_index]
        
        # Decrement length and advance frontIndex
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)
        
        # Return the front item
        return to_return
    
    def resize(self):
        # Create new list and copy existing items
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = max_length
        new_list = [0] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]
        
        # Assign new list and reset front_index to 0
        self.queue_list = new_list
        self.front_index = 0


# Make two queues, one bounded to 4 items and the other bounded
boundedQueue = ArrayQueue(4)
unboundedQueue = ArrayQueue()
        
# Enqueue 8 items in each
print("Enqueueing values 1 through 8 to each queue")
for i in range(1, 9):
    boundedQueue.enqueue(i)
    unboundedQueue.enqueue(i)
       
# Dequeue two items from each queue
print("Dequeuing twice")
for i in range(2):
    print(f"  Dequeued {boundedQueue.dequeue()}", end="")
    print(" from bounded queue");
    print(f"  Dequeued {unboundedQueue.dequeue()}", end="")
    print(" from unbounded queue")

# Enqueue 4 more items
print("Enqueueing values: 10, 20, 30 and 40")
for i in [10, 20, 30, 40]:
    boundedQueue.enqueue(i)
    unboundedQueue.enqueue(i)
        
# Display contents of each queue
print("Bounded queue (maxLength=", end="")
print(f"{boundedQueue.get_max_length()}", end="")
print(") contents:")
while boundedQueue.get_length() > 0:
    print(f"  {boundedQueue.dequeue()}")
print("Unbounded queue contents:")
while unboundedQueue.get_length() > 0:
    print(f"  {unboundedQueue.dequeue()}")