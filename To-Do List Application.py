# To-Do List Application with Multiple Task Management
# Add, View and Remove Tasks 

tasks = [] 

def add_tasks(task_input):
    """Add one or more tasks (comma-separated)"""
    new_tasks = [t.strip() for t in task_input.split(",") if t.strip()]
    tasks.extend(new_tasks)
    print(f"✅ Added {len(new_tasks)} task(s): {', '.join(new_tasks)}")

def view_tasks():
    """View all tasks"""
    if not tasks:
        print("📭 No tasks found!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(index):
    """Remove a task by its index"""
    try:
        removed = tasks.pop(index - 1)
        print(f"🗑️ Task removed: {removed}")
    except IndexError:
        print("⚠️ Invalid task number!")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task(s)")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_input = input("Enter task(s) (separate multiple with commas): ")
            add_tasks(task_input)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
