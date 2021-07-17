'''
Blackjack card game
This game will be played by one player and the computer
user will give 5000 coins initially to play
minimum bet would 500 coins and max would be 5000coins
player has options of "stand" ,"hit","double(hit and doublt the bet)"
player can see one of the first two cards value of the computer
'''
from dayeleven.BalaceCoins import give_initial_coin, player_balance_subtract, player_balance_add
from dayeleven.BlackJack import card_player, sum_list, card_system, player_hit, card_comp, system_hit

print("Welcome to BlackJack game!")
print("two cards will be revealed for player and one card of the system: ")
print("Player has option to 'stand', 'hit' or 'double'")
print("Player will be given 5000 initial coins to play")
print("Lets begin!")

def choice_one():
    hit_list =[]
    hit_list = player_hit()
    print("Your cards: ", hit_list[0], hit_list[1],hit_list[2], "Total: ", sum_list(hit_list))
    if (sum_list(hit_list) > 21):
        print("You lost!")
        return 0
    elif ((sum_list(hit_list) == 21 and sum_list(card_comp) != 21) or sum_list(card_comp)>21):
        print("You won!")
        return 1

    elif sum_list(card_comp) == 21 and sum_list(hit_list) != 21 :
        print("Computer: ", card_comp[0], card_comp[1])
        print("computer won!")
        print("You lost!")
        return 2
    elif sum_list(card_comp) == 21 and sum_list(hit_list) == 21:
        print("Match draw! ")
        return 3
    else:
        return 4
def choice_two():
    hit_list =[]
    hit_list = system_hit( )
    print("Your cards: ", hit_list[0], hit_list[1], hit_list[2], "Total: ", sum_list(hit_list))
    if (sum_list(hit_list) <21):
        hit_list = system_hit( )
        print("Your cards: ", hit_list[0], hit_list[1], hit_list[2],hit_list[3], "Total: ", sum_list(hit_list))
        if(sum_list(hit_list)< sum_list(card_player())):
            print("You lost!")
            return 0
        else:
            print("you won!")
            return 1

    else:
        print("you won!")
        return 1



continue_play = True
user_balance =give_initial_coin()
print("Your balance is: ",user_balance)
while(continue_play):
    player_cards = card_player()
    player_bet = int(input("Enter your bet amount: "))
    print("Your cards: ", player_cards[0],player_cards[1],"Total: ",sum_list(player_cards))
    computer_card = card_system()
    print("Computer card: ", computer_card[0], "| |")
    if(sum_list(player_cards)<21):
        while (sum_list(player_cards) < 21):
            player_decision = int(input("Choose 1 for stand,2 for hit: "))
            if (player_decision == 1):
                if (choice_one( ) == 0):
                    user_balance = player_balance_subtract(user_balance, player_bet)
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False
                elif (choice_one( ) == 1):
                    user_balance = player_balance_add(user_balance, player_bet)
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False
                elif (choice_one( ) == 2):
                    user_balance = player_balance_subtract(user_balance, player_bet)
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False
                elif choice_one( ) == 3:
                    user_balance = user_balance
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False
                elif choice_one( ) == 4:
                    continue_play =True
            if(player_decision ==2):
                if(choice_two() ==0):
                    user_balance = player_balance_subtract(user_balance, player_bet)
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False
                else:
                    user_balance = player_balance_add(user_balance, player_bet)
                    print("Your balance is: ", user_balance)
                    play_re = input("do you want to continue: y or n")
                    if (play_re == "y"):
                        continue_play = True
                    else:
                        continue_play = False


    else:
        print("You lost!")
        user_balance = player_balance_subtract(user_balance, player_bet)
        print("Your balance is: ", user_balance)
        play_re = input("do you want to continue: y or n")
        if (play_re == "y"):
            continue_play = True
        else:
            continue_play = False







