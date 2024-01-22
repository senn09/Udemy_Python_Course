from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.head = self.snakebody[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def extend(self):
        self.add_segment((self.snakebody[-1].position()))

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.pencolor("white")
        segment.goto(position)
        self.snakebody.append(segment)

    def reset(self):
        for seg in self.snakebody:
            seg.goto(1000, 1000)
        self.snakebody.clear()
        self.create_snake()
        self.head = self.snakebody[0]


    def move(self):
        for seg_num in range(len(self.snakebody) - 1, 0, -1):
            new_x = self.snakebody[seg_num - 1].xcor()
            new_y = self.snakebody[seg_num - 1].ycor()
            self.snakebody[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
