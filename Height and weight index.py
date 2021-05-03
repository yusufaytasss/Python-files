length = float(input("Please a enter length :")) #The reason we entered 'float' is because height and weight can be numbers with decimals.
weight = float(input("Please a enter weight :"))

hwi = weight / (length ** 2)

if (hwi < 18.5):
    print("Skinny : {} ".format(hwi))
elif (hwi >= 18.5 and hwi < 25):
    print("Normal : {} ".format(hwi))
elif (hwi >= 25 and hwi < 30):
    print("Overweight : {} ".format(hwi))
else:
    print("Obese : {} ".format(hwi))