'''
This class will provide supporting function for the blackjack game
# will create players cards
# will create blackjackist cards
# will create hit card
# will create jackist card max number 4 until it reaches 21 or more.
'''
import random

jack_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
card_player =[]
card_comp =[]

def card_player():
    card_player1 =[]
    card_one = random.randint(0,len(jack_list))
    card_two = random.randint(0,len(jack_list))
    card_player1.append(jack_list[card_one])
    card_player1.append(jack_list[card_two])
    card_player =card_player1

    return card_player

def card_system():
    card_comp1 =[]
    card_one = random.randint(0,len(jack_list))
    card_two = random.randint(0,len(jack_list))
    card_comp1.append(jack_list[card_one])
    card_comp1.append(jack_list[card_two])
    card_comp =card_comp1
    return card_comp

def player_hit():
    card_player1 =[]
    card_one = random.randint(0, len(jack_list))
    card_player1.append(jack_list[card_one])
    card_player2 = card_player+card_player1
    return card_player2

def system_hit():
    card_comp1 =[]
    card_one = random.randint(0, len(jack_list))
    card_comp1.append(jack_list[card_one])
    card_comp2 =card_comp+card_comp1
    return card_comp2

def check_jack():
    i =sum_list(card_player)
    if(i < 21):
        return 0
    elif i==21:
        return 1
    else:
        return 3
def sum_list(lists):
    sum = 0
    for i in lists:
        sum += i
    return sum
def stand_jack():
    if len(card_comp) ==2:
        sum = sum_list(card_comp)
        if(sum <21):
            system_hit()
            sum = sum_list(card_comp)
            if(sum <=21 and sum_list(card_player)> sum):
                return 1
            else:
                return 0


