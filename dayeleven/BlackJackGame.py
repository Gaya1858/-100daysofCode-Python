'''
Blackjack card game
This game will be played by one player and the computer
user will give 5000 coins initially to play
minimum bet would 500 coins and max would be 5000coins
player has options of "stand" ,"hit","double(hit and doublt the bet)"
player can see one of the first two cards value of the computer
'''
from dayeleven.BalaceCoins import give_initial_coin, balance_check, player_balance_subtract, player_balance_add
from dayeleven.BlackJack import card_player, card_system, player_hit, system_hit


def blackjack_play_one(blackJack_total_player,blackJack_total_computer):
    player_hit1 = player_hit( )
    blackJack_total_player += player_hit1
    print(player_card, player_hit1, "\tTotal is: ", blackJack_total_player)
    if (blackJack_total_player > 21):
        print("You lost!")
        return 0
    elif (blackJack_total_player == 21 and blackJack_total_computer != 21) or blackJack_total_computer>21:
        print("You won!")
        return 1

    elif blackJack_total_computer == 21 and blackJack_total_player!= 21:
        print("Computer: ", computer_card[0], computer_card[1])
        print("computer won!")
        print("You lost!")
        return 2
    else:
        player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))
        if(player_decision ==1):
            player_hit2 = player_hit()
            blackJack_total_player += player_hit2
            print(player_card, player_hit1, player_hit2,"\tTotal is: ", blackJack_total_player)
            return hit2_player(blackJack_total_player)



def blackJack_system(blackJack_total_player,blackJack_total_computer):
    computer =system_hit()
    blackJack_total_computer += computer
    print(computer_card[0],computer_card[1],computer)
    if(blackJack_total_computer <blackJack_total_player ):
        computer2 =system_hit()
        blackJack_total_computer+=computer2
        print(computer_card[0], computer_card[1], computer,computer2)
        if(blackJack_total_computer>blackJack_total_player and blackJack_total_computer <=21):
            player_balance_subtract(user_bal, player_bet)
            print("You lost!")
            return 0
        else:
            player_balance_add(user_bal, player_bet)
            print("You won!")
            return 1


def hit2_player(blackJack_total_player):
    if (blackJack_total_player > 21):
        print("You lost!")
        return 0
    elif (blackJack_total_player == 21 and blackJack_total_computer != 21) or blackJack_total_computer > 21:
        print("You won!")
        return 1

    elif blackJack_total_computer == 21 and blackJack_total_player != 21:
        print("Computer: ", computer_card[0], computer_card[1])
        print("computer won!")
        print("You lost!")
        return 2
    else:
        hit2_player(blackJack_total_player)






print("Welcome to BlackJack game!")
print("two cards will be revealed for player and one card of the system: ")
print("Player has option to 'stand', 'hit' or 'double'")
print("Player will be given 5000 initial coins to play")
print("Lets begin!")
user_bal = give_initial_coin( )
print("Your balance is : ", user_bal)
print("*************************************************************************")

continue_play = True
while(continue_play):
    player_card = card_player()
    player_bet = int(input("Enter your bet amount: "))
    print("Your cards: ", player_card)
    blackJack_total_player = player_card[0] + player_card[1]
    print("your sum is: ", blackJack_total_player)
    computer_card = card_system()
    print("Computer card 1: ", computer_card[0], "| |")
    blackJack_total_computer = computer_card[0] + computer_card[1]

    player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))
    if(player_decision ==1 and balance_check(user_bal,player_bet)):
        replay =blackjack_play_one(blackJack_total_player,blackJack_total_computer)
        if(replay ==0):
            play_re = input("do you want to continue: y or n")
            user_bal =player_balance_subtract(user_bal,player_bet)
            if(play_re =='y'):
                print("your balance is: ",user_bal)

            else:
                continue_play =False
        elif(replay ==1):
            play_re = input("do you want to continue: y or n")
            user_bal = player_balance_add(user_bal, player_bet)
            if (play_re == 'y'):
                print("your balance is: ", user_bal)
                player_bet = int(input("Enter your bet amount: "))
                player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))
            else:
                continue_play = False
        elif (replay == 2):
            play_re = input("do you want to continue: y or n")
            user_bal = player_balance_subtract(user_bal, player_bet)
            if (play_re == 'y'):
                print("your balance is: ", user_bal)
                player_bet = int(input("Enter your bet amount: "))
                player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))
            else:
                continue_play = False
        elif(replay ==3):
            player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))

    elif (player_decision ==2 and balance_check(user_bal,player_bet)):
        replay =blackJack_system(blackJack_total_player,blackJack_total_computer)
        if (replay == 0):
            play_re = input("do you want to continue: y or n")
            user_bal = player_balance_subtract(user_bal, player_bet)
            if (play_re == 'y'):
                print("your balance is: ", user_bal)
                player_bet = int(input("Enter your bet amount: "))
                player_decision = int(input("Choose 1 for stand,2 for hit and 3 for double: "))
            else:
                continue_play = False














