figure = input("Which type of shape would you like to learn? : \n")

if (figure == "Quadrilaterals"):
    print("Please enter the edges one by one.")
    a = int(input("Edge-one :"))
    b = int(input("Edge-two :"))
    c = int(input("Edge-tri :"))
    d = int(input("Edge-for :"))
    
    if (a == b and a == c and a == d):
        print("Square")
    elif (a == c and b == d):
        print("Rectangle")
    else:
        print("Geometric quadrilateral")

elif (figure == "Triangle"):
    a = int(input("Edge-one :"))
    b = int(input("Edge-two :"))
    c = int(input("Edge-tri :"))
    if (abs (a+b) > c and abs (a+c) > b and abs (b+c) > a):
        if (a == b and a == c):
            print("Equilateral triangle...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Isosceles Triangle ....")
        else:
            print("A triangle is not specified...")
else:
    print("Invalid Figure ...")