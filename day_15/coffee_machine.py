# imports
from coffee_resources import MENU, resources


def coffee_main():
    """ virtual coffee device """
    coffee_menu = MENU  # initialize function variables
    profit = float(0.00)
    machine_running = True
    coins = {"quarter": .25, "dime": .1, "nickel": .05, "penny": .01}
    while machine_running is True:  # check of turned off
        restart = False  # will restart and not transact in cases of low resources or money, keep running totals
        while restart is False:
            menu_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if menu_selection == "off":  # turn machine off
                print("Turning machine off.  Have a nice day!")
                exit(0)
            elif menu_selection == "report":  # run inventory report
                for key, value in resources.items():  # cycle through resources
                    print(f"{key.title()}: {value['amount']}{value['uom']}")
                print(f"Money: ${profit:,.2f}")  # print money collected
            elif menu_selection in ["espresso", "latte", "cappuccino"]:  # select coffee
                # check resource availability, restart if not enough ingredients
                for ingredient, amount_needed in coffee_menu[menu_selection]["ingredients"].items():  # begin loop
                    if amount_needed > resources[ingredient]['amount']:  # check for sufficient ingredients
                        print(f"Sorry there is not enough {ingredient}.")
                        restart = True  # restart if insufficient ingredients, otherwise exit loop
                print(f"An espresso will cost ${coffee_menu[menu_selection]['cost']:.2f}")
                money_entered = 0  # enter money
                for coin, value in coins.items():
                    num_coins = int(input(f"Please insert number of {coin}s: "))
                    money_entered += num_coins * value
                    print(f"${money_entered:.2f} entered so far")  # end money entered loop
                if money_entered >= coffee_menu[menu_selection]['cost']:  # check if enough money
                    change = money_entered - coffee_menu[menu_selection]['cost']  # transact if enough money
                    print(f"Here is your {menu_selection} and your change of ${change:.2f}")
                    profit += money_entered - change  # running total of money
                    for ingredient, amount_used in coffee_menu[menu_selection]["ingredients"].items():
                        resources[ingredient]['amount'] -= amount_used
                else:  # if not enough money, restart and do not transact
                    print("That wasn't enough money")
                    restart = True
            else:  # loop on bad selection
                print("invalid selection")
                restart = True


coffee_main()
