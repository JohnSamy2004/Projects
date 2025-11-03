# To-Do List

#### Video Demo:  [To-Do List video Project](https://youtu.be/xZMM1IGCYt4)

#### Description:
This project is a **simple To-Do List application** implemented in Python. It allows users to manage their daily tasks directly from the terminal. The program provides a menu-driven interface to perform several actions:

- **Add a new task:** Users can add tasks with a name. Empty or whitespace-only task names are rejected.
- **View all tasks:** Displays all tasks with a numbering system. Completed tasks are marked with `[Done]`.
- **Mark a task as done:** Users can select a task number to mark it as completed.
- **Delete a task:** Users can remove a task by its number, which also removes it from the list of completed tasks if marked.
- **Exit:** Closes the application.

The project consists of multiple functions to handle each feature (`add`, `view`, `mark`, `delete`) and a main function that runs the program. It is designed to be **modular and testable**, with separate unit tests written in `test_to_do_list.py` using `pytest`.

#### Project Structure:
