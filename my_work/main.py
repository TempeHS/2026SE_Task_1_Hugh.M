import csv

def start_program():
    global is_signedin
    if is_signedin == True:
        signedin()
    if is_signedin == False:
        notsignedin()

def signedin():
        print("Choose: \nLogin \nRegister \nQuit")
    whichone = input("  ")
    match whichone:
        case "Login" | "login":
            login()
        case "Register"|"register":
            register()
        case "Quit"|"quit":
            print("You have quit the program.")

def notsignedin():
    print("Choose: \nLogin \nRegister \nQuit")
    whichone = input("  ")
    match whichone:
        case "Login" | "login":
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
    with open ("source.csv", "a") as file:
        file.write(f"{username}, ")
    
    create_account_password()

    #Create account - Password
def create_account_password():
    password = input("Create Password: ")
    with open ("source.csv", "a") as file:
        file.write(f"{password}\n")
    login()

    #Salt & Hash password



    #Is UN the same as another?
#def username_issameassomeoneelse():
    


#LOGIN
    #Does UN Exist?
def login():
    loginusernamechecker()

def loginusernamechecker():
    usernamecheck = []

    with open ("source.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            usernamecheck.append({"username": row[0]})
    if usernamecheck != row[0]:
        print("Username does not exist, try again.")
    else: 
        print("Username accepted.")
        loginpasswordchecker()

    #Is PW Correct?
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

    #Update menu


#QUIT

    #End program



#CHANGE PASSWORD
    #Edit plain_text.txt to have the new password


#LOGOUT
    #End program

#RUN
start_program()