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
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resouce_sufficient(order_ingredents):
    for item in order_ingredents:
        if order_ingredents[item] >= resources[item]:
            print(f"sorry there is ot enough {item}")
            return False
    return True


while True:
    choice = input("What do you like to have?(espresso/latte/cappuccino)\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resouce_sufficient(drink["ingredients"]):
            print("enjoy your coffee")
