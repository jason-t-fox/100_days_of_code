class QuizBrain:

    def __init__(self, q_list):
        self.currently_asked_question = None
        self.question_number = 0
        self.question_list = q_list
        self.user_answer = ""
        self.user_score = 0

    def still_has_questions(self):
        """Returns 'True' if there are still unasked questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Ask the next question"""
        self.currently_asked_question = self.question_list[self.question_number]
        self.user_answer = input(f"Q.{self.question_number + 1}: {self.currently_asked_question.text} (True/False)?: ")
        self.question_number += 1
        if self.check_answer(self.user_answer, self.currently_asked_question.answer) is True:
            self.user_score += 1
        print(f"Your current score is: {self.user_score} out of {self.question_number}.\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            return True
        else:
            print(f"Incorrect! The correct answer was {correct_answer}")
            return False
