'''
No internet so just making up some coding practice
recursive functions
'''
from turtle import Turtle, Screen
def recursive_circle(radious,trut):
    col  =["red","violet","blue","orange","navy","purple","green","black","grey"]
    if(radious >0):
        x = radious%len(col)
        turt.pencolor(col[x])
        turt.fillcolor(col[x])
        turt.circle(radious)
        radious = radious - 10
        recursive_circle(radious, turt)

    else:
        turt.color("pink")
        turt.shape("turtle")

turt = Turtle()
my_screen = Screen()
for i in range(0,8):
    recursive_circle(100, turt)
    turt.left(45)

my_screen.exitonclick()