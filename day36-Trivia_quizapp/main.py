
from quiz import Quiz

quiz = Quiz()
mark =0
count=0

quiz_on = True
while(quiz_on):
    quiz.show_quiz()
    userAns = input("").upper()
    ans=quiz.answer
    count+=1
    if(userAns[0] == ans[0]):
        mark =mark+1
        print(f"You are correct! Your score is {mark}")
        play = input("Do you want to continue? (Y/N)").upper()
        if(play == "Y"):
            quiz_on = True
        else:
            quiz_on = False


    else:
        print(f"You are wrong! Your score is {mark}")
        play = input("Do you want to continue? (Y/N)").upper()
        if(play == "Y"):
            quiz_on = True
        else:
            quiz_on = False
    if(count ==10):
        print("You have completed the quiz!")
        quiz_on=False




