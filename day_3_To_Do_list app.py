from datetime import datetime  # Import datetime module to handle timestamps

todo_list = []  # Stores tasks as dictionaries: {"task": "Buy milk", "done": False, "created_at": timestamp, "important": False}

def show_tasks():
    if not todo_list:
        print("\n✅ Your To-Do List is empty.")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(todo_list, 1):  # enumerate(todo_list, 1) adds index starting from 1
            status = "✔️" if task["done"] else "❌"  # Ternary operator for done status
            priority = "⭐" if task["important"] else ""  # Ternary operator: ⭐ for important tasks, empty string otherwise
            timestamp_str = f"Created: {task['created_at'].strftime('%Y-%m-%d %H:%M:%S')}"  # Format creation timestamp
            if task.get("updated_at"):  # Safely check for updated_at
                timestamp_str += f", Updated: {task['updated_at'].strftime('%Y-%m-%d %H:%M:%S')}"
            print(f"{i}. {task['task']} {priority} [{status}] ({timestamp_str})")  # Include priority in output

def add_task():
    task_name = input("\nEnter a new task: ")
    todo_list.append({
        "task": task_name,
        "done": False,
        "created_at": datetime.now(),
        "important": False  # New tasks are not important by default
    })
    print(f"➕ Task '{task_name}' added!")
    

def mark_done():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("\nEnter task number to mark as done: "))  # Convert input to integer
        if 0 < task_num <= len(todo_list):  # Validate task number
            todo_list[task_num - 1]["done"] = True
            todo_list[task_num - 1]["updated_at"] = datetime.now()  # Update timestamp
            print(f"✔️ Task '{todo_list[task_num - 1]['task']}' marked as done.")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:  # Catch non-numeric input
        print("⚠️ Please enter a valid number!")

def mark_important():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("\nEnter task number to toggle importance: "))  # Get task number
        if 0 < task_num <= len(todo_list):  # Validate task number
            task = todo_list[task_num - 1]
            task["important"] = not task["important"]  # Toggle important status (True to False or False to True)
            task["updated_at"] = datetime.now()  # Update timestamp when importance changes
            status = "important" if task["important"] else "not important"
            print(f"⭐ Task '{task['task']}' marked as {status}.")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:  # Catch non-numeric input
        print("⚠️ Please enter a valid number!")

def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)  # Remove task
            print(f"🗑️ Task '{removed_task['task']}' deleted.")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

# Main loop
while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Mark/unmark task as important")  # New menu option
    print("5. Delete task")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":  # New option for marking important
        mark_important()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("👋 Exiting To-Do List App. Goodbye!")
        break  # Exit loop
    else:
        print("⚠️ Invalid choice. Please try again.")