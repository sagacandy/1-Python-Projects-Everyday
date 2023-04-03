import os
import art

print(art.gavel)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


dict = []


def auction(n, b):
    data = {
        "bidders_name": n,
        "bidding_amount": b
    }
    dict.append(data)


while True:
    print("Welcome to the secret auction program")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction(name, bid)
    others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if others != "yes":
        break
    else:
        clear()

# finding the highest bid
highest_bid = max(dict, key=lambda x: x['bidding_amount'])

print("\n\nBidding has ended. The winner is {} with a bid of ${}.".format(
    highest_bid['bidders_name'], highest_bid['bidding_amount']))
