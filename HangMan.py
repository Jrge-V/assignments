import random

def guessed_word():
    user_guess = input(f"Guess a letter: ").lower()
    return user_guess


def replaced_word():
    i = 0
    while i < len(chosen_word):
        if guess == chosen_word[i]:
            blank_list[i] = guess
        i += 1
    print(blank_list)


def lose_life():
    lives_left = lives - 1
    return lives_left

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("Welcome to Hangman!")


blank_list = []

for letter in chosen_word:
    blank_list.append("_")

while lives != 0:
    guess = guessed_word()
    if guess in chosen_word:
        print(f"\n{guess} was found!")
        replaced_word()
        if "_" not in blank_list:
            print("You Win!")
            break

    else:
        print(f"{guess} is not in the word")
        replaced_word()
        lives = lose_life()
        print(stages[lives])
        if lives == 0:
            print("You Lose!")
            break
