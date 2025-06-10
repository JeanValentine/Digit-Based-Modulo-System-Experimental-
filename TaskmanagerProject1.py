import hashlib 

'''Lets us create a hash version of passwords. Hashing means we are converting the password 
into a fixed size code that is not so easily reversible. This is important for the security 
of the passwords. It makes sure the password isnt stored as plain text.'''

import json #json stores data like a dictionary. I used json because it stores data easily 
import os #helps us check if the data files exist or not 


class TaskManager: 

    #grouping the data into one place 

    def __init__(self): 

        '''Our constructor method which will run when we create a new TaskManager.
        It will set up file names and load existing users calling it with 'self'. '''

        self.users_file = 'users.json'
        self.tasks_file = 'tasks.json'
        self.current_user = None
        self.load_users()
        self.load_tasks()

    #loading users and tasks: 

    #Loading users data from JSON file 

    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}

    #loading tasks data 

    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = {}

    '''This will check if the data files exist. If they do exist then it will load the 
    data into the dictionaries self.users and self.tasks. If not then it will start with 
    an empty dictionary {}.'''

    #Saving users and tasks to JSON file: 

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f) 

    def save_tasks(self):
        """Save tasks data to JSON file."""
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f)

    #we use json.dump() to convert python dictionaries to JSON.
    #This saves changes like when we add new users, add tasks, or complete tasks. 

    #Password Hashing: 

    #Hash password using SHA-256

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    '''This will convert the password string to bytes with .encode(). 
    It will also create a SHA-256 hash which is a fixed length code. It will then 
    convert the hash to a readable hexadecimal string with .hexdigest(). 
    This protects the passwords when we store it. You would never really save the 
    raw password. '''

    #User registration: 

    #Registering a new user if the username is new 

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username")
            return False
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self.save_users()
        print("Registration successful!")
        return True
    
    '''This checks if the username is already taken or not. If the username is new then 
    it the program will continue to hash the password and store it in self.users. 
    This willl save the users data to the file and return True on success or False if username exists. '''

    #User login 

    #Login the user by verifying its credentials 

    def login(self, username, password):
        if username not in self.users:
            print("Username does not exist. Please register first.")
            return False
        hashed_password = self.hash_password(password)
        if self.users[username] == hashed_password:
            self.current_user = username #if self.current_user is correct then you successfully logged in 
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Please try again.")
            return False

    #Adding a task: 

    #Adds a new task for the logged in user 

    def add_task(self, description):
        if self.current_user is None:
            print("You must be logged in to add a task.")
            return
        task_id = len(self.tasks.get(self.current_user, [])) + 1
        task = {
            'id': task_id,
            'description': description,
            'status': 'Pending'
        }
        if self.current_user not in self.tasks:
            self.tasks[self.current_user] = []
        self.tasks[self.current_user].append(task)
        self.save_tasks()
        print(f"Task added: {task}")

        '''Checks if a user is logged in in the first place. 
        It generates a new task Id by counting the users current tasks +1. 
        It also creates a task dictionary with the ID, description and status. 
        The program will addd the task to the current users task list and save the task to that file. '''

    #Viewing tasks: 

    #Display all tasks for the logged in user 

    def view_tasks(self):
        if self.current_user is None:
            print("You must be logged in to view tasks.")
            return
        user_tasks = self.tasks.get(self.current_user, []) #uses .get with default empty list to avoid errors 
        if not user_tasks:
            print("No tasks found.")
            return
        for task in user_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

    #Marking a task as completed 

    #Masking specific tasks

    def mark_task_completed(self, task_id):
        if self.current_user is None:
            print("You must be logged in to mark a task as completed.")
            return
        user_tasks = self.tasks.get(self.current_user, [])
        for task in user_tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    #Will find the task ID and update its status field to be completed

    #Deleting a task: 

    def delete_task(self, task_id):
        if self.current_user is None:
            print("You must be logged in to delete a task.")
            return
        user_tasks = self.tasks.get(self.current_user, [])
        for task in user_tasks:
            if task['id'] == task_id:
                user_tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")

    #looks up the task Id and removes it from the users list. 

    #Logging out: 

    def logout(self):
        if self.current_user is None: #clears self.current_user so no one is logged in 
            print("You are not logged in.")
            return
        print(f"User {self.current_user} logged out.")
        self.current_user = None

    #Interactive menu: 

    #The main menu for the task manager 

    '''Print options for the user and takes the input and calls on a specific method. 
    It also loops forever until the user selects exit. It is also capable of handling invalid inputs. '''

    def menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Add Task")
            print("4. View Tasks")
            print("5. Mark Task as Completed")
            print("6. Delete Task")
            print("7. Logout")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.register(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.login(username, password)
            elif choice == '3':
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                try:
                    task_id = int(input("Enter task ID to mark as completed: "))
                    self.mark_task_completed(task_id)
                except ValueError:
                    print("Invalid task ID.")
            elif choice == '6':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid task ID.")
            elif choice == '7':
                self.logout()
            elif choice == '8':
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid option. Please try again.")

#Running the program itself:

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.menu()

    '''This block tuns the program when you execute the file and creates a TaskManager 
    object and immediately launches the menu. '''
