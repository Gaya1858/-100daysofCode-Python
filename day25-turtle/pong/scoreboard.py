FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Black")
        self.penup( )
        self.goto(0, 280)
        self.update_score( )
        self.hideturtle( )
        self.update_score()

    def update_score(self):
        self.write(self.score,align="center",font =FONT)
    def add_score(self):
        self.clear()
        self.score +=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("YOU LOST", align="center", font=FONT)


