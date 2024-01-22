from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_GAP = 60

LEFT_PADDLE_X = -SCREEN_WIDTH/2 + PADDLE_GAP
RIGHT_PADDLE_X = SCREEN_WIDTH / 2 - PADDLE_GAP

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_X)
right_paddle = Paddle(RIGHT_PADDLE_X)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
#left paddle
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

#right paddle
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.move()

    #wall collision
    if ball.ycor() > SCREEN_HEIGHT/2 - 15 or ball.ycor() < -SCREEN_HEIGHT/2 + 15:
        ball.update_y_dir()

    #paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() < LEFT_PADDLE_X + 25 or ball.distance(right_paddle) < 50 and ball.xcor() > RIGHT_PADDLE_X - 25:
        ball.update_x_dir()

    #score
    if ball.xcor() < -SCREEN_WIDTH/2 + 10:
        scoreboard.update_right_score()
        ball.reset_ball()
    if ball.xcor() > SCREEN_WIDTH/2 - 10:
        scoreboard.update_left_score()
        ball.reset_ball()

screen.exitonclick()
