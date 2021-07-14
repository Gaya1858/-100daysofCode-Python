from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen( )
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
foods = Food()
scoreboard =Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while (game_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(foods) < 15:
        foods.new_pos()
        snake.extend()
        scoreboard.increase_score()
    if(snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_on =False
        scoreboard.game_over()
        if (game_on == False):
            with open("score.txt") as file2:
                x =int(file2.read())
            with open("score.txt", "w") as file1:
                if(scoreboard.score > x):
                    file1.write('\n%d' % scoreboard.score)
                else:
                    file1.write('\n%d' % x)


screen.exitonclick( )
