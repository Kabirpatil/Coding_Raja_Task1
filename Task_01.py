from datetime import datetime

# Initialize the task list
tasks = []

# Define the file path for data persistence
data_file = "tasks.txt"

# Function to load tasks from a file
def load_data():
    try:
        with open(data_file, "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                title, priority, due_date_str, completed_str = task_data
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
                completed = completed_str == "True"
                tasks.append({"title": title, "priority": priority, "due_date": due_date, "completed": completed})
    except FileNotFoundError:
        pass

# Function to save tasks to a file
def save_data():
    with open(data_file, "w") as file:
        for task in tasks:
            due_date_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else ""
            completed_str = "True" if task["completed"] else "False"
            file.write(f"{task['title']},{task['priority']},{due_date_str},{completed_str}\n")

# Function to add a task
def add_task():
    title = input("Enter task title: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None

    task = {"title": title, "priority": priority, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_data()
    print("Task added successfully.")

# Function to remove a task
def remove_task():
    list_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_data()
        print(f"Removed task: {removed_task['title']}")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed():
    list_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_data()
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to list all tasks
def list_tasks():
    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        due_date = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "N/A"
        print(f"{index}. Title: {task['title']}, Priority: {task['priority']}, Due Date: {due_date}, Status: {status}")

# Load tasks from the file on startup
load_data()

# Main menu loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
