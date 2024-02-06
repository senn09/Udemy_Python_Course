from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50)

        self.score_text = Text()
        self.score_text.insert(END, "Hello")
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(300, 250, text="title", font=("Arial", 40, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()