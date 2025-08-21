from datetime import datetime  # Import datetime for timestamps

todo_list = []  # Stores tasks as dictionaries: {"task": "Buy milk", "done": False, "created_at": timestamp}

def show_tasks():
    if not todo_list:
        print("\n✅ Your To-Do List is empty.")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = "✔️" if task["done"] else "❌"
            # Display task with creation timestamp and updated timestamp if available
            timestamp_str = f"Created: {task['created_at'].strftime('%Y-%m-%d %H:%M:%S')}"
            if task.get("updated_at"):
                timestamp_str += f", Updated: {task['updated_at'].strftime('%Y-%m-%d %H:%M:%S')}"
            print(f"{i}. {task['task']} [{status}] ({timestamp_str})")

def add_task():
    task_name = input("\nEnter a new task: ")
    # Add task with current timestamp
    todo_list.append({
        "task": task_name,
        "done": False,
        "created_at": datetime.now()
    })
    print(f"➕ Task '{task_name}' added!")

def mark_done():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 0 < task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            # Update timestamp when marking as done
            todo_list[task_num - 1]["updated_at"] = datetime.now()
            print(f"✔️ Task '{todo_list[task_num - 1]['task']}' marked as done.")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
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
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting To-Do List App. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")