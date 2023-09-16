tasks = []
def display_menu():
    print("To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")
def mark_task_done():
    view_tasks()
    task_number = int(input("Enter the task number to mark as done: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")
while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task['task']}|{task['done']}\n")
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
