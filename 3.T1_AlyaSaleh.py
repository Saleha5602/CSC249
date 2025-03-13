# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:16:41 2025

@author: Alya Saleh
"""

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
   
    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node

#from Node import Node
#from LinkedList import LinkedList


num_list = LinkedList()

node_a = Node("L") # changed the values to string to check how it will work.
node_b = Node("A")
node_c = Node("Y")
node_d = Node("A")
node_e = Node("L")
node_f = Node(9)

num_list.append(node_b)   # changed 99 to A
num_list.append(node_c)   # Add 6, make the tail
num_list.append(node_e)   # Add 10, make the tail

num_list.prepend(node_a)  # Add 2, make the head

num_list.insert_after(node_c, node_d)  
num_list.insert_after(node_e, node_f)  

# Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.remove_after(node_e)   # Remove the tail (10)
num_list.remove_after(None)     # Remove the head (2)


# Output final list
print('List after removing nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()
