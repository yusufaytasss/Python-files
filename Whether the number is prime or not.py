def Prime_number(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for i in range (2,number):
            if (number % i == 0):
                return False
            return True
while True:
    number = input("Number :")
    
    if (number == "q"):
        break
    else:
        number = int(number)
        
        if(Prime_number(number)):
            print(number,"Is a prime number.")
        else:
            print(number,"It is not a prime number.")