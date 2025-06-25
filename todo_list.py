# Simple To-Do List Application

# Greet the user
print("Welcome to the todo list!")

# Create an empty list to store tasks
TODO = []

# Function to add a new task
def addTask():
    task = input("Enter the task: ")
    TODO.append(task)
    print("Successfully added a new task!")

# Function to view all tasks
def viewTask():
    if not TODO:
        print("There is no task to view")
    else:
        print("Your tasks: ")
        for index, items in enumerate(TODO, start=1):
            print(f"{index}) {items}")

# Function to delete a task
def deleteTask():
    if not TODO:
        print("No task to delete")
        return
    viewTask()
    try:
        task = int(input("Enter the task number to delete: "))
        if 1 <= task <= len(TODO):
            removed = TODO.pop(task - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number")
    except ValueError:
        print("An error has occurred, Please try again")

# Main loop to run the menu
while True:
    try:
        # Show options to the user
        options = int(input("Choose an option: \n 1) Add Task \n 2) View Task \n 3) Delete Task \n 4) Exit \n"))
        
        # Call respective functions based on user input
        if options == 1:
            addTask()
        elif options == 2:
            viewTask()
        elif options == 3:
            deleteTask()
        elif options == 4:
            print("Thanks for using the TODO app")
            break
        else:
            print("Please choose a valid option (1-4)")
    except ValueError:
        print("An error has occurred, Please enter the options properly")
