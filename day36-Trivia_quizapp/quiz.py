'''
all about quiz
show quiz,
check answer
show answer
'''
from trivia import Trivia
import random
class Quiz:
    def __init__(self):
        self.create_quizfile()
        self.previous=[]
    def create_quizfile(self):
        tr =Trivia()
        quiz_dict =tr.trivia_file
        self.ques=[]
        self.ans=[]
        for (i,j) in quiz_dict.items():
            self.ques.append(i)
            self.ans.append(j)

    def show_quiz(self):

        ran_quiz = random.randint(0,len(self.ques)-1)

        while(ran_quiz in self.previous):
            ran_quiz = random.randint(0,len(self.ques)-1)

        self.previous.append(ran_quiz)
        print(self.previous)

        self.question =self.ques[ran_quiz]
        self.answer =self.ans[ran_quiz]
        print(f"{self.question} True/False?")

