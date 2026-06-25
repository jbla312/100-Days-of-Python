class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ{self.question_number}: {curr_question.question_text} (True/False)?:").lower()
        self.check_answer(answer)

    def check_answer(self, answer_text):
        curr_question = self.question_list[self.question_number - 1]
        if answer_text == curr_question.answer_text.lower() or answer_text.lower()[0] == curr_question.answer_text.lower()[0]:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"Correct answer: {curr_question.answer_text}")
        print(f"{self.score}/{self.question_number}")

    def more_questions(self):
        return self.question_number < len(self.question_list)