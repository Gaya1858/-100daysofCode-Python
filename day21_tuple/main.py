'''
tuple:
immutable
douplicates are not allowed
usage : where you create list of items which is going to be constant
'''
import turtle
from turtle import Turtle, Screen
import random

def recursive_circle(radious,trut):

    if(radious >0):

        turt.pencolor(random_color())

        turt.circle(radious)
        radious = radious - 10
        recursive_circle(radious, turt)

    else:
        turt.color("pink")
        turt.shape("turtle")

def random_color():
    r =random.randint(0,255)
    g= random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple =(r,g,b)
    return color_tuple

turt = Turtle()
turtle.colormode(255)
my_screen = Screen()
for i in range(0,8):
    recursive_circle(100, turt)
    turt.left(45)

my_screen.exitonclick()