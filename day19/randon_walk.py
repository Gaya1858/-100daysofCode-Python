import random
from turtle import Turtle, Screen
from randonG import RandomNumber

class RandomWalk:

    def __init__(self):
        self.turt =Turtle()
        self.mscreen =Screen()
        self.mscreen.canvwidth=800
        self.mscreen.canvheight=800
        self.turt.color("red")
        self.turt.pencolor("blue")
        self.turt.shape("turtle")
        self.tpw = 0
        self.tph = 0

        print("position",self.turt.pos())

    def walk(self):

        while((self.turt.pos()[0] >=-400 and self.turt.pos()[0] <=400) and(self.turt.pos()[1] >=-400 and self.turt.pos()[1] <=400) ):
           self.step()



    def step(self):
        rn = RandomNumber()
        move = rn.get_coin()

        if (move == 0):
            self.turt.right(90)
            self.turt.forward(50)
            self.tph -=50

            print("position", self.turt.pos( ))
        elif move ==1:
            self.turt.left(90)
            self.turt.forward(50)
            self.tph += 50

            print("position", self.turt.pos( ))



r =RandomWalk()
r.walk()
r.mscreen.exitonclick()
