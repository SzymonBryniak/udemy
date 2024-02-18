import threading
import datetime
import time

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

profit = 0


def idling():

    time.sleep(1)
    print("seconds")
    return "time is up"


def get_user_input():
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    user_prompt = input('“What would you like? (espresso/latte/cappuccino)')
    return user_prompt


def process_coins(thread1, thread2):
    # TODO: 5.  Process coins.
    global profit
    seconds = 10
    wait_time = False
    total = 0
    coins = {
        "quarter": 0.25,
        "dimes": 0.10,
        "nickles": 0.50,
        "pennies": 0.01,
    }

    coin_input = input('Please insert coins (quarter, dimes, nickles, pennies): ')

    if coin_input:
        for key, value in coins.items():
            if key == coin_input:
                total += value

    profit += total
    return total


th1 = threading.Thread(target=idling, args=())
th2 = threading.Thread(target=process_coins, args=())


def coffee_machine(fetch_menu, thread1, thread2):
    global resources
    price = 0
    user_input = get_user_input()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        return 'Machine turned off'
    # TODO: 3. Print report.
    elif user_input == "report":
        print(fetch_menu)
        get_user_input()
    elif user_input == "espresso":
        resources['water'] -= fetch_menu['espresso']['ingredients']['water']
        resources['coffee'] -= fetch_menu['espresso']['ingredients']['coffee']
        # TODO: 4. Check resources sufficient?
        for key, value in resources.items():
            if value <= 0:
                print(f' enough {key}')
                #cost= fetch_menu['espresso']['cost'], old argument for process_coins
        process_coins(thread1, thread2)  # ask to insert coins
        return coffee_machine(fetch_menu, thread1, thread2) #
    elif user_input == "latte":
        resources['water'] -= fetch_menu['latte']['ingredients']['water']
        resources['milk'] -= fetch_menu['latte']['ingredients']['milk']
        resources['coffee'] -= fetch_menu['latte']['ingredients']['coffee']
        for key, value in resources.items():
            if value <= 0:
                print(f'Sorry there is not not enough {key}')
        return coffee_machine(fetch_menu)
    elif user_input == "cappuccino":
        resources['water'] -= fetch_menu['cappuccino']['ingredients']['water']
        resources['milk'] -= fetch_menu['cappuccino']['ingredients']['milk']
        resources['coffee'] -= fetch_menu['cappuccino']['ingredients']['coffee']
        for key, value in resources.items():
            if value <= 0:
                print(f'Sorry there is not not enough {key}')
        return coffee_machine(fetch_menu)
    return



    #TODO: 6. Check transaction successful?
    #TODO: 7. Make Coffee.

coffee_machine(MENU, th1, th2)
# resources['water'] -= MENU['espresso']['ingredients']['water']
# print(resources)
#
# for i, a in resources.items():
#     print(i,a)

