# To-Do List!!!
import json
from datetime import datetime

# Task class
class Task:
    def __init__(self, id, title, description="", due_date=None, priority="low", status="pending"):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        self.updated_at = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    def to_dict(self):
        return self.__dict__

#Storage Functions

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks_data = json.load(f)
            return tasks_data
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

#Task Processes 
#add

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter the task description (optional): ")
    due_date = input("Enter due date (DD-MM-YYYY) (optional): ")
    priority = input("Enter priority (Low, Medium, Important): ")
    new_id = len(tasks) + 1
    task = Task(new_id, title, description, due_date, priority)
    tasks.append(task.to_dict())
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No task found.")
    else:
        for task in tasks:
            print(f"Task_ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | "
                  f"Priority: {task['priority']} | Status: {task['status']}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the Task ID to mark as completed: "))
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            task['updated_at'] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
            save_tasks(tasks)
            print("Task marked as completed.")
            return
    print("Task not found.")

def delete_tasks(tasks):
    view_tasks(tasks)
    delete_id = int(input("Enter the Task ID to delete: "))
    for task in tasks:
        if task['id'] == delete_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def main_menu():
    print("\n<-- TODOLIST APP MENU -->")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")
    return input("Enter your choice: ")

def main():
    tasks = load_tasks()

    while True:
        choice = main_menu()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
