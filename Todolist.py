# Build a to-do list manager that:
#     •   Allows users to add tasks with priorities (e.g., "Buy milk - high").
#     •   Lets them view the current list, delete tasks by number, and mark tasks as complete.
#     •   Keeps looping until the user types “exit”.
#     •   Shows a summary at the end: number of completed tasks vs pending.
# Skills practiced: lists, string parsing, loops, input, CRUD basics

# note: commands(add,view,complete,dellete,exist)


# Step-1: Welcome message
print("============= Group Two's To-Do List =============")
print()

# Step - 2: Initialize task as an empty list
tasks = []
completed_tasks = []

# Step-3: Create a command lists that a user can practice in the To-Do activity
print("Available Commands in this To-Do List are: 'Add', 'Delete', 'View', 'Complete' and 'Exit'.")
print()

while True:
    # Step-4: Get commands from the user
    user_command = input('Please enter a command that you want to do: ').strip().lower()
    print()

    # Step-5: Use conditional formatting to execute the above five commands
    # For 'exit' condition
    if user_command == 'exit':
        print(" You exited! ")
        break
    # For 'add' condition
    elif user_command == 'add':
        # Get task description and priority for the task from the user as in the example specification
        user_task = input('Enter tasks with priorities (e.g., "Buy milk - high"): ').strip().title()
        if ' - ' in user_task:
            tasks.append(user_task)
            print(f"Your task '{user_task}' is added to the tasks list")
            print()
        else:
            print(f'You entered incorrectly. Please make sure you entered the task as in the example format.')
            print()
    # For 'delete' condition
    elif user_command == 'delete':
        if not tasks:
            print('There is no any task in the list for deleting.')
            print()
        else:
            print(' ===== List of Tasks ==== ')
            i = 0
            for task in tasks:
                i += 1
                print(f"{i}. {task}")
            print()
            try:
                task_number = input('Please enter task number from the list of tasks above: ')
                task_number_int = int(task_number)
                if task_number_int in range(1, len(tasks)+1):
                    removed_task = tasks.pop(task_number_int - 1)
                    print(f"You delete the task '{removed_task}' from the task list.")
                    print()
                else:
                    print(f"You entered incorrect task number. Please use a number between 1 and {len(tasks)}.")
                    print()
            except ValueError:
                print('Invalid number. Please enter again.')
                print()
    # For 'view' condition
    elif user_command == 'view':
        if not tasks:
            print('There is no any task in the list to view.')
        else:
            print('List of Tasks')
            i = 0
            for task in tasks:
                i += 1
                print(f"{i}. {task}")
# For 'complete' condition
    elif user_command == 'complete':
        if not tasks:
            print('There is no any task in the list to complete.')
        else:
            print(' ==== List of Tasks ====')
            i = 0
            for task in tasks:
                i += 1
                print(f"{i:}. {task}")
            print()
            try:
                task_number = input('Please enter task number from the above list of tasks you completed: ')
                task_number_int = int(task_number)
                if task_number_int in range(1, len(tasks)+1):
                    completed_task = tasks.pop(task_number_int - 1)
                    completed_tasks.append(completed_task)
                    print(f"You completed the task '{completed_task}' from the task list.")
                    print()
                else:
                    print(f"You entered incorrect task number. Please use a number between 1 and {len(tasks)}.")
                    print()
            except ValueError:
                print('Invalid number. Please enter again.')
                print()
    #For incorrect command input
    else:
        print(f'You entered incorrect command. {user_command} is not in the command list')
# Step-6: Print the To-Do List summary

print(f"Number of Completed tasks = {len(completed_tasks)}")
print(f"Number of pending tasks ={len(tasks)} ") 
    