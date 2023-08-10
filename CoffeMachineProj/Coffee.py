import Coffee_Data


def coffee_prompt(user_coffee_choice):
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return user_coffee_choice


def espresso():
    resources['water'] -= menu['espresso']['ingredients']['water']
    resources['coffee'] -= menu['espresso']['ingredients']['coffee']
    resources['money'] += menu['espresso']['cost']
    print("Your espresso is ready. Hope to see you soon!")


def latte():
    resources['water'] -= menu['latte']['ingredients']['water']
    resources['milk'] -= menu['latte']['ingredients']['milk']
    resources['coffee'] -= menu['latte']['ingredients']['coffee']
    resources['money'] += menu['latte']['cost']
    print("Your latte is ready. Hope to see you soon!")


def cappuccino():
    resources['water'] -= menu['cappuccino']['ingredients']['water']
    resources['milk'] -= menu['cappuccino']['ingredients']['milk']
    resources['coffee'] -= menu['cappuccino']['ingredients']['coffee']
    resources['money'] += menu['cappuccino']['cost']
    print("Your cappuccino is ready. Hope to see you soon!")


def report():
    print("REPORT")
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def process_coins():

    if ask_user_coffee_choice == "espresso":
        coffee_cost = menu['espresso']['cost']
    elif ask_user_coffee_choice == "latte":
        coffee_cost = menu['latte']['cost']
    else:
        coffee_cost = menu['cappuccino']['cost']

    client_money = 0.0
    remaining_coffee_cost = coffee_cost

    while True:
        if client_money < coffee_cost:
            print(f"Remaining amount: ${remaining_coffee_cost}")
            user_coin_choice = input("Please choose 'quarters', 'dimes', 'nickels', or 'pennies': ").lower()

            if user_coin_choice == "quarters":
                number_of_coins = int(input("How many quarters would you like to insert?: "))
                current_client_money = coins['quarters'] * number_of_coins
                client_money += coins['quarters'] * number_of_coins
                remaining_coffee_cost -= current_client_money
                remaining_coffee_cost = round(remaining_coffee_cost, 2)

            elif user_coin_choice == "dimes":
                number_of_coins = int(input("How many dimes would you like to insert?: "))
                current_client_money = coins['dimes'] * number_of_coins
                client_money += coins['dimes'] * number_of_coins
                remaining_coffee_cost -= current_client_money
                remaining_coffee_cost = round(remaining_coffee_cost, 2)

            elif user_coin_choice == "nickels":
                number_of_coins = int(input("How many nickels would you like to insert?: "))
                current_client_money = coins['nickels'] * number_of_coins
                client_money += coins['nickels'] * number_of_coins
                remaining_coffee_cost -= current_client_money
                remaining_coffee_cost = round(remaining_coffee_cost, 2)

            elif user_coin_choice == "pennies":
                number_of_coins = int(input("How many pennies would you like to insert?: "))
                current_client_money = coins['pennies'] * number_of_coins
                client_money += coins['pennies'] * number_of_coins
                remaining_coffee_cost -= current_client_money
                remaining_coffee_cost = round(remaining_coffee_cost, 2)

        elif client_money > coffee_cost:
            client_money -= coffee_cost
            client_money = round(client_money, 2)
            print(f"Transaction complete. Refunding ${client_money}.")
            break
        elif client_money == coffee_cost:
            print("Transaction complete.")
            break


def turn_off():
    print("Coffee Machine is now offline. :)")

    # Saves the resources left over after program has exited.
    text_file_save = open(".\CoffeMachineProj\Resource_Data.txt", "w")
    updated_entry = [
        f"WATER = {resources['water']}\n",
        f"MILK = {resources['milk']}\n",
        f"COFFEE = {resources['coffee']}\n",
        f"MONEY = {resources['money']}\n",
    ]

    text_file_save.writelines(updated_entry)
    text_file_save.close()


# stores the dictionary for the coffee info
resources = Coffee_Data.parse_text_data({})
menu = Coffee_Data.MENU
coins = Coffee_Data.COINS

while True:
    ask_user_coffee_choice = coffee_prompt("")

    while ask_user_coffee_choice != "espresso" and ask_user_coffee_choice != "latte" and ask_user_coffee_choice != "cappuccino" and ask_user_coffee_choice != "off" and ask_user_coffee_choice != "report":

        ask_user_coffee_choice = coffee_prompt("")

    if ask_user_coffee_choice == "espresso":
        if resources['water'] < menu['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < menu['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            process_coins()
            espresso()

    elif ask_user_coffee_choice == "latte":
        if resources['water'] < menu['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['milk'] < menu['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        elif resources['coffee'] < menu['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            process_coins()
            latte()

    elif ask_user_coffee_choice == "cappuccino":
        if resources['water'] < menu['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['milk'] < menu['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        elif resources['coffee'] < menu['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            process_coins()
            cappuccino()

    elif ask_user_coffee_choice == "report":
        report()
    elif ask_user_coffee_choice == "off":
        turn_off()
        break
