import turtle as tl
import random

turtle = tl.Turtle()
turtle.screen.bgcolor("light blue")
turtle.speed(20)
turtle.pensize(3)
color = ["green", "blue", "red", "orange", "yellow", "black", "violet"]


def snowflake1():

    for i in range(10):
        turtle.color(random.choice(color))
        for i in range(2):
            turtle.forward(200)
            turtle.right(60)
            turtle.forward(200)
            turtle.right(120)
        turtle.right(36)

def branch():

    for i in range(3):
        for i in range(3):
            turtle.forward(30)
            turtle.backward(30)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(30)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(90)

def snowflake2():
    for i in range(8):
        turtle.color(random.choice(color))
        branch()
        turtle.left(45)


def snowflakes():

    for i in range(15):
        snowflake2()
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.pendown()



var = int(input("Wähle Variante 1, 2 oder 3: "))

if var == 1:
    snowflake1()
elif var == 2:
    snowflake2()
elif var == 3:
    snowflakes()
else:
    print("not an option")