class Quiz:
    def __init__(self,ans,model):
        self.ans = ans
        self.model =model

    def check_answer(self):
        if(self.ans == self.model):
            print("You are correct.The answer is: ",self.model)
        else:
            print("You are wrong.The answer is: ", self.model)
