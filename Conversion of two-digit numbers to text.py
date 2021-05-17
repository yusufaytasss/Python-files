number = int(input("Please enter a two-digit number"))
if(number <= 99):
    ones_digits = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    tens_digits = ["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eightyt","Ninety"]
    
    def translate(number):
        first_digit = number % 10
        second_digit = number // 10
        return tens_digits[second_digit] + " " + ones_digits[first_digit]
    print(translate(number))
else:
    print("The numerical value you enter is not a number between 1 and 100")