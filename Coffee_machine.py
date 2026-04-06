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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: Print report to see the remaining resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

# TODO 2: Check if enough resources are present to make coffee
def check_resources(coffee_choice):
    for item in coffee_choice:
        if coffee_choice[item] > resources[item]:
            print(f"Sorry, you don't have enough money. Money refunded.")
            return False
    return True

# TODO 3: Process coins
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# TODO 4: Check if transaction is successful
def check_transaction(money, coffee_cost):
    if money >= coffee_cost:
        change = round(money - coffee_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += coffee_cost
        return True
    else:
        print(f"Sorry, you don't have enough money for this coffee {coffee_cost}.")
        return False

# TODO 5: Deduct the required ingredients from the resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name} ☕️. Enjoy!")

machine_on = True

while machine_on:
    customer_drink = input("What would you like? espresso/latte/cappuccino: ")
    if customer_drink == "off":
        print("Turning off the coffee machine.")
        machine_on = False
    elif customer_drink == "report":
        report()
    else:
        drink = MENU[customer_drink]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(customer_drink, drink["ingredients"])
