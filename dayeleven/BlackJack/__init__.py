'''
This class will provide supporting function for the blackjack game
# will create players cards
# will create blackjackist cards
# will create hit card
# will create jackist card max number 4 until it reaches 21 or more.
'''
import random

jack_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def card_player():
    card_one = random.randint(0,len(jack_list))
    card_two = random.randint(0,len(jack_list))
    card1 =jack_list[card_one]
    card2 =jack_list[card_two]
    return card1,card2

def card_system():
    card_one = random.randint(0,len(jack_list))
    card_two = random.randint(0,len(jack_list))
    card1 =jack_list[card_one]
    card2 =jack_list[card_two]
    return card1,card2

def player_hit():
    card_one = random.randint(0, len(jack_list))
    card1 = jack_list[card_one]
    return card1
