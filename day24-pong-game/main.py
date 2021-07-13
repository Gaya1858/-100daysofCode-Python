'''
Pong game
Main class works as a driver class and it generates the screen of the game.
'''

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen  = Screen()
screen.bgcolor("black")
screen.setup(width =800,height=600)
screen.title("Pong Game")
screen.tracer(0)

rpaddle = Paddle(350,0)
lpaddle= Paddle(-350,0)
ball =Ball()
scoreboard =Scoreboard()

screen.listen()
screen.onkey(rpaddle.rup,"Up")
screen.onkey(rpaddle.rdown,"Down")
screen.onkey(lpaddle.lup,"a")
screen.onkey(lpaddle.ldown,"z")



game_on =True
while game_on:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # detect collision with wall (ball bounce)
    if(ball.ycor() < -280 or ball.ycor() >280):
        ball.bounce_y()
    # detect collision with paddle and ball
    if( (ball.distance(rpaddle)) < 50 and ball.xcor() > 320) or(ball.distance(lpaddle)) < 50 and ball.xcor()<-320:
        ball.bounce_x()
        # Detect R paddle misses
    if ball.xcor( ) > 380:
        ball.reset()
        scoreboard.l_point()

        # Detect L paddle misses:
    if ball.xcor( ) < -380:
        ball.reset()
        scoreboard.r_point( )
    if scoreboard.rscore == 25 or scoreboard.lscore == 25:
        game_on =False
        scoreboard.game_over()

screen.exitonclick()