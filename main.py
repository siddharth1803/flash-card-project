from tkinter import *
import pandas
import random

current_card = {}

try:
    word_list = pandas.read_csv("data/word_to_learn.csv", encoding="utf-8")
except FileNotFoundError:
    word_list = pandas.read_csv("data/hindi_words.csv", encoding="utf-8")
words = word_list.to_dict(orient="records")


def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(foreign_text_word, text=current_card.get("text_hindi"), fill="black")
    canvas.itemconfig(foreign_text, text="hindi", fill="black")
    canvas.itemconfig(canvas_image, image=image)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(foreign_text_word, text=current_card.get("text"), fill="white")
    canvas.itemconfig(foreign_text, text="english", fill="white")
    canvas.itemconfig(canvas_image, image=new_image)


def is_known_word():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/word_to_learn")
    generate_random_word()


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = ("Ariel", 40, "italic")
LANGUAGE_TEXT = ("Ariel", 40, "bold")

window = Tk()
window.title("Flashy Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
foreign_text = canvas.create_text(400, 100, text="", font=LANGUAGE)
foreign_text_word = canvas.create_text(400, 263, text="", font=LANGUAGE_TEXT)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, pady=50, command=is_known_word)
right_button.grid(column=0, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, padx=50, command=generate_random_word)
wrong_button.grid(column=1, row=1)

generate_random_word()
window.mainloop()
