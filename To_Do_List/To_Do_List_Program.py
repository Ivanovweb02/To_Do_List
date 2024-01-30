

def add_task(some_task: str) -> str:
    task_status = '[ ]'
    list_of_task.append([some_task, task_status])
    return f'Task "{some_task}" added successfully!'


list_of_task = []
while True:
    print("=== To-Do List Menu ===")
    print("""
    1. Add a new task
    2. Mark a task as completed
    3. View all task
    4. Quit
    """)

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        task_description = input("Enter a task description: ")
        print(add_task(task_description))

    elif choice == '2':
        print("=== Tasks ===")
        for index in range(len(list_of_task)):
            print(f"{index}. {list_of_task[index][1]} {list_of_task[index][0]}")
        completed_task = int(input("Enter the index of the task to mark as completed: "))
        if completed_task not in range(len(list_of_task)):
            print("Invalid Input. Try Again!")
            completed_task = int(input("Enter the index of the task to mark as completed: "))
            continue
        elif list_of_task[completed_task][1] == '[X]':
            print("Task already completed. Try with another one!")
            completed_task = int(input("Enter the index of the task to mark as completed: "))
            continue
        list_of_task[completed_task][1] = "[X]"
        print(f"Task marked as completed!")

    elif choice == '3':
        print("==== Task ===")
        for index in range(len(list_of_task)):
            print(f"{index}. {list_of_task[index][0]} {list_of_task[index][1]}")
        print()

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("invalid Input. Try Again !")
        continue
