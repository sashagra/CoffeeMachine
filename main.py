from menu import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def discover_resources(menu):
    resources_available = {}
    for drink in menu:
        resources_available[drink] = True
        for item in menu[drink]["ingredients"]:
            if menu[drink]["ingredients"][item] > resources[item]:
                resources_available[drink] = False
    for drink in resources_available:
        if resources_available[drink]:
            return resources_available
        else:
            return False


def fl_text(available_list):
    text = ""
    for item in available_list:
        if available_list[item]:
            text = text + item + "/"
    return text[0:-1]


def input_and_check_coins(drink):
    total_pay = 0
    attempts = 3
    while True:
        p = int(input('pennies: '))
        n = int(input('nickles: '))
        d = int(input('dimes: '))
        q = int(input('quarters: '))
        total_pay = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
        if total_pay >= drink["cost"]:
            print("Take your drink")
            return
        else:
            print("It's not enough money. You should add something")
            if attempts > 0:
                attempts -= 1
            else:
                print("Something went wrong. Maybe you have not money? Then back later")
                return False


available_drinks = discover_resources(MENU)

if not available_drinks:
    print("Sorry. The machine not have needful ingredients. Back again later")
else:
    while True:
        answer = input(f"What would you like? ({fl_text(available_drinks)}): ").lower()

        try:
            if not available_drinks[answer]:
                print("Not enough ingredients")
            else:
                input_and_check_coins(MENU[answer])
                break
        except KeyError:
            print("It's not right answer!")

    print("Good choice")
