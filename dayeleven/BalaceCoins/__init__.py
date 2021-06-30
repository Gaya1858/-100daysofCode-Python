'''
this class keeps track of the user coins balances
'''

def give_initial_coin():
    player_bal = 5000
    return player_bal

def player_balance_add(initial,bet):
    player_bal =initial+bet
    return player_bal

def player_balance_subtract(initial,bet):
    player_bal = initial - bet
    return player_bal

def balance_check(balance,bet):
    if(balance -bet >=0):
        return True
    else:
        return False

