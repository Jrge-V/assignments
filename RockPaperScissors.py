import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
print("Welcome to the classic Rock, Paper, Scissors game!")
choice = ""

while choice != "q":

    choice = input("You can type 'rock', 'paper', or 'scissors' to begin, or 'q' to exit: ").lower()
    num = random.choice(game)

    if choice == "rock":
        print(num)
        if num == game[0]:
            print("It's a TIE!, go again")
        elif num == game[1]:
            print("You lose!")
            break
        else:
            print("You Win!")
            break

    elif choice == "paper":
        print(num)
        if num == game[0]:
            print("You Win!")
            break
        elif num == game[1]:
            print("It's a TIE!, go again")
        else:
            print("You lose!")
            break
    elif choice == "scissors":
        print(num)
        if num == game[0]:
            print("You lose!")
            break
        elif num == game[1]:
            print("You Win!")
            break
        else:
            print("It's a TIE!, go again")

print("\nThank You For Playing!")