from task import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the task index to complete: "))
            todo_list.complete_task(index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

