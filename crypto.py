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
USER_MONEY = 10000
COUNTRY = ['France', 'USA' , 'Canada', 'Japan', 'Australia', 'China', 'Russia', 'Germany', 'Algeria']

#################################################################
# Don't edit these value !
# It will crash the game.
#################################################################

USER_VALUE = 0
DAY = 1
dateNow = datetime.datetime.now()
file = open(f"{dateNow.year}-{dateNow.month}-{dateNow.day}-{dateNow.hour}-{dateNow.minute}-{dateNow.second}-{CRYPTO_NAME}.log", "w")
file.write("# Generated Log of the Game.\n# Game by Teo Jauffret\n\n")
x = [DAY]
y = [CRYPTO_COST]

#################################################################
# Code of the game
#################################################################

while True:
    os.system("cls")
    print(f"Day {DAY}\nMoney : {USER_MONEY:.2f}$\n{CRYPTO_NAME} you have : {USER_VALUE}\n{CRYPTO_NAME} value you have : {USER_VALUE*CRYPTO_COST:.2f}$\n\n{CRYPTO_NAME} info :\n\t- Value : {CRYPTO_AVAILABLEVALUE}\n\t- Cost : {CRYPTO_COST:.2f}$\n\t- Total Cost : {CRYPTO_COST*CRYPTO_AVAILABLEVALUE}$")
    file.write(f"Day {DAY}\nMoney : {USER_MONEY:.2f}\n{CRYPTO_NAME} you have : {USER_VALUE}\n{CRYPTO_NAME} value you have : {USER_VALUE*CRYPTO_COST:.2f}$\n\n{CRYPTO_NAME} info :\n\t- Value : {CRYPTO_AVAILABLEVALUE}\n\t- Cost : {CRYPTO_COST:.2f}$\n\t- Total Cost : {CRYPTO_COST*CRYPTO_AVAILABLEVALUE}$\n")
    choice = input("Choose your action (BUY/SELL/WAIT/GRAPHIC/EXIT) : ")
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
    elif choice == "EXIT":
        print("Goodbye Trader.")
        print(f"You can find a log file of this game in the game dir !")
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