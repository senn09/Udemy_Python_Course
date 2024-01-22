from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def remove_card():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card_canvas.itemconfig(card_side, image=card_front_image)
    flash_card_canvas.itemconfig(card_title, text="French", fill="Black")
    flash_card_canvas.itemconfig(card_text, text=current_card["French"], fill="Black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    flash_card_canvas.itemconfig(card_side, image=card_back_image)
    flash_card_canvas.itemconfig(card_title, text="English", fill="White")
    flash_card_canvas.itemconfig(card_text, text=current_card["English"], fill="White")

# ------------------- Grab CSV Data -----------------
try:
    data = pandas.read_csv('data/words_to_learn.csv')
    print("words_to_learn")
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    print("french_words")
to_learn = data.to_dict(orient="records")

# -------------------- UI Setup --------------------
window = Tk()
window.title("French to English Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash card

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
flash_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = flash_card_canvas.create_image(400, 263, image=card_front_image)
card_title = flash_card_canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_text = flash_card_canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
flash_card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_card)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()



window.mainloop()

