import Art
import os
import sys
import random


def welcome_message():
    play = input("Welcome to Blackjack, would you like to play? Type 'y' to continue or 'n' to exit: ")
    if play == 'y':
        os.system('cls')
        print(Art.logo)
        initialize_game()
    elif play == 'n':
        print("Hope to see you soon!")
        sys.exit()
    else:
        welcome_message()


def initialize_game():
    add_card_user()
    add_card_user()
    add_card_dealer()
    current_score()


def add_card_user():
    user_cards.append(random.choice(cards))


def add_card_dealer():
    dealer_cards.append(random.choice(cards))


def current_score():
    print(f"\nYour hand is: {user_cards}, current score: {sum(user_cards)}")
    print(f"The Dealers hand is: {dealer_cards}, current score: {sum(dealer_cards)}")

    if sum(user_cards) > 21:
        print("You Lose.")
        sys.exit()

    if sum(dealer_cards) > 21 or sum(user_cards) == 21:
        print("You Win!")
        sys.exit()

    if sum(dealer_cards) < 17 and len(dealer_cards) > 1:
        add_card_dealer()
        current_score()


def hit_stand(con_flag):
    if hit_or_stand == 'y':
        add_card_user()
        current_score()

    elif hit_or_stand == 'n':
        add_card_dealer()
        current_score()
        con_flag = False

    return con_flag


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

welcome_message()
continue_flag = True

while continue_flag:
    hit_or_stand = input("Would you like to HIT or STAND? Type 'y' to HIT or 'n' to STAND: ")
    continue_flag = hit_stand(continue_flag)


if sum(user_cards) > sum(dealer_cards):
    print("You Win!")
elif sum(user_cards) < sum(dealer_cards):
    print("You Lose.")
else:
    print("IT'S A DRAW!")
