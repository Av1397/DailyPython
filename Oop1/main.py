from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_making = CoffeeMaker()
coffee_money_machine = MoneyMachine()

isOn = True
while isOn:
    user_choice = input("“What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        isOn = False
    elif user_choice == "report":
        coffee_making.report()
        coffee_money_machine.report()
    else:
        drink = coffee_menu.find_drink(user_choice)
        if coffee_making.is_resource_sufficient(drink):
            if coffee_money_machine.make_payment(drink.cost):

                coffee_making.make_coffee(drink)
               







