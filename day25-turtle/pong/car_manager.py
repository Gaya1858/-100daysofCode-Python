
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        head = random.randint(1,6)
        if(head ==1):
            ran = random.randint(-250, 250)
            new_car =Turtle("square")
            new_car.shapesize(2,1)
            new_car.shape("square")
            new_car.shapesize(2, 1)
            new_car.color(random.choice(COLORS))
            new_car.penup( )
            new_car.goto(300, ran)
            self.cars.append(new_car)


    def move_car(self):
       for car in self.cars:
           car.backward(MOVE_INCREMENT)

    def start_move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT