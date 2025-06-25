#todo list
print("Welcome to the todo list!")
TODO = []

def addTask():
    task = input("Enter the task: ")
    TODO.append(task)
    print("Successfully added a new task!")

def viewTask():
    if not TODO:
        print("There is no task to view")
    else:
        print("Your tasks: ")
        for index, items in enumerate(TODO, start=1):
            print(f"{index}) {items}")
        
def deleteTask():
    if not TODO:
        print("No task to delete")
        return
    viewTask()
    try:
        task = int(input("Enter the task to delete: "))
        if 1 <= task <= len(TODO):
            removed = TODO.pop(task - 1)
            print(f"Task {removed} deleted successfully!")
        else:
            print("Invalid task number ")
    except ValueError:
        print("An error has occurred, Please try againi")
    
while True:
    try:
        options = int(input("Choose an option: \n 1) Add Task \n 2) View Task \n 3) Delete Task \n 4) Exit \n"))
        if options == 1:
            addTask()
        elif options == 2:
            viewTask()
        elif options == 3:
            deleteTask()
        elif options == 4:
            print("Thanks for using the TODO app")
            break
    except ValueError:
        print("An error has occured, Please enter the options properly")
