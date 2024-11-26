MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def printResources():
    print(f"Water: {resources["water"]}mL")
    print(f"Milk: {resources["milk"]}mL")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def checkSufficientResources():
    sufficientResources = True
    for ingredient in MENU[userOption]["ingredients"]:
        if MENU[userOption]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            sufficientResources = False
    return sufficientResources


def calcMoney(numQuarters, numDimes):
    return float(numQuarters) * 0.25 + float(numDimes) * 0.10


def updateResources():
    for ingredient in MENU[userOption]["ingredients"]:
        resources[ingredient] -= MENU[userOption]["ingredients"][ingredient]
    resources["money"] += MENU[userOption]["cost"]


machineOn = True

while machineOn:
    userOption = input("What would you like? (espresso/latte/cappuccino): ")
    if userOption == "Off":
        machineOn = False
    elif userOption == "report":
        printResources()
    elif userOption in MENU:
        if checkSufficientResources():
            numQuarters = input("How many quarters? : ")
            numDimes = input("How many dimes? : ")
            totalMoney = calcMoney(numQuarters, numDimes)

            if totalMoney >= MENU[userOption]["cost"]:
                if totalMoney > MENU[userOption]["cost"]:
                    change = totalMoney - MENU[userOption]["cost"]
                    print(f"Here is ${change} dollars in change")

                updateResources()
                print("Here is your latte. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")