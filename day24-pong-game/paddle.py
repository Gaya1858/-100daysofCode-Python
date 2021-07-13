'''
paddle class- creates the paddle and taking care of the moves
'''
from turtle import Turtle

class Paddle(Turtle):
    MOVE =5

    def __init__(self, x, y):
        super( ).__init__( )
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(x,y)
    def rup(self):
        x = self.xcor()
        y = self.ycor()+20
        self.goto(x,y)
    def rdown(self):
        x = self.xcor( )
        y = self.ycor( ) -20
        self.goto(x, y)
    def lup(self):
        x = self.xcor( )
        y = self.ycor( ) + 20
        self.goto(x, y)
    def ldown(self):
        x = self.xcor( )
        y = self.ycor( ) - 20
        self.goto(x, y)