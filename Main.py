from tasks import add_task, view_tasks, delete_task

def main():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                task = input("Enter task: ")
                add_task(task)

            elif choice == "2":
                view_tasks()

            elif choice == "3":
                number = int(input("Enter task number: "))
                delete_task(number)

            elif choice == "4":
                print("Thank you!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()