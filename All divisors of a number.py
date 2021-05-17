def full_divisors(number):
    divisors = []
    
    for i in range(2,number):
        if(number % i == 0):
            divisors.append(i)
    return divisors

while True:
    number = input("Number :")
    
    if(number == "q"):
        print("The program is closing")
        break
    else:
        number = int(number)
        print("Divisors of the number 'number'",full_divisors(number))