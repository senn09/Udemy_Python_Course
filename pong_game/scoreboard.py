from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.teleport(x= 0, y= 260)
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def update_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score} | {self.right_score}", False, "center", ("Arial", 16, "normal"))
