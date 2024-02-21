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
ThreadEnd = False


def idling():
    global ThreadEnd
    global ToElapse
    ToElapse = 10
    time.sleep(10)

    ThreadEnd = True
    return


def get_user_input():
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    user_input = input('“What would you like? (espresso/latte/cappuccino)')
    return user_input


def check_transaction(total, cost):
    if total >= cost:
        print('transaction successful')
        print('making coffee')
        print(f'your change is {total - cost}')
    elif total< cost:
        print('not enough money inserted')
    return
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):


def process_coins(thread_idling, cost):
    global ThreadEnd
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

    while total < cost and not ThreadEnd:
        print(total, cost)
        coin_input = input('Please insert coins (quarter, dimes, nickles, pennies): ')
        for key, value in coins.items():
            if key == coin_input:
                total += value
                profit += value
    check_transaction(total, cost)
    return total


ThreadIdling = threading.Thread(target=idling, args=())
ThreadCoins = threading.Thread(target=process_coins, args=())
ThreadInput = threading.Thread(target=get_user_input, args=())


def coffee_machine(fetch_menu, thread1):
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

        process_coins(thread1, cost=fetch_menu['espresso']['cost'])  # ask to insert coins
        return coffee_machine(fetch_menu, thread1)
    elif user_input == "latte":
        resources['water'] -= fetch_menu['latte']['ingredients']['water']
        resources['milk'] -= fetch_menu['latte']['ingredients']['milk']
        resources['coffee'] -= fetch_menu['latte']['ingredients']['coffee']
        for key, value in resources.items():
            if value <= 0:
                print(f'Sorry there is not enough {key}')
        process_coins(thread1, cost=fetch_menu['latte']['cost'])
        return coffee_machine(fetch_menu, thread1)
    elif user_input == "cappuccino":
        resources['water'] -= fetch_menu['cappuccino']['ingredients']['water']
        resources['milk'] -= fetch_menu['cappuccino']['ingredients']['milk']
        resources['coffee'] -= fetch_menu['cappuccino']['ingredients']['coffee']
        for key, value in resources.items():
            if value <= 0:
                print(f'Sorry there is not not enough {key}')
        process_coins(thread1, cost=fetch_menu['cappuccino']['cost'])
        return coffee_machine(fetch_menu, thread1)
    return


ThreadIdling.start()
coffee_machine(MENU, ThreadIdling)
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.

# resources['water'] -= MENU['espresso']['ingredients']['water']
# print(resources)
#
# for i, a in resources.items():
#     print(i,a)

#th1.start()
#th2.start()

