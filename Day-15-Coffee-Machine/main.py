import art
import os


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
PENNY = .01
NICKEL = .05
DIME = .10
QUARTER  = .25

machine_money=0
choice=""

def clear_screen():
    """Clears the terminal screen across Windows, Mac, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def report():
    print(f"Total resources left\n"
          f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${machine_money:.2f}")
    return

def get_resources(coffee):
    """Gets resources for coffee."""
    water_needed = MENU[coffee]["ingredients"]["water"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    milk_needed = MENU[coffee]["ingredients"].get("milk", 0)
    return compare_resources(water_needed, coffee_needed, milk_needed)

#   TODO these greater than are wrong, change them
def compare_resources(water, coffee, milk):
    if int(resources['water']) >= water and int(resources['coffee']) >= coffee and int(resources['milk']) >= milk:
        return True
    else:
        print("Not enough resources")
        return False

def process_coins(coffee):
    penny = int(input("How many pennies did you insert?")) * PENNY
    nickel = int(input("How many nickels did you insert?")) * NICKEL
    dime = int(input("How many dimes did you insert?")) * DIME
    quarter = int(input("How many quarters did you insert?")) * QUARTER
    total_money = penny + nickel + dime + quarter
    if total_money >= MENU[coffee]['cost']:
        diff = total_money - MENU[coffee]['cost']
        total_money = MENU[coffee]['cost']
        print(f"{choice} costs: ${total_money:.2f}, refunded: ${diff:.2f} back to customer")
        sub_resources(coffee)
    else:
        print("Money refunded, not enough money")
        total_money = 0

    return total_money

def sub_resources(coffee):
    resources["water"] -= int(MENU[coffee]["ingredients"]["water"])
    resources["coffee"] -= int(MENU[coffee]["ingredients"]["coffee"])
    resources["milk"] -= MENU[coffee]["ingredients"].get("milk",0)



print(art.logo)

while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(f"{choice} selected")
        # Looks at amount of resources needed and calls compare resources to make sure there is enough to make the coffee
        if get_resources(choice):
            total_money = process_coins(choice)
            machine_money += total_money
            print(f"Total cost of {choice}: ${total_money:.2f} Total money in machine: ${machine_money:.2f}")
        else:
            print("Sorry, Please try again")
    elif choice == "off":
        clear_screen()
    elif choice == "report":
        report()
    else:
        print("Invalid Choice")