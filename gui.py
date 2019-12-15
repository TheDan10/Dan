import turtle
wn = turtle.Screen()    # make a graphics windows to draw in
tom = turtle.Turtle()   # create a turtle called tom

def square(length):
    for a in range (4):
        tom.forward(length)
        tom.right(120)

def square2(length):
    for a in range(10):
        tom.forward(length)
        tom.right(10)

def square3(length):
    for a in range (4):
        tom.forward(length)
        tom.right(100)


square(10)
square(20)
square(30)
square(40)
square(50)
square(60)
square(70)
square(80)
square(90)
square(100)
square(110)
square(120)
square(130)
square(140)
square(150)
square(160)
square(170)
square(180)
square(190)
square(200)

square2(10)
square2(20)
square2(30)
square2(40)
square2(50)
square2(60)
square2(70)
square2(80)
square2(90)
square2(100)
square2(110)
square2(120)
square2(130)
square2(140)
square2(150)
square2(160)
square2(170)
square2(180)
square2(190)
square2(200)



wn.exitonclick()
