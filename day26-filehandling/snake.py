'''
Snake game
this snake class will make sure all snake movements

'''
from turtle import Turtle

SEGMENTS =[(0,0),(-10,0),(-20,0)]
MOVE =10

class Snake():
    def __init__(self):
        self.seg =[]
        for i in range(0,len(SEGMENTS)):
            new_turt = Turtle()
            new_turt.penup()
            x_pos =SEGMENTS[i][0]
            y_pos =SEGMENTS[i][1]
            new_turt.shapesize(0.5,0.5)
            new_turt.goto(x_pos,y_pos)
            new_turt.shape("square")
            new_turt.color("white")
            self.seg.append(new_turt)
        self.head =self.seg[0]

    def move(self):
        for i in range(len(self.seg)-1,0,-1):
            x_seg = self.seg[i-1].xcor()
            y_seg = self.seg[i-1].ycor()
            self.seg[i].goto(x_seg,y_seg)
        self.head.forward(MOVE)


    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)
        self.seg[0].setheading(270)
    def left(self):
        if self.head.heading( ) !=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading( ) !=180:
            self.head.setheading(0)
    def extend(self):
        #add a segment
        self.add_seg()
    def add_seg(self):
        new_turt = Turtle( )
        new_turt.penup( )
        x_pos = self.seg[-1].xcor()
        y_pos = self.seg[-1].ycor()
        new_turt.shapesize(0.5, 0.5)
        new_turt.goto(x_pos, y_pos)
        new_turt.shape("square")
        new_turt.color("white")
        self.seg.append(new_turt)