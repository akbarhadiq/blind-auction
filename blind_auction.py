# HINT: You can call clear() to clear the output in the console.

import os
import art

bidder_exist = True
print(art.logo)
bids = {

}
while bidder_exist:

    os.system("cls")
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: $"))

    bids[name] = bid

    is_still_bidding = input("Are there any other bidder? (Y/N) :").lower()
    if is_still_bidding == "y":
        bidder_exist = True
    elif is_still_bidding == "n":
        bidder_exist = False
    else:
        print("You've got a wrong input, please enter correctly (Y/N)")
        print("Bid terminated!")
        bidder_exist = False

# Ends Here

highest_bidder = ""
highest_bid = 0

for name in bids:
    if bids[name] > highest_bid:
        highest_bidder = name
        highest_bid = bids[name]

print(f"The Winner of the auction is {highest_bidder}, with ${highest_bid} amount of bid")
