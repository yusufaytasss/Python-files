import turtle
obj = turtle.Turtle()
obj.speed(0)
obj.pencolor("yellow")

win = turtle.Screen()
win.bgcolor("black")
win.title("Next codes")
f = 0
r = 0
obj.up()
obj.goto(0,200)
obj.down()
while(1):
    obj.forward(f)
    obj.right(r)
    f+=3
    r+=1
    if r >= 200:
        break
    obj.hideturtle()
    turtle.done
    
print("Hello world")
print("Selamlar")