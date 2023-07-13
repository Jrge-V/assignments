import Art
import os


def new_calc():
    curr_n = int(input("What's the first number?: "))
    op = input("+\n-\n*\n/\nPick an operation: ")
    next_n = int(input("What's the next number?: "))

    return curr_n, op, next_n

def continue_calc():
    op = input("+\n-\n*\n/\nPick an operation: ")
    next_n = int(input("What's the next number?: "))

    return op, next_n

def operation(op, curr_n, next_n):
    if op == "+":
        return curr_n + next_n
    elif op == "-":
        return curr_n - next_n
    elif op == "*":
        return curr_n * next_n
    else:
        return curr_n / next_n


print(Art.logo)

curr_num, oper, next_num = new_calc()

result = operation(oper, curr_num, next_num)

print(f"{curr_num} {oper} {next_num} = {result}")

choice = "y"



while choice == "y" or choice == "n":
    choice = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type any other key to exit: ")

    if choice == "y":
        oper, next_num = continue_calc()

        curr_num = result

        operation(oper, curr_num, next_num)
        result = operation(oper, curr_num, next_num)
        print(f"{curr_num} {oper} {next_num} = {result}")

    elif choice == "n":
        os.system('cls')
        curr_num, oper, next_num = new_calc()
        result = operation(oper, curr_num, next_num)
    else:
        print("Now Exiting...")
