import turtle as tl
import random

# Initialize Turtle, setting background color, setting speed and pensize,
# Initialize color palette

turtle = tl.Turtle()
turtle.screen.bgcolor("light blue")
turtle.speed(3)
turtle.pensize(3)
color = ["green", "blue", "red", "orange", "yellow", "black", "violet"]

# snowflake variant 1 with random color

def snowflake1():

    i = 0
    while i < 10:
        turtle.color(random.choice(color))
        j = 0
        while j < 2:
            turtle.forward(200)
            turtle.right(60)
            turtle.forward(200)
            turtle.right(120)
            j = j + 1
        turtle.right(36)
        i = i + 1


# single branch for snowflake variant 2

def branch():
    i=0
    while i < 3:
        j=0
        while j < 3:
            turtle.forward(30)
            turtle.backward(30)
            turtle.right(45)
            j = j+1
        turtle.left(90)
        turtle.backward(30)
        turtle.left(45)
        i = i + 1
    turtle.right(90)
    turtle.forward(90)


# iterating 8 times over branch(), turning 45 degree everytime and changing color
def snowflake2():
    i=0
    while i < 8:
        turtle.color(random.choice(color))
        branch()
        turtle.left(45)
        i = i+1

# draw a lot of snowflakes, changing position randomly
def snowflakes():

    i=0
    while i < 15:
        snowflake2()
        turtle.penup()
        turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
        turtle.pendown()
        i = i+1


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