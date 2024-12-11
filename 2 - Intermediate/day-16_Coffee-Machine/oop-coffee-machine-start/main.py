from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafeMenu = Menu()
coffeeMachine = CoffeeMaker()
money = MoneyMachine()

run = True

while run:
    userChoice = input("What would you like? (espresso/latte/cappuccino/):")

    if userChoice == "report":
        coffeeMachine.report()
        money.report()
    elif userChoice == "off":
        run = False
    elif cafeMenu.find_drink(userChoice) == "":
        print(cafeMenu.find_drink(userChoice))
    else:
        if coffeeMachine.is_resource_sufficient(cafeMenu.find_drink(userChoice)) and money.make_payment(cafeMenu.find_drink(userChoice).cost):
            coffeeMachine.make_coffee(cafeMenu.find_drink(userChoice))