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

# Global variables
turn_off = False
water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
money_ammount = 0

# Functions
def check_selection(selection):
    """Checks user user selection"""
    if selection == "espresso":
        if (check_resources_sufficient(selection)):
            print("Making an espresso")
    elif selection == "latte":
        if (check_resources_sufficient(selection)):
            print("Making a latte")
    elif selection == "cappuccino":
        if (check_resources_sufficient(selection)):
            print("Making a cappuccino")
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

def check_resources_sufficient(selection):
    """Checks the resources of user's selection"""
    def print_out_of_resources(resource):
        """Prints the out of resources message"""
        print(f"Sorry, there is not enough {resource}")

    if water_level < MENU[selection]["ingredients"]["water"]:
        print_out_of_resources("water")
        globals()["turn_off"] = True
    elif selection != "espresso" and milk_level < MENU[selection]["ingredients"]["milk"]:
        print_out_of_resources("milk")
        globals()["turn_off"] = True
    elif coffee_level < MENU[selection]["ingredients"]["coffee"]:
        print_out_of_resources("coffee")
        globals()["turn_off"] = True
    else:
        return True
    

# Main program
while not turn_off:
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    check_selection(selection)

