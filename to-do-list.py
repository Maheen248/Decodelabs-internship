def create_task():
    task = []
    print("----- Welcome to your To-Do List! -----")
    total_task = int(input("how many tasks do you want to add? "))
    for i in range(1 , total_task+1):
     task_name = input(f"Enter task {i}: ")
     task.append(task_name)
    
    print(f"Today's task list is: {task}")
    return task 


def add_task(task , task_name):
    task.append(task_name)
    print(f"{task_name} has been added to your list.")
    print(f"current task list is :{task}")

def del_task(task ,task_name):
    if task_name in task:
        task.remove(task_name)
        print(f"{task_name} has been removed from your list.")
    else:
        print(f"{task_name} is not in your list.")
    print(f"current task list is :{task}")

def update_task(task , old_name , new_task):
    if old_name in task:
        index = task.index(old_name)
        task[index] = new_task
        print(f"{old_name} has been updated to {new_task}.")
    else:
        print(f"{old_name} is not in your list.")

    print(f"current task list is :{task}")

def view_task(task):
    if not task:
        print("Your task list is empty.")
    else:
        print("Your current task list is: ")
        for i,task_name in enumerate(task , start =1):
            print(f"{i}. {task_name} ")
    

def search_task(task , task_name):
    if task_name in task:
        print(f"{task_name} is in your list at index {task.index(task_name)}")
    else:
        print(f"{task_name} is not in your list.")

def save_task(task):
    with open("task_file.txt" , "w") as file:
         if task:
          for t in task:
              file.write(t + "\n")
          print("Your task list has been saved to task_file.txt")
         else:
             print("Your task list is empty. No tasks to save.")




task = create_task()
while True:
    choice = input(" 1.Add task \n 2.Remove task \n 3.Update task \n 4.View tasks \n 5.Search task \n 6.Save tasks \n 7. Exit \n Please select an operation: ")

    if choice == "1":
        new_task = input("enter the task you wanted to add :")
        if new_task not in task:
            add_task(task, new_task)
        else:
            print(f"{new_task} is already in your list.")

    elif choice == "2":
        remove_task = input("enter the task you wanted to remove :")
        del_task(task, remove_task)

    elif choice == "3":
        task_to_update = input("enter the task you wanted to update :")
        new_task = input("enter the updated task :")
        update_task(task, task_to_update, new_task)

    elif choice == "4":
        view_task(task)

    elif choice == "5":
        search_task_name = input("enter the task you wanted to search :")
        search_task(task, search_task_name)

    elif choice == "6":
        save_task(task)
    
    elif choice == "7":
        print("Thank you for using the To-Do List!")
        break
    else:
        print("Invalid choice. Please select a valid operation.")
    