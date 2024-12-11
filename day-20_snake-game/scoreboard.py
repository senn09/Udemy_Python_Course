from turtle import Turtle
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        with open("data.txt") as txtdata:
            self.highscore = int(txtdata.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", 'w') as txtdata:
                txtdata.write(str(self.score))

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align="center", font=FONT)

