from turtle import Turtle

DIRECTION = (45, 135, 225, 315)



class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.color("red")
        self.setheading(DIRECTION[0])
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def update_x_dir(self):
        self.x_move *= -1

    def update_y_dir(self):
        self.y_move *= -1

    def reset_ball(self):
        self.teleport(x=0, y=0)
        self.x_move *= -1
        self.y_move *= -1
