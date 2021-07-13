'''
scoreboard keeps tracks of the score .

paddler can get a score of 1 when the otehr paddler misses the ball
'''

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore =0
        self.rscore =0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update()


    def update(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.lscore, align="center", font=("Courier", 50, "normal"))
        self.goto(150, 200)
        self.write(self.rscore, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.lscore +=1
        self.update()

    def r_point(self):
        self.rscore += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align ="center",font =("Courier", 30, "normal"))