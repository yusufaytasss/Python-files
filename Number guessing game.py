import random,time

print("""
******************************************************************
                      Number Guessing Game
                       Guess 1-40 Numbers
            *  Just type 'stop' to terminate the program  *
******************************************************************
      """)
random_number = random.randint(1,40)
right_to_predict = 5
while True:
    prediction = input("Your prediction :")
    if (prediction == "stop"):
        print("The program is closing...")
        break
    else:
        prediction = int(prediction)
        if (prediction <= 40 and prediction >= 1):
            if (prediction == random_number):
                print("The number '{}' you guessed is correct!".format(random_number))
                break
            else:
                if (prediction < random_number):
                    print("Information is being questioned ...")
                    time.sleep(1.5)
                    right_to_predict -= 1
                    if (right_to_predict == 0):
                        print("Your guessing right is over! The number would be '{}'.".format(random_number))
                        break
                    else:
                        print("Please enter a higher number...")
                        time.sleep(0.5)
                elif (prediction > random_number):
                    print("Information is being questioned ...")
                    time.sleep(1.5)
                    right_to_predict -= 1
                    if (right_to_predict == 0):
                        print("Your guessing right is over! The number would be '{}'.".format(random_number))
                        break
                    else:
                        print("Please enter a lower number...")
                        time.sleep(0.5)
        else:
            print("Please enter a number between 1 and 40.")
                    