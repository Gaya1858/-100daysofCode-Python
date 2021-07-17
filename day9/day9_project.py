'''
Blind action project
people can enter their name and bid amount
this program will show the highest bidder name and bid amount
'''

import art


bidding ={}
def bidder_detail(name,bid_amount):
    bidding[name]=bid_amount

def highest_bid():
    max_bid =0
    max_bid_name =""
    for bid in bidding:
        if(bidding[bid] > max_bid):
            max_bid =bidding[bid]
            max_bid_name =bid
    print("The higest bid amount is: ",max_bid, " and the name of the person is: "+max_bid_name)

print(art.logo)
choice = input("do you want to bid? say yes or no: ").lower()

while( choice != "no"):
    user_name = input("Please enter youe name:  ")
    user_bid = int(input("Please enter your bid amount: "))
    bidder_detail(user_name, user_bid)
    choice = input("do you want to bid? say yes or no: ").lower( )

highest_bid()