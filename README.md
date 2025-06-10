# Command line interface Task Manager built in Python

This program allows users to register, log in, and manage personal to do tasks securely using password hashing and persistent storage through JSON files. 

# Features

* #### User registration and login:
  
        Securely register and authenticate users using hashed passwords (SHA-256)
  
* #### Task management:
  
        Add, view, complete, and delete tasks per user
  
* #### Secure password storage:
  
        Passwords are never stored in plain text
  
* #### Data Persistence:
        All users and tasks are saved to .json files

* #### User sessions:
        Only the logged in user can manage their tasks

# How to run it: 
  1. Make sure you have python 3 installed
  2. Save the files as task_manager.py
  3. In your terminal or command prompt, run:
     
     ```python
     python task_manager.py
     ```
     
This will run an interactive menu in the terminal 

# Menu Options: 

1. Register a new user
2. Login with existing credentials
3. Add a new task only after login
4. View all your tasks
5. Mark a task as completed
6. Delete a task
7. Logout from current session
8. Exit the program

# How password security works: 

  Passwords are hashed using SHA-256. This ensures that even if someone gains access to users.json, they won't be able to read the original passwords. 
  ``` python
hashlib.sha256(password.encode()).hexdigest()
```
This never stores the password in plain text. 

# Data Storage 

* Users are stored in users.json in this format:
  
  ``` python
  {
    "username1": "hashed_password",
    "username2": "hashed_password"
  }
  ```

 * Tasks are stored in tasks.json as:

    ```python
    {
      "username1": [
        {
          "id":1,
          "description": "Example Task",
          "status": "Pending"
        }
      ]
    }
    ```

# How it works: 

  * Users are stored as key value pairs (username: password hash)
  * Tasks are linked to usernames and stored as lists
  * All operations (registering, adding tasks, etc.) update the corresponding .json file

# Files Generated 

After running the program, two files will be created if they don't already exist: 
  * users.json - stores all user credentials securely
  * tasks.json - stores user specific task lists

# Example Usage: 

<pre>
Task Manager Menu:
1. Register
2. Login
3. Add Task
...
Choose an option: 1
Enter username: alice
Enter password: secret123
Registration Successful!
</pre> 

# Future improvements (Ideas) 
* Add password validation rules (minimum lenght, symbols)
* Add due dates or priority levels for tasks
* Export task lists to .csv or .txt
* Build a simple GUI with tkinter or PyQt
* Add a search or filter system for tasks

# Dependencies 
No external libraries required. Uses only python built in modules: 
* hashlib
* json
* os

# Author
Developed by Jean Carlo Latorre Vargas 
