from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
    question_bank.append(new_question)
#print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print("\n")
print(f"you have completed the quiz\n"
      f"your final score is: {quiz.score}")


