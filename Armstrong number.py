number = input("Number :")
Number_of_digits = len(number)
number = int(number)
step = 0
total = 0

temporary_number = number

while(temporary_number > 0):
    
    step = temporary_number % 10
    
    total += step ** Number_of_digits
    
    temporary_number //= 10
    
if (total == number):
    print(number," is an armstrong number.")
else:
    print(number," isn't armstrong number.")