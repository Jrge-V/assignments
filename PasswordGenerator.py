#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# initialize a list in order to use the shuffle function
password = []
for let in range(0, nr_letters):
    # use the choice function in order to pick a random letter from the lists above
    password.append(random.choice(letters))
for sym in range(0, nr_symbols):
    password.append(random.choice(symbols))
for num in range(0, nr_numbers):
    password.append(random.choice(numbers))

# shuffle function to shuffle randomly (only used on lists, not string)
random.shuffle(password)

# initiate a new string for randomized password
randomize_pass = ""
for char in password:
    randomize_pass += char

print(f"\nYour new password is: {randomize_pass}")
