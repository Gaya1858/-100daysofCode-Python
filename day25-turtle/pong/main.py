import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player =Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
screen.onkey(player.right_p,"l")
screen.onkey(player.left_p,"r")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.start_move()
    # detect collision with cars
    for car in car_manager.cars:
        if(car.distance(player) < 20):
            game_is_on =False
            scoreboard.game_over()
    if player.is_at_finish_line():
        scoreboard.add_score()
        player.go_to_start()


screen.exitonclick()



