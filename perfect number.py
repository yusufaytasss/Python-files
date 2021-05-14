number = int(input("Please enter a number :"))
i = 1
total = 0
while(i < number):
    if (number % i == 0):
        total += i
    i += 1
    
if (total == number):
    print(number," is a perfect number.")
else:
    print(number," it is not a perfect number.")
