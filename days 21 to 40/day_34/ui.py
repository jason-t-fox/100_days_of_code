from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # variable here is an object
        self.current_score = 0

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.quiz_score = Label(text=f"Score: {self.current_score}/10")
        self.quiz_score.config(bg=THEME_COLOR, fg="white", font=("Ariel", 10), padx=20, pady=20)
        self.quiz_score.grid(row=0, column=1)

        self.question_canvas = Canvas(height=250, width=300)
        self.updatable_q = self.question_canvas.create_text(150, 125,
                                                            text="question",
                                                            font=("Ariel", 18, "italic"),
                                                            width=270)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(command=self.check_button_press)
        self.check_button.config(image=check_img,
                                 highlightthickness=0,
                                 relief="flat",
                                 borderwidth=0,
                                 padx=20,
                                 pady=20)
        self.check_button.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button(command=self.x_button_press)
        self.x_button.config(image=x_img,
                             highlightthickness=0,
                             relief="flat",
                             borderwidth=0,
                             pady=20,
                             padx=20)
        self.x_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions() is True:
            q_text = self.quiz.next_question()  # method calling method within object, complex!
            self.question_canvas.itemconfig(self.updatable_q, text=q_text)
            self.quiz_score.config(text=f"Score: {self.current_score}/10")
        else:
            self.quiz_score.config(text=f"Final Score: {self.current_score}/10")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def x_button_press(self):
        answer = "false"
        return_value = self.quiz.check_answer(answer)
        self.get_next_question()
        if return_value is True:
            self.current_score += 1

    def check_button_press(self):
        answer = "true"
        return_value = self.quiz.check_answer(answer)
        self.get_next_question()
        if return_value is True:
            self.current_score += 1
