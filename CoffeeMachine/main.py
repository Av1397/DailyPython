MENU = {
    'espresso': {

        'ingredients': {

            'water': 50,

            'coffee': 18
        },

        'cost': 1.5
    },

    'latte': {

        'ingredients': {

            'water': 200,
            'milk': 150,
            'coffee': 24
        },

        'cost': 2.5
    },

    'capuccino': {

        'ingredients': {

            'water': 250,
            'milk': 100,
            'coffee': 24
        },

        'cost': 3.0
    },

    
}

def isResourceSufficient(order_ingredients):

    '''Return true if ingredients are enough to make the order'''

    for item in order_ingredients:

        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")

            return False
        return True

def processCoins():

    '''Returns the total money Calculated'''

    print("Inster Coins")
    total = float(input("Inster quater: "))*0.25
    total += float(input("Inster dimes: "))*0.10
    total += float(input("Inster nickles: "))*0.05
    total += float(input("Inster pennies: "))*0.01
    return total

def isTransactionSuccessful(moneyReceived, orderAmount):

    '''Return True if payment is accepted else false if money id insuuficent'''
    if moneyReceived >= orderAmount:
        change = round((moneyReceived - orderAmount), 2)
        global profit 
        profit += moneyReceived

        print(f"Here is your remaining amount in change {change}")
        return True
    else:
        print("Sorry the money is not enough. Money is refunded")
        return False

def makeCoffee(drink, order_ingredients):

    for item in order_ingredients:

        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink}")


profit = 0
resources = {

    'water': 300,
    'milk': 200,
    'coffee': 100

}

isOn = True
while (isOn):
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':

        isOn = False

    elif choice == "report":

        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")

    else:

        drink = MENU[choice]
        if isResourceSufficient(drink['ingredients']):

            payment = processCoins()
            if isTransactionSuccessful(payment, drink['cost']):
                makeCoffee(choice, drink['ingredients'])

            




        




