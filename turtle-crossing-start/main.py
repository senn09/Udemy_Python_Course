import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

def check_collision(player, cars):
    for car in cars:
        print(f"player.ycor() {player.ycor()} car.ycor() {car.ycor()} player.distance(car) {player.distance(car)}")
        if player.ycor() + 30 > car.ycor() and player.distance(car) < 37:
            return True
    return False

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    if check_collision(player, car_manager.cars):
        print("Collision detected")
        scoreboard.game_over()
        game_is_on = False

    if player.reached_end():
        player.reset_pos()
        scoreboard.update_level()

    car_manager.generate_cars()
    car_manager.move(scoreboard.level)

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
