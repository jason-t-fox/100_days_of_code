from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):


        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.quiz_score = Label(text="Score: 0")
        self.quiz_score.config(bg=THEME_COLOR, fg="white", font=("Ariel", 10), padx=20, pady=20)
        self.quiz_score.grid(row=0, column=1)

        self.question_canvas = Canvas(height=250, width=300)
        self.updatable_q = self.question_canvas.create_text(150, 125,
                                                            text="question",
                                                            font=("Ariel", 20, "italic"),
                                                            width=260)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button()
        self.check_button.config(image=check_img,
                                 highlightthickness=0,
                                 relief="flat",
                                 borderwidth=0,
                                 padx=20,
                                 pady=20)
        self.check_button.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button()
        self.x_button.config(image=x_img,
                             highlightthickness=0,
                             relief="flat",
                             borderwidth=0,
                             pady=20,
                             padx=20)
        self.x_button.grid(row=2, column=1)

        self.window.mainloop()
