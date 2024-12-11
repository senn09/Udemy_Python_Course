import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(0)
tim.pensize(2)
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)
def drawCircle(num_circles):
    angle =  360/ num_circles
    tim.color(random_colour())
    tim.circle(100,)
    tim.right(angle)

def drawShape(turtle, num_sides, length):
    angle = 360 / num_sides

    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(angle)


# for num_sides in range(3, 100):
#     drawShape(tim, num_sides, 20)

num_circles = 70
for _ in range(num_circles):
    drawCircle(num_circles)

screen = Screen()
screen.exitonclick()
