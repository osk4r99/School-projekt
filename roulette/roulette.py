#Roulette v 0.5
#Its now playable
import random
def betFunc():
    while True:
        bet = input("How much do you bet[1]: ") or 1
        try:
            bet = int(bet)
        except ValueError:
            print("Not a valid number\n")
            continue
        if bet >= 0:
            return bet
            break
        else:
            print("Cant bet less than 0\n")
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
red=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
even=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
low=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
hi=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
first12=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
secound12=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
third12=[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
#print("ALL NUMBERS")
#print(numbers)
#print("\nRED")
#print(red)
#print("\nBLACK")
#print(black)
#print("\nEVEN")
#print(even)
#print("\nODD")
#print(odd)
#print("\n19 to 36")
#print(hi)
#print("\n1 to 18")
#print(low)
#print("\nFIRST")
#print(first12)
#print("\nSECOUND")
#print(secound12)
#print("\nTHIRD")
#print(third12)
money=100
while True:
    print("MONEY")
    print(money)
    win=0
    number=random.sample(numbers,1)
#    print("\nCHOOSEN NUMBER")
#    print(number[0])
    bet=betFunc()
    ans=input("What do you bet on 1 red 2 black 3 high 4 low 5 odd 6 even 7 first 8 secound 9 third 0 straight on")
    if "7" in ans or "8" in ans or "9" in ans:
        for i in range(0, 12):
            if "7" in ans:
                if number[0]==first12[i]:
                    print("Its in the first dozen")
                    money+=bet+bet
                    win=1
                    break
            elif "8" in ans:
                if number[0]==secound12[i]:
                    print("Its in the secound dozen")
                    money+=bet+bet
                    win=1
                    break
            elif "9" in ans:
                if number[0]==third12[i]:
                    print("Its in the third dozen")
                    win=1
                    money+=bet+bet
                    break
        if win==0:
            print("You guessed wrong")
            money-=bet
    elif "1" in ans or "2" in ans or "3" in ans or "4" in ans or "5" in ans or "6" in ans:
        for i in range(0, 18):
            if "1" in ans:
                if number[0]==red[i]:
                    print("Its red")
                    win=1
                    money+=bet
                    break
            elif "2" in ans:
                if number[0]==black[i]:
                    print("Its black")
                    win=1
                    money+=bet
                    break
            elif "3" in ans:
                if number[0]==hi[i]:
                    print("Its a high number")
                    win=1
                    money+=bet
                    break
            elif "4" in ans:
                if number[0]==low[i]:
                    print("Its a low number")
                    win=1
                    money+=bet
                    break
            elif "6" in ans:
                if number[0]==even[i]:
                    print("Its a even number")
                    win=1
                    money+=bet
                    break
            elif "5" in ans:
                if number[0]==odd[i]:
                    print("Its a odd number")
                    win=1
                    money+=bet
                    break
        if win==0:
            print("You guessed wrong")
            money-=bet
    elif "0" in ans:
        ans=input("number")
        if int(ans)==int(number[0]):
            print("Straight on")
            win=1
            money+=bet*35
        else:
            print("You guessed wrong")
            money-=bet
    print("\nCHOOSEN NUMBER")
    print(number[0])
    print("\n\n","RESTART".center(70,"*"),"\n\n")
