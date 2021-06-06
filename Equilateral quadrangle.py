def p(n):
    # Upper star triangle
    for i in range(n):
        print((n-i-1)*" ", end="")
        print((2*i+1)*"*")
    # lower star triangle
    for i in range(n-1, -1 , -1):
        print((n-1-i)*" ", end="")
        print((2*i+1)*"*")
p(5)