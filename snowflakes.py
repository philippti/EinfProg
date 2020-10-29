import turtle as tl
import random

# Initialize Turtle, setting background color, setting speed and pensize,
# Initialize color palette

turtle = tl.Turtle()
turtle.screen.bgcolor("light blue")
turtle.speed(10)
turtle.pensize(3)
color = ["green", "blue", "red", "orange", "yellow", "black", "violet"]

# snowflake variant 1 with random color

def snowflake1():

    for i in range(10):
        turtle.color(random.choice(color))
        for i in range(2):
            turtle.forward(200)
            turtle.right(60)
            turtle.forward(200)
            turtle.right(120)
        turtle.right(36)

# single branch for snowflake variant 2

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

# iterating 8 times over branch(), turning 45 degree everytime and changing color
def snowflake2():
    for i in range(8):
        turtle.color(random.choice(color))
        branch()
        turtle.left(45)

# draw a lot of snowflakes, changing position randomly
def snowflakes():

    for i in range(15):
        snowflake2()
        turtle.penup()
        turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
        turtle.pendown()


# asking the user which variant of snowflake he wants to see drawn:

var = int(input("Wähle Variante 1, 2 oder 3: "))

if var == 1:
    snowflake1()
elif var == 2:
    snowflake2()
elif var == 3:
    snowflakes()
else:
    print("not an option")