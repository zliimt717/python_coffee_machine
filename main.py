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

# TODO: 1. Print report of all coffee machine resources


def print_report(money):
    for key in resources:
        if key == "coffee":
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: {resources[key]}ml")
    print(f"Money: ${money}")


def is_sufficient(coffee_type):
    sufficient=True
    for key in coffee_type["ingredients"]:
        if resources[key] < coffee_type["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            sufficient =False
            break
    return sufficient


def calculate_coin():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    return quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01


def make_coffee(coffee_type):
    for key in coffee_type["ingredients"]:
        resources[key] = resources[key] - coffee_type["ingredients"][key]

    return resources


money = 0
is_the_end = False
while not is_the_end:
    chosen = input("What would you like? (espresso/latte/cappuccino)")
    if chosen == "report":
        print_report(money)
    else:
        drink = MENU[chosen]
        #is_sufficient("espresso")
        if is_sufficient(drink):
            sum = calculate_coin()
            if sum < drink["cost"]:
                money = 0
                print("Sorry that's not enough money. Money refunded.")
            else:
                money = round(sum - drink["cost"],2)
                make_coffee(drink)
                print(f"Here is ${money} in change.")
                print(f"Here is your {chosen}. Enjoy.")

        else:
            is_the_end = True
