from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker= CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like to have {options}").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)