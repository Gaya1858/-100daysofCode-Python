'''
colorgram.py
pip install colorgram.py
'''
import colorgram
import turtle as t
import random


def draw_dots(turt,row,col,colors):
    for i in range(0,row):

        for j in range(0,col):

            x =random_color(colors)
            turt.fillcolor(x)
            turt.begin_fill()
            turt.pencolor(x)
            turt.pendown()
            turt.speed(10)
            turt.circle(5)
            turt.end_fill( )
            turt.penup()
            turt.forward((30))
        turt.backward(30*col)
        turt.left(90)
        turt.forward(30)
        turt.right(90)


def random_color(colors):
    ran = random.randint(0,len(colors)-1)
    return colors[ran].rgb
# Extract 6 colors from an image.
colors =colorgram.extract("image.jpg",15)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34
turt = t.Turtle()

t.colormode(255)
my_screen =t.Screen()
draw_dots(turt,15,15,colors)
my_screen.exitonclick()

