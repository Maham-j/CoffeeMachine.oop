from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu =  Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

options = menu.get_items()


while True:
    choice = input(f'What would you like? {options}')
    drinks = menu.find_drink(choice)
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        break
    elif choice == choice not in options:
        print('Type valid data')
    else:
        if coffee_maker.is_resource_sufficient(drink=drinks):
            if money_machine.make_payment(drinks.cost):
                coffee_maker.make_coffee(drinks)



