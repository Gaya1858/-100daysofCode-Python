'''
ball.py
creates a ball and controls the ball's movement
'''

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup( )
        self.xmove =3
        self.ymove =3
        self.moveSpeed =0.05


    def move(self):
        x = self.xcor( ) + self.xmove
        y = self.ycor( ) + self.ymove
        self.goto(x,y)

    def bounce_y(self):
        self.ymove  *= -1

    def bounce_x(self):
        self.xmove  *= -1
        self.moveSpeed *= 0.45

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.bounce_x( )