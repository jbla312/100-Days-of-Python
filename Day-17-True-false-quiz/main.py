from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

score = 0
question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
answer = quiz.next_question()
while quiz.more_questions():
    answer = quiz.next_question()

print("Quiz Completed")
print(f"Final score: {quiz.score}/{quiz.question_number}")