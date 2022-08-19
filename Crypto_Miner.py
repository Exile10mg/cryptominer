from random import choices
import time
import os
import keyboard

os.system('CLS')

log = "admin"
pas = "admin"
username = "Annonymous"
wallet = "Unknown"
balance123 = 0
logotype = """

█▀▀ █▀█ █▄█ █▀█ ▀█▀ █▀█   █▀▄▀█ █ █▄░█ █▀▀ █▀█   █░█ ▄█ ░ █▀█ ▀█
█▄▄ █▀▄ ░█░ █▀▀ ░█░ █▄█   █░▀░█ █ █░▀█ ██▄ █▀▄   ▀▄▀ ░█ ▄ █▄█ █▄

      """
chars = list('abcdefghijklmnopqrstvxyzABCDEFGHIKLMNOPQRSTVXYZ0123456789')
mnemic = ['Please', 'Memory', 'Aunt', 'Sally', 'Addition', 'Subtraction', 'Dear', 'My']
def random_string(chars, length):
    string = []
    for _ in range(length):
        string += choices(chars)
    return ''.join(string)

def miner():
    while True:
        if keyboard.is_pressed('F4'):
            for i in range(100):
                print("BALANCE: 0 | RECEIVED: 0 | ADDRESS: 0x" + random_string(chars, 36) + " | MNEMONIC PHRASE: " + random_string(mnemic, 3))
                time.sleep(0.1)
            print("BALANCE: 1.45 | RECEIVED: 1.45 | ADDRESS: 0x" + random_string(chars, 36) + " | MNEMONIC PHRASE: " + random_string(mnemic, 4))
            for i in range(100): 
                print("BALANCE: 1.45 | RECEIVED: 0 | ADDRESS: 0x" + random_string(chars, 36) + " | MNEMONIC PHRASE: " + random_string(mnemic, 3))
                time.sleep(0.1)
            break
        os.system('CLS')
        print(logotype)
        print("")
        print("Hold F4 to start mining...")
        time.sleep(1)
        print("Hold F4 to start mining...")
def main_fun():
    print(logotype)
    print("- Welcome Crypto Miner v1.02 created by Exile.")
    print("""- Program designed for educational purposes.
- The creator is not responsible for the damage suffered. """)
    print("")
    login = input("Please enter your login: ")
    password = input("Please enter your password: ")

    if login == log and password == pas:
        os.system('CLS')
        print(logotype)
        for q in range(10):
            print("Logging in...")
            time.sleep(0.5)
        print("")    
        print("Successful login!")
        time.sleep(3)
        os.system('CLS')
        login_fun(wallet, balance123)
    else:
        while True:
            print("")
            print("Incorrect login or password!")
            time.sleep(2)
            os.system('CLS')
            main_fun()
def login_fun(a, b):
    print(logotype)
    print(f"Welcome again {username} !")
    print("")
    print(f"Your wallet address is: {a}")
    print("")
    print("Menu: ")
    print("1. Enter the address of your wallet.")
    print("2. Check your balance.")
    print("3. Information about your account.")
    print("4. Start mining ...")
    print("5. Logout!")
    print("")
    menu_input = input("Choose your option: ")
    if menu_input == '4':
        miner()
        print("")
        print("Found BTC with value: 1.45!")
        print("Press F5 to continue.")
        b2 = balance123
        b2 += 1.45
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                login_fun(a, b2)
                break
            else:
                continue
    elif menu_input not in ['1', '2', '3', '4', '5']:
        print("")
        print("Invalid option.")
        time.sleep(1.5)
        os.system('CLS')
        login_fun(a, b)
    elif menu_input == '5':
        for h in range(5):
            print("")
            print("You will be logged out in a moment.")
            time.sleep(1)
        os.system('CLS')
        main_fun()
    elif menu_input == '1':
        os.system('CLS')
        print(logotype)
        print("WARNING!")
        print("Make sure the wallet address you entered is correct!")
        print("***************************************************")
        wallet2 = input("Enter your wallet address: ")
        print("")
        if len(wallet2) < 8:
            print("")
            print("Incorrect wallet address!")
        else:
            for r in range(5):
                print("Checking...")
                time.sleep(1)
            print("")
            print("Congratulations 🙂, you have successfully updated your wallet address!")
            print("")
            print("Press F5 to continue.")
            while True:
                if keyboard.is_pressed('F5'):
                    os.system('CLS')
                    login_fun(wallet2, balance123)
                else:
                    continue
    elif menu_input == '2':
        os.system('CLS')
        print(logotype)
        print(f"Your balance is: {b} BTC")
        print("")
        print("Press F5 to continue.")
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                login_fun(a, b)
                break
            else:
                continue
main_fun()