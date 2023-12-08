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
                exit()
            elif menu_selection == "report":  # run inventory report
                for key, value in resources.items():  # cycle through resources
                    print(f"{key.title()}: {value['amount']}{value['uom']}")
                print(f"Money: ${profit:,.2f}")  # print money collected
            elif menu_selection in ["espresso", "latte", "cappuccino"]:  # select coffee
                # check resource availability, restart if not enough ingredients
                for ingredients_key, ingredients_value in coffee_menu[menu_selection]["ingredients"].items():
                    for resources_key, resources_value in resources.items():
                        if ingredients_key == resources_key:
                            if ingredients_value > resources_value['amount']:
                                print(f"Sorry there is not enough {ingredients_key}.")
                                restart = True
                print(f"An espresso will cost ${coffee_menu[menu_selection]['cost']:.2f}")  # enter money
                num_quarters = int(input("Please insert number of quarters: "))
                money_entered = num_quarters * coins['quarter']
                print(f"${money_entered:.2f} entered so far")
                num_quarters = int(input("Please insert number of dimes: "))
                money_entered += num_quarters * coins['dime']
                print(f"${money_entered:.2f} entered so far")
                num_quarters = int(input("Please insert number of nickels: "))
                money_entered += num_quarters * coins['nickel']
                print(f"${money_entered:.2f} entered so far")
                num_quarters = int(input("Please insert number of pennies: "))
                money_entered += num_quarters * coins['penny']
                print(f"${money_entered:.2f} entered so far")
                if money_entered >= coffee_menu[menu_selection]['cost']:  # check if enough money
                    change = money_entered - coffee_menu[menu_selection]['cost']  # transact if enough money
                    print(f"Here is your {menu_selection} and your change of ${change:.2f}")
                    profit += money_entered - change  # running total of money
                    for ingredients_key, ingredients_value in coffee_menu[menu_selection]["ingredients"].items():
                        for resources_key, resources_value in resources.items():
                            if ingredients_key == resources_key:  # loop to deduct ingredients on transaction
                                resources_value['amount'] -= ingredients_value
                else:  # if not enough money, restart and do not transact
                    print("That wasn't enough money")
                    restart = True
            else:  # loop on bad selection
                print("invalid selection")
                restart = True


coffee_main()
