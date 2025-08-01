MENU = { 
    "espresso" : { 
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },

    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : { 
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0
    }
}
profit = 0
resources = {
    
    "water" : 300,
    "milk" : 200,
    "coffee" : 180,
}

def is_resources_sufficient(order_ingredients):
    """ Return true when order have been made and return false when ingredients are insufficients. """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry there is not enough {item}. ")
            return False
    return True

def process_coins():
    """ Calculated total  inserted  coins. """
    print("Please insert the coins. ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennis? ")) * 0.01
    return total

def is_payment_successful(money_recieved, drink_cost):
    """ Return true if the payment is accepted or false if not. """
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost , 2)
        print(f" Here is ${change} change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enouh money. money refunds. ")
        return False

def make_coffee(drink_name, order_ingredients):
    """ Deduct the ingreients after the order placed successfully. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ")

is_on = True
while is_on:
    choice  = input("What would you like? : espresso, latte, cappuccino. ").lower()
    if choice == "off":
        is_on = False
    elif choice  == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")

             
      




    