#Blackjack version 1.3
#Now aces should automatically turn into value of 1 instead of making your hand bust
#Todo Doubling down and splitting
#adding more than 1 player (Perhaps start with 2) 
#Five card charlie
#
#NOTE TO SELF vvvvvvvvv
#dealer får blackjack och jag 21 blir det oavgjort eller vinner dealer
#när får man splitta och hur funkar det
#När får man double down och vad innebär det
#Vad innebär incuranse eller försäkring
#och om dealern får 17 får han plocka mera kort
#och när t.ex spelare 1 har 17 och dealer har 17 blir det tie
#
#TODO add so if player has 21 he cannot pickup another card
from random import shuffle
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
def answear():
    while True:
        ans = input("Y/n[Yes]:\n") or "y"
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
def cardDraw(drawncard, OneOrTwo, plyr, name):
    global drawncards
    hand=[]
    for i in range(drawncards, drawncard):
        hand.append(cardDeck[drawncards])
        cardsdranw[plyr].append(cardDeck[drawncards])
        drawncards+=1
#    if len(hand)==2:
#        hand[0]="Ace of Clubs"
#        hand[1]="Ace of Spades"
    for i in range(0, OneOrTwo):
        if "Ace" in hand[i]:
            cardValue[plyr].append(11)
        elif "King" in hand[i] or "Queen" in hand[i] or "Jack" in hand[i]:
             cardValue[plyr].append(10)
        else:
           cardValue[plyr].append(int(hand[i][0:2])) #0:2 takes the 2 first letters from the string
    testForAces(plyr)
    if OneOrTwo==2:
        print("%s got a %s and a %s \nWich is a total of %s"%(name, hand[0], hand[1], sum(cardValue[plyr])))
    elif OneOrTwo==1:
        print("%s got a %s"%(name, hand[0]))
def testForAces(plyr):
    if sum(cardValue[plyr])>=22:
        for i in range(0, len(cardsdranw[plyr])):
            if "Ace" in cardsdranw[plyr][i]:
                if cardValue[plyr][i]==1:
                    continue
                else:
                    cardValue[plyr][i]=1
                    break
def testPlayerCards():
    if len(cardsdranw[1])==5:
        return 1
#Remove this when you make the full game
money=100
bet=0
name=input("Enter NAME[Bob]:") or "Bob"
tLos=0
tWon=0


while True:
    while True:
        lose=0
        cardsdranw=[[], []]
        cardValue=[[], []]
        #0 is dealer 1 is player
        
        #try to replace cards drawn with len(cardsdranw)
        drawncards=0
        cardDeck=[]
        color=["Hearts", "Diamonds", "Spades", "Clubs"]
        card=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for i in range(0,13):
            var="%s of %s"%(card[i], color[0])
            var2="%s of %s"%(card[i], color[1])
            var3="%s of %s"%(card[i], color[2])
            var4="%s of %s"%(card[i], color[3])
            cardDeck.extend((var, var2, var3, var4))
        shuffle(cardDeck)
#        print(cardDeck)
#        cardDeck[0]="Ace of Hearts"
#        cardDeck[1]="Ace of Spades"
#        cardDeck[3]="Ace of Clubs"
#        cardDeck[4]="Ace of Diamonds"
        print("Total money %s €\nTotal los %s €\nTotal won %s €"%(money, tLos, tWon))
        bet=betFunc()
    #    if money<=0:
    #        money+=sel()
    #        if money<=0:
    #            break
        if bet>money:
            bet=money
        print("Hello %s\nwelcome to blackjack\n"%(name))
        input("Press enter to start\n")
        cardDraw(drawncards+2, 2, 1, name)
        win=testPlayerCards()
        print()
        cardDraw(drawncards+1, 1, 0, "Dealer")
        if sum(cardValue[1])==21:
            print("Player got a blackjack")
            money+=bet*1.5
            tWon+=bet*1.5
            break
        while True:
            if win==1:
                break
            print("Do you want another card\n")
            ans = answear()
            if ans == "n":
                print("Dealers turn")
                break
            cardDraw(drawncards+1, 1, 1, name)
            win=testPlayerCards()
            print("Wich is a total of",sum(cardValue[1]))
            if sum(cardValue[1])>=22:
                print("\n\nDealer won\n")
                money-=bet
                tLos+=bet
                lose=1
                break
        while lose==0:
            if win==1:
                print("Player got a five card charlie")
                break
            input("\nPress enter to continiue\n")
            cardDraw(drawncards+1, 1, 0, "Dealer")
            print("Wich is a total of",sum(cardValue[0]),"\n")
            if sum(cardValue[0])>=17:
                break
        if lose==1:
            pass
        elif sum(cardValue[1])<sum(cardValue[0]) and  sum(cardValue[0])<22:
            print("\n\nDealer won\n")
            money-=bet
            tLos+=bet
        elif sum(cardValue[0])<sum(cardValue[1]):
                print("\n\n%s won\n"%(name))
                money+=bet
                tWon+=bet
        elif sum(cardValue[0])==sum(cardValue[1]):
            print("Its a draw")
        elif sum(cardValue[0])>=22:
            print("\n\n%s won\n"%(name))
            money+=bet
            tWon+=bet
        break
#        print(cardsdranw)
#        print(cardValue)
#        print(sum(cardValue[0]))
#        print(sum(cardValue[1]))
    print("Do you want to play again\n")
    ans = answear()
    if ans == "n":
        print("Welcome back again",name)
        break
print("\n\n","RESTART".center(70,"*"),"\n\n")
