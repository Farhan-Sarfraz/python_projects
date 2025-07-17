
bids = {}
bidding_finished = False
def find_highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner} with highest bid price ${highest_bid}")

while not bidding_finished:
#  taking input name and bidding price
    name = input("what is name ? ")
    price = int(input("what is your bid price ? $"))
    bids[name] = price
    should_continue = input("is there any bidders ? type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif bidding_finished == "yes":
        exit()
