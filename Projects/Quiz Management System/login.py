# login.py
# Function to perform user login

def login:

    # Store data login credentials
    user_name = "admin"
    password_num = "1234"

    # Display project heading 
    print("        QUIZ MANAGEMENT SYSTEM        ")
    
    # Take usernamr & password from user
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Compare entered credentials with stored credentials
    if username == user_name and password == password_num:
        print("Login Successful!\n")
        # Return True if login is successful
        return True

    else:
        print("Invail Username or Password.")
        # Return False if login is fail
        return False