

from Task import Task


def load_tasks():
    tasks = []
    with open('tasks.txt','r') as file:
        for line in file:
            if not line.isspace():
                description, completed_str = line.strip().split(',')
                completed = True if completed_str == 'True' else False
                tasks.append(Task(description,completed))
    return tasks


def save_tasks(tasks):
    with open('tasks.txt','w') as file:
        for task in tasks:
            file.write(f'{task.description},{task.completed}\n')


def display(tasks):
    print('To Do List:\n')
    for id,task in enumerate(tasks,start=1):
        status = '#complete#' if task.completed else '#     #'
        print(f'{id}:{status} 3{task.description}')

def remove(tasks,number):
    del tasks[number-1]


    

def main():
    tasks = load_tasks()

    while True:
        
        print("""
            Options:
              1.Display Tasks
              2.Add Task
              3.Mark Task as Completed
              4.Remove  
              5.Quit

            """)
        
        choice = input('Enter your choice:')

        if choice == '1':
            display(tasks)
           
        
        elif choice == '2':
            description = input('\nEnter Task:')
            tasks.append(Task(description))
            save_tasks(tasks)

        elif choice == '3':
            task_number = int(input("\nEnter task number to mark as completed:"))
            tasks[task_number - 1].completed = True
            save_tasks(tasks)
        
        elif choice == '4':
            task_number = int(input("\nEnter task number to be removed:"))
            remove(tasks,task_number)
        
        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print('\nInvalid choice.Please Select a valid option!')


if __name__ == '__main__':
    main()



    
