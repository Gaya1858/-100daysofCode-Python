from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def right_p(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)
    def left_p(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def is_at_finish_line(self):
        if self.ycor( ) > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARTING_POSITION)