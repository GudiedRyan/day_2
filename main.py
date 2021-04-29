from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    user = input("What would you like? (espresso/latte/cappuccino): \n")
    if user == "off":
        print("Shutting off.")
        is_on = False
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)