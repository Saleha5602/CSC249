# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:11:24 2025

@author: Alya Saleh
"""

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-" * 30)

def main():
    to_do_list = []  # Initialize an empty list
    choice = None  # Initialize choice to enter the loop
    
    while choice != "4":
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            display_tasks(to_do_list)
        elif choice == "2":
            task = input("Enter the task to add: ").strip()
            if task:
                to_do_list.append(task)
                print(f"'{task}' has been added to your to-do list.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            display_tasks(to_do_list)
            if to_do_list:
                try:
                    task_num = int(input("Enter the task number to mark as completed: "))
                    if 1 <= task_num <= len(to_do_list):
                        completed_task = to_do_list.pop(task_num - 1)
                        print(f"'{completed_task}' has been marked as completed and removed from your list.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting the To-Do List Manager. Goodbye!")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


