import csv

is_signedin = False

def start_program():
    global is_signedin
    if is_signedin == True:
        signedin()
    if is_signedin == False:
        notsignedin()

def signedin():
    print("Choose: \n    Change Password\n    Logout\n")
    whichopt = input("  ")
    match whichone:
        case "Change password"|"Change Password"|"change password":
            change_password()
        case "Logout"|"logout"|"Log out"|"log out"|"Log Out":
            print("You have logged out.")
            is_signedin = False

def notsignedin():
    print("Choose: \n    Login \n    Register \n    Quit")
    whichone = input("")
    match whichone:
        case "Login"|"login"|"Log in"|"log in"|"Log In":
            login()
        case "Register"|"register":
            register()
        case "Quit"|"quit":
            print("You have quit the program.")



#REGISTER
def register():
        create_account_username()

    #Create account - Username
def create_account_username():
    global username
    username = input("Register Username: ")
    doesusernamealreadyexist()

#Check if the registered username already exists
def doesusernamealreadyexist():
    with open ("source.csv", "a") as file:
        if username == row[0]:
            print("Username is already taken, please enter another.")
        else:
            file.write(f"{username}, ")
        create_account_password()


    #Create account - Password
def create_account_password():
    password = input("Create Password: ")
    with open ("source.csv", "a") as file:
        file.write(f"{password}\n")
    login()

    #Salt & Hash password

#how??

#LOGIN

def login():
    global existingusername
    existingusername = input("Enter Username: ")
    loginusernamechecker()


    #Does Username Exist?
def loginusernamechecker():
    usernamecheck = []

    with open ("source.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            usernamecheck.append({"username": row[0], "password": row[1]})
    if existingusername != row[0]:
        print("Username does not exist, try again.")
    else: 
        print(f"Username accepted, welcome, {existingusername}")
        

    #Is Password Correct?
def loginpasswordchecker():
    passwordcheck = []

    with open ("source.csv") as file:
        for row in reader:
            passwordcheck.append({"password": row[1]})
    if passwordcheck != row[1]:
        print("Incorrect password, try again.")
    else:
        print("Password accepted, logged in.")
        is_signedin = True

#CHANGE PASSWORD
    #Edit source.csv to have the new password
def change_password():
    print("not working yet.")

#LOGOUT
    #End program

#RUN
start_program()