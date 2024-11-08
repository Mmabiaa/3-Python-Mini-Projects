import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []  # If the file doesn't exist, return an empty list

    with open(TASKS_FILE, "r") as file:
        tasks = []
        for line in file:
            task = line.strip().split(" - ")
            tasks.append({"task": task[0], "completed": task[1] == "Completed"})
        return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            file.write(f"{task['task']} - {status}\n")

# Function to add a new task
def add_task(tasks):
    task_description = input("Enter the task description: ")
    tasks.append({"task": task_description, "completed": False})
    save_tasks(tasks)
    print(f'Task "{task_description}" added.')

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task "{task["task"]}" removed.')
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_index]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

# Function to view all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")
    print()

# Main menu function
def main():
    tasks = load_tasks()
    while True:
        print("\nWelcome to the To-Do List App!")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
