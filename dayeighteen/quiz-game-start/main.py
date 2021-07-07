
from question_model import Question
from quiz_brain import Quiz

print("Welcome to True/False game!")
print("You will be shown a question and you have to answer True/T or False/F ")
print("Let us start!")
print("\n")
quiz = Question()
print("Your question is: ")
print(quiz.text)
answer = input("Please enter your answer: ")
check =Quiz(answer,quiz.answer)
check.check_answer()


