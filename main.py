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
        print_report()

def print_report():
    """Prints the values of all resources on the Coffee Machine"""    
    print("Resource Level --------------------")
    print(f"Water: {water_level}")
    print(f"Milk: {milk_level}")
    print(f"Coffee: {coffee_level}")
    print(f"Money: {money_ammount}")

# Global variables
turn_off = False
water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
money_ammount = 0

# Main program
while not turn_off:
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    check_selection(selection)

