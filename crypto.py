# Crypto Game by Téo Jauffret

# MIT License
#
# Copyright (c) 2024 Téo Jauffret
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import random
import matplotlib.pyplot as plt
import datetime
import sys

#################################################################
# You can edit all data you want in this section !
#################################################################

CRYPTO_NAME = "BTC"
CRYPTO_COST = 200
CRYPTO_AVAILABLEVALUE = 45001
USER_MONEY = 0
COUNTRY = ['France', 'USA' , 'Canada', 'Japan', 'Australia', 'China', 'Russia', 'Germany', 'Algeria']

#################################################################
# Don't edit these value !
# It will crash the game.
#################################################################

USER_VALUE = 0
DAY = 1
dateNow = datetime.datetime.now()
CPU_LEVEL = 1
file = open(f"{dateNow.year}-{dateNow.month}-{dateNow.day}-{dateNow.hour}-{dateNow.minute}-{dateNow.second}-{CRYPTO_NAME}.log", "w")
file.write("# Generated Log of the Game.\n# Game by Teo Jauffret\n\n")
x = [DAY]
y = [CRYPTO_COST]
CREDIT_TAKE = False
ae = random.choice(COUNTRY)
DAY_TO_FILL = 100

#################################################################
# Code of the game
#################################################################

while True:
    if USER_MONEY <= 0:
        print("You loose the game!")
        if not CREDIT_TAKE:
            ad = random.randint(0, 15000)
            af = int(ad*1.5)
            print(f"Bank of {ae} want to offer you {ad}$ But you have to give us at day {DAY_TO_FILL} : {int(ad*1.5)}$!")
            p = input("Do you want to accept this offer ? (Yes = Continue) (No = Loose The Game) : ")
            if p == "Yes":
                CREDIT_TAKE = True
                USER_MONEY += ad
                print(f"[Bank of {ae}] Good luck.")
                a = input("Press enter to continue")
                continue
            else:
                a = input("Press enter to exit")
                sys.exit()
    if CREDIT_TAKE:
        if DAY >= DAY_TO_FILL:
            print(f"[Bank of {ae}] Hey you, You didn't pay us! Byebye...\nYou've been killed.")
            a = input("Press enter to exit")
            sys.exit()
        else:
            pass
    os.system("cls")
    print(f"Day {DAY}\nMoney : {USER_MONEY:.2f}$\n{CRYPTO_NAME} you have : {USER_VALUE}\n{CRYPTO_NAME} value you have : {USER_VALUE*CRYPTO_COST:.2f}$\n\n{CRYPTO_NAME} info :\n\t- Value : {CRYPTO_AVAILABLEVALUE}\n\t- Cost : {CRYPTO_COST:.2f}$\n\t- Total Cost : {CRYPTO_COST*CRYPTO_AVAILABLEVALUE}$")
    if CREDIT_TAKE:
        print("Don't forget that you have a credit to but!")
    file.write(f"Day {DAY}\nMoney : {USER_MONEY:.2f}\n{CRYPTO_NAME} you have : {USER_VALUE}\n{CRYPTO_NAME} value you have : {USER_VALUE*CRYPTO_COST:.2f}$\n\n{CRYPTO_NAME} info :\n\t- Value : {CRYPTO_AVAILABLEVALUE}\n\t- Cost : {CRYPTO_COST:.2f}$\n\t- Total Cost : {CRYPTO_COST*CRYPTO_AVAILABLEVALUE}$\n")
    choice = input("Choose your action (BUY/SELL/WAIT/GRAPHIC/MINE/SHOP/EXIT/BANK) : ")
    if choice == "BUY":
        howMuch = int(input(f"How many {CRYPTO_NAME} you want to buy : "))
        if USER_MONEY >= howMuch*CRYPTO_COST:
            USER_VALUE += howMuch
            USER_MONEY = USER_MONEY-(howMuch*CRYPTO_COST)
        else:
            print("You need more money to buy the quantity you want!")
            a = input("Press enter to continue")
            continue
        TEMP = CRYPTO_AVAILABLEVALUE
        CRYPTO_AVAILABLEVALUE = CRYPTO_AVAILABLEVALUE - howMuch
        CRYPTO_COST = float((CRYPTO_COST*TEMP)/CRYPTO_AVAILABLEVALUE)
        file.write(f"You buy {howMuch} {CRYPTO_NAME} !\n")
    elif choice == "SELL":
        howMuch = int(input(f"How many {CRYPTO_NAME} you want to sell : "))
        TEMP = CRYPTO_AVAILABLEVALUE
        if USER_VALUE >= howMuch:
            CRYPTO_AVAILABLEVALUE += howMuch
            USER_MONEY = USER_MONEY + (howMuch*CRYPTO_COST)
            USER_VALUE = USER_VALUE - howMuch
        else:
            print("You need more crypto to sell!")
            a = input("Press enter to continue")
            continue
        CRYPTO_COST = float((CRYPTO_COST*TEMP)/CRYPTO_AVAILABLEVALUE)
        file.write(f"You sell {howMuch} {CRYPTO_NAME} !\n")
    elif choice == "WAIT":
        file.write(f"You decided to wait !\n")
        pass
    elif choice == "GRAPHIC":
        plt.plot(x, y, marker="o", linestyle="-")
        plt.title(f"Evolution of {CRYPTO_NAME}")
        plt.xlabel("Days")
        plt.ylabel(f"{CRYPTO_NAME} Price")
        plt.xticks(range(1, max(x) + 1))
        plt.grid(True)
        plt.show()
        file.write("You decided to see the graphic !\n")
        a = input("Press enter to continue")
        continue
    elif choice == "MINE":
        if USER_MONEY >= 500:
            number = random.randint(0, 100)
            for i in range(CPU_LEVEL*10):
                k = random.randint(0, 100)
                print(f"[{CRYPTO_NAME}Miner] Trying to mine block '{k}'...")
                if k == number:
                    print(f"[{CRYPTO_NAME}Miner] {CRYPTO_NAME} \033[32m FOUND \033[0m on block '{k}'")
                    m = random.randint(0, 50)
                    print(f"[{CRYPTO_NAME}Miner] You found {m} {CRYPTO_NAME}\n")
                    TEMP = CRYPTO_AVAILABLEVALUE
                    USER_VALUE += m
                    CRYPTO_AVAILABLEVALUE = CRYPTO_AVAILABLEVALUE - m
                    CRYPTO_COST = float((CRYPTO_COST*TEMP)/CRYPTO_AVAILABLEVALUE)
                else:
                    print(f"[{CRYPTO_NAME}Miner] \033[31m FAILED \033[0m to mine block '{k}'\n")
            USER_MONEY = USER_MONEY-500
        else:
            print(f"[{CRYPTO_NAME}Miner] We are sorry, but you don't have the money needed to mine with our service. (500$ is needed.)")
    elif choice == "SHOP":
        print("Welcome to the CrypterShop!\n---------------------\n")
        print(f"1. CPU Lvl.{CPU_LEVEL+1}: {CPU_LEVEL*5000}$ (Multiply by 10 the Minage)")
        print("2. Exit the Shop.")
        p = input("Enter a product you want to buy: ")
        if p == "1":
            if USER_MONEY >= CPU_LEVEL*5000:
                print(f"You successfully buy CPU Lvl.{CPU_LEVEL} !")
                USER_MONEY = USER_MONEY-(CPU_LEVEL*5000)
                CPU_LEVEL += 1
                continue
            else:
                print("You don't have so much money for this article !")
                continue
        else:
            print("Exit the shop.")
            continue
    elif choice == "BANK":
        if not CREDIT_TAKE:
            print(f"[Bank of {ae}] You don't have any taxe!")
            a = input("Press enter to continue")
            continue
        else:
            print(f"[Bank of {ae}] You must give us {af}$ before day {DAY_TO_FILL} to survive.")
            pe = input("Do you want to pay ? (YES/NO) : ")
            if pe == "YES":
                if USER_MONEY >= af:
                    USER_MONEY = USER_MONEY - af
                    print(f"[Bank of {ae}] Thank you for paying.")
                    CREDIT_TAKE = False
                    a = input("Press enter to continue")
                else:
                    print(f"[Bank of {ae}] You don't have the requirement!")
                    a = input("Press enter to continue")
                continue
    elif choice == "EXIT":
        print("Goodbye Trader.")
        print(f"You can find a log file of this game in the game dir !")
        a = input("Press enter to exit")
        file.close()
        sys.exit()
    else:
        pass
    numberOfValue = random.randint(int(-CRYPTO_AVAILABLEVALUE/25), int(CRYPTO_AVAILABLEVALUE/25))
    if numberOfValue < 0:
        WORD = "sell"
        numberOfValue = str(numberOfValue).replace("-", "")
        TEMP = CRYPTO_AVAILABLEVALUE
        CRYPTO_AVAILABLEVALUE += int(numberOfValue)
        CRYPTO_COST = float((CRYPTO_COST*TEMP)/CRYPTO_AVAILABLEVALUE)
    else:
        WORD = "buy"
        numberOfValue = str(numberOfValue)
        TEMP = CRYPTO_AVAILABLEVALUE
        CRYPTO_AVAILABLEVALUE = CRYPTO_AVAILABLEVALUE - int(numberOfValue)
        CRYPTO_COST = float((CRYPTO_COST*TEMP)/CRYPTO_AVAILABLEVALUE)
    print(f"Trader from {random.choice(COUNTRY)} {WORD} {numberOfValue} {CRYPTO_NAME} !")
    file.write(f"Trader from {random.choice(COUNTRY)} {WORD} {numberOfValue} {CRYPTO_NAME} !\n--------------------------\n")
    a = input("Press enter to continue")
    DAY += 1
    x.append(DAY)
    y.append(CRYPTO_COST)