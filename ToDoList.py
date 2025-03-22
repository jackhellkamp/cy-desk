import gradio as gr   # Import gradio for eventual deployment as a rudimentary web app


task_list = []    # Initialize an empty list to store tasks

def add_task(task):   # Add task fuction
  task_list.append(task)
  print(f"Task '{task}' added to ToDo list.")
  view_tasks()

def remove_task(index):   # Remove task function (NEEDS CHECKS FOR INDEX OUT OF RANGE)
  index = index - 1
  task_list.pop(index)

def view_tasks():   # View tasks function
  if len(task_list) == 0:
    print("Your ToDo list is empty. Add a task.")
  else:
    index = 1
    for task in task_list:
      print(f"{index}. {task}")
      index += 1

def run_list():   # Main function to run the ToDo list
  print("Welcome to the ToDo List App!")
  print("Select an option: ")
  running = True
  while running:
    print("Options:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) View Tasks")
    print("4) Quit")

    choice = input("")
    if choice == "1":
      task = input("Enter a task: ")
      add_task(task)
    elif choice == "2":
      view_tasks()
      index = int(input("Enter the list position of the task to remove: "))
      remove_task(index)
    elif choice == "3":
      view_tasks()
    elif choice == "4":
      print("Have a good day!")
      running = False

run_list()