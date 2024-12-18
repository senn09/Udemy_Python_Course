from turtle import Turtle

FONT = ("Arial", 8, "normal")

class Game_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def display_state(self, state_data):
        pos = (state_data[1], state_data[2])
        state = state_data[0]
        self.goto(pos)
        self.write(state, False, "center", FONT)
