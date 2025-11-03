def main():
    # Main function: runs the whole To-Do List program
    tasks = []        # list to store all tasks
    done_tasks = []   # list to store completed tasks

    try:
        while True:
            # Display menu options
            print("""==== To-Do List ====
1. Add a new task
2. View all tasks
3. Mark a task as done
4. Delete a task
5. Exit""")
            
            choose = int(input("Choose an option (1-5): "))

            # Match user's choice
            match choose:
                case 1:
                    # Add a new task
                    new_task = input("Enter task name: ")
                    add(tasks, new_task)
                case 2:
                    # Show all tasks
                    view(tasks, done_tasks)
                case 3:
                    # Mark a task as done
                    marked = int(input("Enter the number of the task you finished: "))
                    mark(tasks, done_tasks, marked)
                case 4:
                    # Delete a task by its number
                    num_to_delete = int(input("Enter the number of the task you want to delete: "))
                    delete(tasks, done_tasks, num_to_delete)
                case 5:
                    # Exit the program
                    print("✅ All saved! Have a productive day!")
                    break
                case _:
                    # Handle invalid menu choice
                    print("Invalid choice")

    except ValueError:
        # Handle invalid input (like letters instead of numbers)
        print("You should enter just numbers from 1 to 5")


def add(tasks, new_task):
    # Add a task only if it's not empty or just spaces
    if new_task.strip():
        tasks.append(new_task)
        return True
    return False


def view(tasks, done_tasks):
    # Display all tasks and their status
    if tasks:
        print("==== Your Tasks ====")
        for index, task in enumerate(tasks):
            if task in done_tasks:
                print(f"{index + 1}. {task} [Done]")
            else:
                print(f"{index + 1}. {task}")
    else:
        print("No tasks yet! Add one first.")


def mark(tasks, done_tasks, marked):
    # Mark a specific task as done
    try:
        if not tasks:
            return "No tasks to mark as done!"

        if marked <= 0 or marked > len(tasks):
            return "Invalid number!"

        task = tasks[marked - 1]
        if task not in done_tasks:
            done_tasks.append(task)
            return f'Task "{task}" marked as done!'
        else:
            return "This task is already marked as done!"
            
    except ValueError:
        return "Invalid input! Please enter a number."


def delete(tasks, done_tasks, num_to_delete):
    # Delete a task by its number
    try:
        if num_to_delete > len(tasks) or num_to_delete <= 0:
            return "Task number not found! Try again."
        else:
            removed = tasks.pop(num_to_delete - 1)
            # Remove it from done_tasks too (if it was marked done)
            if removed in done_tasks:
                done_tasks.remove(removed)
            return f"Task {removed} deleted successfully!"
    except ValueError:
        return "Invalid input! Please enter a number."


# Run the program
if __name__ == "__main__":
    main()
