tasks=[]

def AddTask():
    task=input("enter any task you want to add")
    tasks.append(task)
    print(f"the task '{task} is added.")

def ListTask():
    if not tasks:
        print("You're all done:). No tasks for the moment")
    else:
        print("Given below is the list of tasks:")
    for index,task in enumerate(tasks):
        print(f"Task no.{index}. {task}")


    
def RemoveTask():
    ListTask()
    deletedtask=int(input("enter the task number to be deleted:"))
    if deletedtask<= len(tasks):
        tasks.pop(deletedtask)
        print(f"the task number '{deletedtask} has been removed")
    else:
        print("Invalid Choice. Please try again")


if __name__ == "__main__":
    print("Hey, Welcome to the To Do list app")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice number: ")
     
        if (choice == "1"):
          AddTask()
        elif (choice == "2"):
          RemoveTask()
        elif (choice == "3"):
          ListTask()
        elif (choice == "4"):
          break
        else: 
          print("Invalid Choice")
    
    print("Goodbye!!")