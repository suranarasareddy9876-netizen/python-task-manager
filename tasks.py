tasks = []

def add_task(task):
    if not task.strip():
        raise ValueError("Task cannot be empty")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(number):
    try:
        task = tasks.pop(number - 1)
        print(f"Deleted: {task}")
    except (IndexError, ValueError):
        print("Invalid task number.")