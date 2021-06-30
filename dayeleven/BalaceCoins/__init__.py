'''
this class keeps track of the user coins balances
'''
player_balance = 5000


def give_initial_coin():
    player_bal = player_balance
    return player_bal


def player_balance_add(initial, bet):
    add_bet = initial + bet
    player_balance = add_bet
    return add_bet


def player_balance_subtract(initial, bet):
    player_bal = initial - bet
    player_balance =player_bal
    return player_bal


def balance_check(balance, bet):
    if (balance - bet >= 0):
        return True
    else:
        return False
