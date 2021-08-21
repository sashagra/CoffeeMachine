from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    available_drinks = menu.get_items(coffee_maker.resources)
    if available_drinks is None:
        sleep(3)
        print("Sorry. The machine not have needful ingredients. Back again later")
        sleep(5)
        break
    else:
        while True:
            choice = input(f"What would you like? Available: ({available_drinks}): ").lower()

            if choice == "off":
                is_on = False
                print()
                break
            elif choice == "report":
                coffee_maker.report()
                money_machine.report()
                break
            else:
                drink = menu.find_drink(choice)
                if drink and coffee_maker.is_resource_sufficient(drink):
                    is_successful_payment = money_machine.make_payment(drink.cost)
                    if is_successful_payment:
                        coffee_maker.make_coffee(drink)
                break

print("Bye, bye!")
