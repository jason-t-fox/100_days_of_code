from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    test_word_df = pd.read_csv("data/known_words.csv")
except FileNotFoundError:
    test_word_df = pd.read_csv("data/french_words.csv")
test_word_dict = test_word_df.to_dict(orient="records")
random_row = {}


def choose_test_word():
    global random_row, timer
    screen.after_cancel(timer)
    random_row = random.choice(test_word_dict)
    french_word = random_row["French"]
    card_canvas.itemconfig(test_word_title, text="French", fill="black")
    card_canvas.itemconfig(test_word_text, text=french_word, fill="black")
    card_canvas.itemconfig(canvas_image, image=card_front_img)
    screen.after(3000, func=turn_card_over)


def turn_card_over():
    global random_row
    english_word = random_row["English"]
    card_canvas.itemconfig(test_word_title, text="English", fill="white")
    card_canvas.itemconfig(test_word_text, text=english_word, fill="white")
    card_canvas.itemconfig(canvas_image, image=card_back_img)


def card_is_known():
    test_word_dict.remove(random_row)
    choose_test_word()
    known_words = pd.DataFrame(test_word_dict)
    known_words.to_csv("data/known_words.csv", index=False)


screen = Tk()
screen.title("Flashy, The Flash Card App")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = screen.after(3000, func=turn_card_over)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
check_img = PhotoImage(file="images/right.png")
x_img = PhotoImage(file="images/wrong.png")

card_canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
canvas_image = card_canvas.create_image(400, 263, image=card_front_img)
card_canvas.config(highlightthickness=0, relief="flat", borderwidth=0)
test_word_title = card_canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
test_word_text = card_canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

x_button = Button(command=choose_test_word)
x_button.config(image=x_img, highlightthickness=0, relief="flat", borderwidth=0)
x_button.grid(row=1, column=0)

check_button = Button(command=card_is_known)
check_button.config(image=check_img, highlightthickness=0, relief="flat", borderwidth=0)
check_button.grid(row=1, column=1)

choose_test_word()

screen.mainloop()
