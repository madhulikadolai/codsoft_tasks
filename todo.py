import os

FILE_NAME = "todo.txt"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- TO-DO LIST -----")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        display_tasks(tasks)

        if tasks:
            try:
                number = int(input("Enter task number to update: "))

                if 1 <= number <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[number - 1] = new_task
                    save_tasks(tasks)
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        display_tasks(tasks)

        if tasks:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")
