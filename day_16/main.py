from menu import Menu  # , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

machine_running = True

while machine_running:
    options = coffee_maker_menu.get_items()
    user_selection = input(f"What would you like? ({options}): ").lower()
    if user_selection == "off":
        print("Turning machine off!")
        machine_running = False
    elif user_selection == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = coffee_maker_menu.find_drink(user_selection)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
