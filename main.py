from menu import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
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
    """Ask for payment with coins and check if money enough"""
    attempts = 3
    total_pay = 0
    while True:
        print(f"It costs ${drink['cost']}. Insert the coins")
        p = int(input('pennies: '))
        n = int(input('nickles: '))
        d = int(input('dimes: '))
        q = int(input('quarters: '))
        total_pay += round((q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01), 2)
        if total_pay >= drink["cost"]:
            return total_pay
        else:
            print(f"You insert ${total_pay} but it's not enough. You should add something to ${drink['cost']}")
            if attempts > 0:
                attempts -= 1
            else:
                print("Something went wrong. Maybe you have not money? Then back later")
                return False


def give_the_drink(drink, res):
    for item in drink["ingredients"]:
        res[item] -= drink["ingredients"][item]
    res["money"] += drink["cost"]
    print("Take your drink")
    return res


is_on = True

while is_on:
    available_drinks = discover_resources(MENU)

    if not available_drinks:
        print("Sorry. The machine not have needful ingredients. Back again later")
        break
    else:
        while True:
            choice = input(f"What would you like? ({fl_text(available_drinks)}): ").lower()
            if choice == "off":
                is_on = False
                break
            elif choice == "report":
                print(f"Resources: {resources}")
                break
            try:
                if not available_drinks[choice]:
                    print("Not enough ingredients")
                else:
                    payment = input_and_check_coins(MENU[choice])
                    if payment:
                        if payment > MENU[choice]['cost']:
                            change = round((payment - MENU[choice]['cost']), 2)
                            print(f"Your change is ${change}")
                        resources = give_the_drink(MENU[choice], resources)
                    break
            except KeyError:
                print("It's not right answer!")

print("Bye, bye!")
