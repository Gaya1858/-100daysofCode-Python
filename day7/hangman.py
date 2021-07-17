'''
    Hangman game
    using loops and conditional, logic satements
'''
hangman = '''
                 ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |        /Y . . Y\
        | |       // |   | \\
        | |      //  | . |  \\
        | |     ')   |   |   (`
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \
        """"""""""|_`-' `-' |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :  sk
        . .          `'       . .

'''

import random

def guess_word(word):
      word_l =list(word)
      print(word)
      word1 ="-"*len(word)
      word1_l =list(word1)
      print(word1)
      life = 3
      check =0
      count =len(word)
      while count>0:
            u_guess = input("Please guess letter: \n")
            x =0
            guess=""
            for ch in word_l:
                  if (ch == u_guess):
                        word1_l[x] =word_l[x]
                        check +=1
                        count -=1
                  else:
                        if x == len(word)-1 :
                              if(check ==0):
                                    life -=1
                                    print("you have ", life, "left")
                                    if(life ==0):
                                          print(hangman)
                  x +=1
            for i in word1_l:
                  guess +=i
            print(guess)







word_list =["which","there","their","about","would","these","other","words","could"]


print("Welcome to Hangman game!\n")
print("This game will show a word with blank characters and ask you to guess a letter."
      "You will have 3 lifes and each failed guess will take off your a life."
      "All the best!")
random_word = random.randint(0, len(word_list))
guess = word_list[random_word]
guess_word(guess)
print("You won the game!!!\n")
