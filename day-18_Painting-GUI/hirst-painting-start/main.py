import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

colour_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
dot_size = 20
gap = 50

t = Turtle()
t.hideturtle()

def startPos():
    draw_size = 9 * gap
    t.penup()
    start_x = - (draw_size/2)
    start_y = - (draw_size/2)
    t.setpos(start_x, start_y)

def draw_row():
    t.setheading(0)
    t.dot(dot_size, random.choice(colour_list))
    for _ in range(9):
        t.forward(gap)
        t.dot(dot_size, random.choice(colour_list))

def next_row():
    t.setheading(90)
    t.forward(gap)
    t.setheading(180)
    t.forward(gap*9)


startPos()
print(t.screen.canvwidth)
print(t.screen.canvheight)
for _ in range (10):
    draw_row()
    next_row()

screen = Screen()
screen.exitonclick()