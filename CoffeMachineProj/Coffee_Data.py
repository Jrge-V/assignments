import argparse
import sys


def parse_text_data(resource_data_read):
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", dest="resourceData", help="Pass resource data to be read")
    args = parser.parse_args()

    if args.resourceData is None:
        print("No resource Data has been passed")
        sys.exit()

    with open(args.resourceData, 'r') as file:
        parsed_data = file.read().splitlines()

    for i in range(len(parsed_data)):
        parsed_data[i] = parsed_data[i].split(" ")[2]

    resource_data_read = {
        "water": int(parsed_data[0]),
        "milk": int(parsed_data[1]),
        "coffee": int(parsed_data[2]),
        "money": float(parsed_data[3])
    }

    return resource_data_read





MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


COINS = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01
}

