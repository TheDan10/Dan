import turtle
import sys
thisModule = sys.modules[__name__]

wn = turtle.Screen()
wn.window_width()
wn.screensize(720,1080)# make a graphics windows to draw in
tom = turtle.Turtle()
tom.hideturtle()# create a turtle called tom
wn.listen()

style = ('Courier', 15, 'italic')
tom.write('Hello! Welcome to my drawing program have fun :)  except spas\n'
          'Press C to clear and get started', font=style, align='center')

thisModule.isWelcomeScreenOpen = True


def clear():
    tom.reset()

def isTheWelcomeScreenVisable():
    if thisModule.isWelcomeScreenOpen :
        clear()
        thisModule.isWelcomeScreenOpen = False

def triangle():
    isTheWelcomeScreenVisable()
    for a in range (3):
        tom.forward(100)
        tom.right(120)

def square():
    isTheWelcomeScreenVisable()
    for a in range(4):
        tom.forward(100)
        tom.right(90)

def printWarning():
    tom.write('Get out of here with that shit key press', font=style, align='center')

wn.textinput("NIM", "Name of first player:")
wn.onkeypress(triangle,"t")
wn.onkeypress(square,"s")
wn.onkeypress(clear,"c")
wn.onkeypress(printWarning)

wn.exitonclick()
