from turtle import Turtle

MOVE_DIST = 60

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(x=x_pos, y=0)

    def up(self):
        same_x = self.xcor()
        new_y = self.ycor() + MOVE_DIST
        self.teleport(x=same_x, y= new_y)

    def down(self):
        same_x = self.xcor()
        new_y = self.ycor() - MOVE_DIST
        self.teleport(x=same_x, y= new_y)
