from art import logo
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
}

def check_resource(ingridient):
    for item in ingridient:
        if ingridient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def insert_coint():
    print("Please Insert coin!!")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total

def check_Transaction_Suscces(money_receive, drink_cost):
    if money_receive > drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {drink_name} ☕")

def restock_resource():
    resources["water"] += int(input("How much water: "))
    resources["milk"] += int(input("How much milk: "))
    resources["coffee"] += int(input("How much coffee: "))

profit = 0
end_machine = True
print(logo)
while end_machine:
    
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user == "off":
        end_machine = False
    elif user == "report":
        for item in resources:
            print(item, ":" , resources[item])
        print("Money : $", profit)
    elif user == "restock":
        restock_resource()
    
    else:
        drink = MENU[user]
        if check_resource(drink["ingredients"]):
            payment = insert_coint()
            if check_Transaction_Suscces(payment,drink["cost"]):
                make_coffee(user,drink["ingredients"])



