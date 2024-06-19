class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def mark_undone(self):
        self.is_done = False

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        status = "Done" if self.is_done else "Not Done"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def update_task(self, index, description=None, status=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if description is not None:
                task.update_description(description)
            if status is not None:
                if status:
                    task.mark_done()
                else:
                    task.mark_undone()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
            print("Task added.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to update: ")) - 1
                print("1. Edit Description")
                print("2. Mark as Done")
                print("3. Mark as Undone")
                update_choice = input("Enter your choice: ")
                
                if update_choice == '1':
                    new_description = input("Enter the new description: ")
                    todo_list.update_task(index, description=new_description)
                    print("Task updated.")
                elif update_choice == '2':
                    todo_list.update_task(index, status=True)
                    print("Task marked as done.")
                elif update_choice == '3':
                    todo_list.update_task(index, status=False)
                    print("Task marked as undone.")
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
                print("Task deleted.")
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
