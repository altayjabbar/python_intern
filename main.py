class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False  

    def task_completed(self):
        self.completed = True  

    def __str__(self):
        status = "++++++" if self.completed else "------"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []  

    def add_task(self, description):
        task = Task(description)  
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task_completed()
            print("Task  completed!")
        else:
            print("Error!!!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}") 



todo_list = ToDoList()

while True:
    print("To-Do List")
    print("1. Add a new task")
    print("2. Task completed")
    print("3. Show all tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_description = input("Enter the task description: ")
        todo_list.add_task(task_description)

    elif choice == "2":
        todo_list.show_tasks()
        task_id = int(input("Enter the task number to task completed: ")) - 1
        todo_list.complete_task(task_id)

    elif choice == "3":
        todo_list.show_tasks()

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print(" please try again.")
