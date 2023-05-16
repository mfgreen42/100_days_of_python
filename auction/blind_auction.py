from art import logo
import os

# from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)
print('The silent auction is about to start.... ')

keep_going = True
final_bids = {}


def find_highest_value():
    highest_bid = 0
    for bidder in final_bids:
        bid_amount = final_bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is: {winner} with a bid of ${highest_bid}")
while keep_going:
 

    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    final_bids[name] = bid
    more_bids = input("Are there more bids to enter? yes or no  ")
    if more_bids == "yes":
        os.system('cls')
        

    else:
        keep_going = False
        find_highest_value()


