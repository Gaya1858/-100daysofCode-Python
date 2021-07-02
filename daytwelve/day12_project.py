'''
number guessing game
easy level, player will get 10 guesses and
hard level, player will get 5 guesses to find the number
'''
import random
def hard_level(guess):
    rand_num =random_num()
    print(rand_num)
    guesss =1
    userGuess = int(input(f"Please guess your {guesss} guess: "))
    result = False
    while(guesss < guess):
        guesss += 1
        if(userGuess == rand_num):
            guesss =guess
            result = True
            print(f"Your guess {rand_num} is correct")
        elif (userGuess <rand_num):
            print(" Your gusss is lower than then actual number: ")
            userGuess = int(input(f"Please guess your {guesss} guess: "))
        elif (userGuess >rand_num):
            print("Your gusss is greater than then actual number: ")
            userGuess = int(input(f"Please guess your {guesss} guess: "))

    if(result == False):
        print(f"You are finished all your {guesss} gusses.")



def random_num():
    rand_num = random.randint(1,101)
    return rand_num


print("Welcome to number guessing game!")
print("Easy level you get get 10 guesses to find the number and Hard level you get only 5 guesses to find the number.")
level = int(input("Please choose level: hard level choose and for 1 and easy level choose 2 "))
result =True
while(result):
    if (level == 1):
        hard_level(5)
        choice_continue = input("Do you continue to play? 'y'-yes or 'n'-no: ")
        if (choice_continue == 'y'):
            level = int(input("Please choose level: hard level choose and for 1 and easy level choose 2 "))
        else:
            result =False
    elif (level == 2):
        hard_level(10)
        choice_continue = input("Do you continue to play? 'y'-yes or 'n'-no: ")
        if (choice_continue == 'y'):
            level = int(input("Please choose level: hard level choose and for 1 and easy level choose 2 "))
        else:
            result =False


