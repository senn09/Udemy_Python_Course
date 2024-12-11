COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        self.tick = 0

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        rand_ycor = random.randrange(-250, 260, 30)
        # test
        car.goto(280, rand_ycor)
        car.setheading(180)
        self.cars.append(car)

    def move(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
                print(f"len(self.cars) {len(self.cars)}")

    def generate_cars(self):
        self.tick += 1
        if self.tick == 10:
            generate = random.randint(0,1)
            if generate:
                num_cars = random.randint(1, 4)
                for _ in range(num_cars):
                    self.create_car()
            self.tick = 0




