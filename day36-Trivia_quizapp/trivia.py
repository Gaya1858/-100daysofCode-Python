'''
this class will create dictionary of trivia question and answers

'''
import requests
import json
class Trivia:
    def __init__(self):
        self.response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
        self.response.raise_for_status()
        self.data =self.response.json()["results"]
        self.trivia_dict()
    def trivia_dict(self):
        self.trivia_file= {ques["question"]:ques["correct_answer"] for ques in self.data}


