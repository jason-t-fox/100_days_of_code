from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  # This lesson is about using classes, but the alternative is a lambda function
for question in question_data:
    q_text = question['text']
    a_text = question['answer']
    new_question = Question(question_text=q_text, answer_text=a_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was {quiz.user_score} out of {quiz.question_number}.")