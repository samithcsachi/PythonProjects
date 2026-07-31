import json

file_name = "todo_list.json"
COMPLETED = "Completed"
PENDING = "Pending"
INCOMPLETE = "Incomplete"


def load_tasks():

    try: 
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_task(tasks):
    try: 
        with open(file_name, "w") as file:
            return json.dump(tasks, file)
    except:
        print("Failed to save")

def view_task(tasks):
    print()

    task_list = tasks["tasks"]

    if not task_list:
        print("No tasks to display")
    else:
        print("Your To-Do list: ")

        for idx, task in enumerate(task_list):
            status = task["status"]
            print(f"{idx + 1}. {task['description']} | {status}")

def create_task(tasks):
    description = input("Enter the task description: ").strip()

    if description:
        tasks["tasks"].append({
            "description": description,
            "status": PENDING
        })
        save_task(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty")

def mark_task_complete(tasks):
    view_task(tasks)

    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        

        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["status"] = COMPLETED
            save_task(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_task_incomplete(tasks):
    view_task(tasks)

    try:
        task_number = int(input("Enter the task number to mark as incomplete: ").strip())
        

        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["status"] = INCOMPLETE

            save_task(tasks)
            print("Task marked as Incomplete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")    

def delete_task(tasks):
    view_task(tasks)

    try:
        task_number = int(input("Enter the task number to delete: ").strip())

        if 1 <= task_number <= len(tasks["tasks"]):
            removed = tasks["tasks"].pop(task_number - 1)
            save_task(tasks)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Enter a valid number.")


def main():
    tasks= load_tasks()

    while True:
        print("\n To-Do list Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Incomplete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice : ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice =="3":
            mark_task_complete(tasks)
        elif choice =="4":
            mark_task_incomplete(tasks)

        elif choice =="5":
            delete_task(tasks)

        elif choice == "6":
            print("Goodbye")
            break
        else: 
            print("Invalid choice. Please try again")





if __name__ == "__main__":
    main()
