import data
import random

class Question:

    def __init__(self):
        ran = random.randint(0,len(data.question_data)-1)
        question_set =data.question_data[ran]
        self.text = question_set["text"]
        self.answer= question_set["answer"]




