from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def do_nothing(self):
        pass
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score = 0", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=self.true_image, command=lambda: self.check_answer("true"))
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=self.false_image, command=lambda: self.check_answer("false"))
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def check_answer(self, answer):
        is_right = self.quiz.check_answer(answer)
        if(is_right):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score = {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")