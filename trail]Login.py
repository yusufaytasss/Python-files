import time,random
print("Welcome to the system")
time.sleep(0.5)
print("Enter 'registration' to register, 'login' to log into the system or 'forgot my password' if you have forgotten your password.")
operation = input("Choose an action")

while True:
    if(operation == "registration"):
        User_Name = float(input("Please set a username :"))
        time.sleep(0.5)
        password = float(input("Please set a password :"))
        time.sleep(0.5)
        Recovery_password = random.randint(1,10000)
        print("If you have forgotten your password, you can log into the system by entering the {} recovery password.")

    if(operation == "login"):
        loginUser_Name = float(input("Enter the system username :"))
        loginpassword = float(input("Enter the system password :"))

    #Login system
    if(operation == User_Name and operation == password):
        print("Login successful.")
    if(operation == "forgot my password"):
        if(operation == Recovery_password):
            print("Login successful.")