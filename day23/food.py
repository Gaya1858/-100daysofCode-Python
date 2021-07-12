from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("purple")
        self.speed("fastest")
        self.new_pos()

    def new_pos(self):
        x_pos = random.randint(-260,260)
        y_pos = random.randint(-260,260)
        self.goto(x_pos,y_pos)

    def clear(self):
        self.clear()

