
##  EventListener :
''' turtle has an object that listens user's keyboard actions
create a sceen object
screen.listen()
screem.onkey(key ="useraction", function)
key = it takes whatever user hits in the keyboard will be saved likt space, a letter and so on
function = based on the key, function will be executed
'''
##Higher order function - a function that works with other functions
'''passing function inside the function is called higher order function.
A function is called Higher Order Function if it contains other functions as a parameter or
 returns a function as an output i.e, the functions that operate with another function are known
 as Higher order Functions. ... Python too supports the concepts of higher order functions
'''
# Etch a sketch program

import turtle as t

turt =t.Turtle()
my_screen =t.Screen()


def draw_forward():
    turt.forward(10)
def draw_backward():
    turt.backward(10)
def draw_left():
    #turt.left(10) ---- same as setheading
    new_heading =turt.heading() +10
    turt.setheading(new_heading)
def draw_right():
    # turt.right(10) ---- same as setheading
    new_heading = turt.heading( ) -10
    turt.setheading(new_heading)
def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


my_screen.listen()
my_screen.onkey(draw_forward,'w')
my_screen.onkey(draw_backward,'s')
my_screen.onkey(draw_left, 'a')
my_screen.onkey(draw_right,'d')
my_screen.onkey(draw_right,'c')

my_screen.exitonclick()
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
#
# screen.exitonclick()