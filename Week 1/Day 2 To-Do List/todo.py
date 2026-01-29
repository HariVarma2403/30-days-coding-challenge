import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def mark_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice-1] = tasks[choice-1].replace("[ ]", "[✔]")
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid number.\n")
    except:
        print("Enter a valid number.\n")

def main():
    while True:
        tasks = load_tasks()
        print("=== TO-DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
