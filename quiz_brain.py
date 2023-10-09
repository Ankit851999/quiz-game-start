class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].text} "
                            f"(True/False): ").lower()
        question_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("you got it right")
        else:
            print(f"wrong answer .")
        print(f"The correct answer is {question_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
