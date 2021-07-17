'''
Rock papper scissors game
'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Papper and Scissors game!\n")
user_input= int(input("Please enter 1 for rock, 2 for paper and 3 for scissors:\n"))
random_game = random.randint(1,3)
list_game =[rock,paper,scissors]
if(random_game == user_input):
    print("Computer: \n")
    print(list_game[user_input-1])
    print("You: \n")
    print(rock)
    print("Kudos!!!")
else:
    print("Computer: \n")
    print(list_game[random_game-1])
    print("You: \n")
    print(list_game[user_input - 1])
    print("Better Luck Next Time!")