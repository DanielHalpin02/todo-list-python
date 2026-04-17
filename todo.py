tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("|")
                if len(parts) == 2:
                    task_name = parts[0]
                    is_done = parts[1] == "True"
                    tasks.append({"name": task_name, "done": is_done})
except FileNotFoundError:
    pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['done']}\n")


while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter a task: ")
        tasks.append({"name": task_name, "done": False})
        save_tasks()
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Not completed"
                print(f"{i}. {task['name']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Not completed"
                print(f"{i}. {task['name']} - {status}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks()
                    print(f"Removed: {removed['name']}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Not completed"
                print(f"{i}. {task['name']} - {status}")

            try:
                num = int(input("Enter task number to mark as completed: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks()
                    print("Task marked as completed!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")