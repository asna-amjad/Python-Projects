from replit import clear
from art import logo
print(logo)

# find the highest bid in dictionary
def find_max_bid(bidding_log):
    highest_bid = 0
    for bidder in bidding_log:
        bid_price = bidding_log[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder

    print(f"THe winner is {winner} with a bid price of {highest_bid}")

bidding_log = {}

continue_bid = True

while continue_bid:
    name = input("Enter your name?: ")
    bid = int(input("Enter your bid price: "))
    bidding_log.update({name: bid})

    other_users = input("Do you have another user? 'yes' or 'no': ").lower()
    if other_users == "no":
        continue_bid = False
        find_max_bid(bidding_log)
    elif other_users == "yes":
        print("\n" * 20)
        #clear()
