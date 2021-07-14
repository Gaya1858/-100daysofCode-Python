from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super( ).__init__( )
        self.score = 0
        self.color("white")
        self.penup( )
        with open("score.txt") as file1:
            self.hscore =int(file1.read( ))
        self.goto(0, 270)
        self.update_score()
        self.hideturtle( )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}\t High Score: {self.hscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

