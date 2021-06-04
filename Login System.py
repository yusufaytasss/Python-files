import time,random
print("""
             *WELCOME TO THE SYSTEM*
""")
time.sleep(1)
print("""
        -SELECT THE ACTION YOU WANT TO DO-

        1.Login the system
        2.Register
        3.I forgot my password
        4.Exit
""")
time.sleep(2)
selection = int(input("Choose the action you want to take : "))
time.sleep(2)

while True:
    while(selection == 1 or selection == 2 or selection == 3 or selection == 4):
        #Admin and user login block
        if(selection == 1):
            print("If you forgot your password, you can write 'forgot password' in the password section.")
            time.sleep(2)
            username = input("Enter your username \n : ")
            time.sleep(2)
            userpassword = input("Enter your password \n : ")

            #User login and password forgot block
            if(userpassword == "forgot password"):
                print("WELCOME TO PASSWORD RECOVERY")
                time.sleep(1.5)
                print("Receiving information...")
                time.sleep(3)
                rescue = int(input("Please enter the recovery code : "))

                #Activating the recovery code
                if(rescue == recovery_code):
                    print("The system is logged in, would you like to reset your password? (T/F)")
                    question = input("Selection : ")
                    if(question == "T"):
                        print("Password reset is in progress...")
                        time.sleep(5)
                        new_password = input("Enter your new password")
                        time.sleep(3)
                        print("The password has been changed. Exiting the program...")
                        exit()
                    elif(question == "F"):
                        print("Your selection has been confirmed!")
                else:
                    print("The recovery code is incorrect. Signed out of the system!")
                    exit()
        
            #Login
            if(username == "admin" and userpassword == "admin123" or username == new_username and userpassword == new_password):
                print("You have successfully logged into the system !!!")
                break
            else:
                print("Receiving information...")
                time.sleep(3)
                print("An error occurred while logging into the system !")
                time.sleep(1)
                print("Check your information again...")
                time.sleep(3)

        #Register
        if(selection == 2):
            print("Be careful not to forget your password when creating a new registration :) ")
            time.sleep(2)
            new_username = input("Enter your username : ")
            new_password = input("Enter your password : ")
            new_password_again = input("Please a enter again you password : ")

            #Password sync
            if(new_password != new_password_again):
                right_to_repeat = 3
                while(new_password != new_password_again):
                    right_to_repeat -= 1
                    print("Error ! Passwords do not match.")
                    time.sleep(2)
                    print("re-enter your password : ")
                    time.sleep(2)
                    new_password = input("Enter your password : ")
                    new_password_again = input("Please a enter again you password : ")
                    if(right_to_repeat == 0):
                        print("You have been kicked from the system !")
                        exit()
                print("Registration Successful !")

            if(new_password == new_password_again):
                print("Welcome to the system, nice to see you")
                time.sleep(3)
                recovery_code = random.randint(1,10000)
                print("If you forget your password or username, you can access the system by typing the '{}' code.".format(recovery_code))
                time.sleep(1.5)
                selection = int(input("Select the action you want to do : "))
            
        #forgot password block
        if(selection == 3):
            print("WELCOME TO PASSWORD RECOVERY")
            time.sleep(1.5)
            print("Receiving information...")
            time.sleep(3)
            rescue = int(input("Please enter the recovery code : "))
            if(rescue == recovery_code):
                print("The system is logged in, would you like to reset your password? (T/F)")
                question = input("Selection : ")
            if(question == "T"):
                print("Password reset is in progress...")
                time.sleep(5)
                new_password = input("Enter your new password")
                time.sleep(3)
                print("The password has been changed. Exiting the program...")
                exit()
            elif(question == "F"):
                print("Your selection has been confirmed!")
                time.sleep(3)
                exit()
    
        #Exiting the program
        if(selection == 4):
            print("The program is terminating...")
            time.sleep(2)
            print("have a nice day")
            exit()

    else:
        print("Wrong choice! try logging in again")
        selection = int(input("Choose the action you want to take : "))
    
