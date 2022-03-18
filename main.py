from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["Spanish"]
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=back_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# ------------------------UI----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# --------------------------text------------------------------#

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Button

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=is_known)
right_button.config(highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=next_word)
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=0, row=1)

next_word()

window.mainloop()
