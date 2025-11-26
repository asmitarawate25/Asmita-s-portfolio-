# Asmita's To-Do List App


tasks = []


while True:
    print("\n--- Asmita's To-Do App ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")


    choice = input("Choose an option (1-4): ")


    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")


    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")


    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("\nSelect task number to delete:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            
            delete_index = int(input("Enter number: "))
            if 1 <= delete_index <= len(tasks):
                removed = tasks.pop(delete_index - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number!")


    elif choice == "4":
        print("Goodbye!")
        break


    else:
        print("Invalid option! Choose 1-4.")