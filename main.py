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
# TODO: 2. Check resources are sufficient to make drink order

# Functions
def check_selection(selection):
    """Checks user user selection"""
    if selection == "espresso":
        print("Espresso")
    elif selection == "latte":
        print("Latte")
    elif selection == "cappuccino":
        print("Cappuccino")
    elif selection == "off":
        globals()["turn_off"] = True
        print("Switching off the coffee machine...")
    elif selection == "report":
        print("Report:")

# Global variables
turn_off = False

# Main program
while not turn_off:
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    check_selection(selection)

