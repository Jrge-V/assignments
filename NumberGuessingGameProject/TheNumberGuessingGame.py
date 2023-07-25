import random
import Art


def how_difficult():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return diff


def guess(att, ran_num):

    while att != 0:
        print(f"You have {att} attempts remaining to guess a number.")
        user_guess = int(input("Make a guess: "))

        if user_guess < ran_num:
            print("Too Low.\nTry again.")
        elif user_guess > ran_num:
            print("Too High.\nTry again.")
        else:
            print(f"Congrats, the number was {ran_num}. You guessed it with {att} attempt(s) left!")
            break
        att -= 1

    if att == 0:
        print(f"Game Over. The number was {ran_num}.\nBetter luck next time!")


print(Art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
rng = random.randint(1, 100)

difficulty = ""
while difficulty != "easy" and difficulty != "hard":
    difficulty = how_difficult()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

guess(attempts, rng)
