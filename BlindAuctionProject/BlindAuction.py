import Art
import os


def add_bidders():
    curr_name = str(input("What is your name?: ")).capitalize()
    curr_bid = int(input("What's your bid?: $"))
    all_bidders[curr_name] = curr_bid
    more_bidders()


def more_bidders():
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidders == "yes":
        clear_console()
        add_bidders()
    elif bidders == "no":
        clear_console()
        highest_bidder()
    else:
        more_bidders()


def highest_bidder():
    sorted_bidders = sorted(all_bidders.items(), key=lambda x: x[1], reverse=True)
    print(f"The winner is {sorted_bidders[0][0]} with a bid of ${sorted_bidders[0][1]}")


def clear_console():
    os.system('cls')


all_bidders = {}
print(Art.logo)
print("Welcome to the secret auction game program.")
add_bidders()
