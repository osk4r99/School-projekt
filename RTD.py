# Original by Jerry Pesola

import random

def answear():
    while True:
        ans = input("Y/n\n")
        ans = ans.lower()
        if "y" in ans:
            return ans
            break
        elif "n" in ans:
            return ans
            break
        else:
            print("ERROR")
            continue
def betFunc():
    while True:
        bet = input("How much do you bet: ")
        try:
            bet = float(bet)
        except ValueError:
            print("Not a valid number\n")
            continue
        if bet >= 0:
            return bet
            break
        else:
            print("Cant bet less than 0\n")
bet = 0
money = 10000
tWon = 0
tLos = 0
name = input("Whats your name")
ans = input("Type h for help")
if ans == "help" or ans == "h":
    print("In roll the dice your roll a 100 sided dice\nIf you get 65 or more you win double your bet\nIf you get 90 or more you win tripple")
    input("Enter to start")
while True:
    print("do you want to keep your bet?\nYour current bet is",bet,"€")
    ans = answear()
    if ans =="n":
        bet=betFunc()
    if money<=0:
        break
    if bet > money:
        bet=money
    dice=int(random.random()*100)
    print("\n\n======\n| {} |\n======".format(dice))
    if bet>money:
      bet=money
    elif bet<0:
      bet=0
    elif dice>=90:
      print(name,"won:",bet*3,"€")
      money+=bet*3
      tWon+=bet*3
    elif dice>=65:
      print(name,"won:",bet*2,"€")
      money+=bet*2
      tWon+=bet*2
    else:
      print(name,"lost:",bet,"€")
      money-=bet
      tLos+=bet
    print("\n\n\n\n\nMoney:",money,"€")
    print("\nTotal won:",tWon,"€")
    print("Total lost:",tLos,"€\n")
    print("\nDo you want to continue playing")
    ans = answear()
    if ans == "n":
        break
    print("\n\n","RESTART".center(70,"*"),"\n\n")
