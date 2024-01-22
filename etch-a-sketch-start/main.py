from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(x=-230, y=-100 + (i * 45))

if user_bet:
    is_race_on = True

while is_race_on:

    for i in range(6):
        rand_distance = random.randint(0, 10)
        all_turtles[i].forward(rand_distance)
        if all_turtles[i].position()[0] >= 230:
            is_race_on = False
            winning_colour = all_turtles[i].pencolor()
            if winning_colour == user_bet:
                print(f"You win, the winner of the race is {winning_colour}")
            else:
                print(f"You lost, the winner of the race is {winning_colour}")


screen.exitonclick()
