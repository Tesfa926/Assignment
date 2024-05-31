# to do list application Assignment 1 
class Task:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.checked= False

    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def isCompleted(self):
        return self.checked
    def markCompleted(self):
        self.checked=True
class Node:
    def __init__(self, task):
        self.task=task
        self.next=None
class ToDoList:
    def __init__(self) :
        self.head= None
    def addToDO(self,task):# enables the user to add new to-do list
        newNode= Node(task)
        if self.head is None:
            self.head= newNode
        else:
            current= self.head
            while current.next is not None:
                current= current.next
            current.next= newNode
    def markToDoAsCompleted(self,title):# enable the user to mark as completed the tasks are completed
        current =self.head
        while current is not None:
            if current.task.getTitle()==title:
                current.task.markCompleted()
                return 
            current = current.next
        print("Task not found")     
    def viewToDoList(self): # enable the user to see all the to-do lists 
        current= self.head
        while current is not None:
            print(current.task.getTitle())
            current=current.next
    # to check the status of the to do list 
    def viewStatusOfCompletion(self):
        current=self.head
        while current is not None:
            print(current.task.getTitle() + " : "+ str(current.task.isCompleted()))
            current=current.next
finalToDoList= ToDoList()
# the welcome page dispalys options that a user can use
while True:
    print("""WELCOME TO OUR TODOLIST_PLATFORM !
        Here are some commands that make you use the program
        
            #Have a Planned Lifestyle ! #
        
        """)
    print(""" press 1 to add To-Do list

    press 2 to mark a To-Do list as completed
    
    press 3 to view your  To-Do lists
    
    press 4 to view the status of completion
    
    press 5 to exit """ )
    
    choice= int(input("enter here: "))
    
    if choice==1:
        titleof= input("enter the  title of the to-do list to be added: ")
        descriptionof= input("enter the  description of the to-do list to be added: ")
        newtask=Task(titleof,descriptionof)
    
        finalToDoList.addToDO(newtask)
        print("sucessfully added!")
        print("\n")
       
    if choice==2:
        mark=input("enter the title of the to-do list you want it to be marked: ")
        finalToDoList.markAsCompleted(mark)
        print("sucessfully marked as completed")
    if choice==3:
        print("your To-Do List: ")
        finalToDoList.viewToDoList()
        print("\n")
    if choice==4:
        print("here is your status: ")
        finalToDoList.viewStatusOfCompletion()
    if choice ==5:
        print("see you soon")
        break
