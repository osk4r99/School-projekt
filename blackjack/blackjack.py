from random import shuffle
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
def cardDraw(drawncards, drawncard, OneOrTwo):
    hand=[]
    cardValue=[0, 0]
    for i in range(drawncards, drawncard):
        hand.append(cardDeck[drawncards])
        drawncards+=1
    for i in range(0, OneOrTwo):
        if "Ace" in hand[i]:
            cardValue[i]+=11
        elif "King" in hand[i] or "Queen" in hand[i] or "Jack" in hand[i]:
            cardValue[i]+=10
        else:
            cardValue[i]+=int(hand[i][0:2]) #0:2 tar de 2 första letters from the string
    if OneOrTwo==2:
        cardTotal=int(cardValue[0])+int(cardValue[1])
        print("You got a",hand[0],"and a",hand[1],"\nWich is a total of",cardTotal)
    elif OneOrTwo==1:
        cardTotal=int(cardValue[0])
        print("You got a",hand[0])  
    return cardTotal
a=0
cardTotal=0
while a<4:
    drawncards=0
    cardDeck=[]
    color=["Hearts", "Diamonds", "Spades", "Clubs"]
    card=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    for i in range(0,13):
        var="%s of %s"%(card[i], color[0])
        var2="%s of %s"%(card[i], color[1])
        var3="%s of %s"%(card[i], color[2])
        var4="%s of %s"%(card[i], color[3])
        cardDeck.append(var)
        cardDeck.append(var2)
        cardDeck.append(var3)
        cardDeck.append(var4)
    shuffle(cardDeck)
    print(cardDeck)

    cardTotal=0
#    print("Total money",money,"€")
#    print("Total los",tLos,"€")
#    print("Total won",tWon,"€")
#    print("do you want to keep your bet?")
#    print("Your current bet is",bet,"€")
#    ans = answear()
#    if ans =="n":
#        bet=betFunc()
#    if money<=0:
#        money+=sel()
#        if money<=0:
#            break
#    if bet>money:
#        bet=money
    #print("Hello",name,"\nwelcome to blackjack\n")
    input("Press enter to start\n")
    cardTotal+=cardDraw(drawncards, drawncards+2, 2)
    drawncards+=2
    print("Do you want another card\n")
    ans = answear()
    if ans == "n":
        a=1
    while a<1:
        cardTotal+=cardDraw(drawncards, drawncards+1, 1)
        drawncards+=1
        print("Wich is a total of",cardTotal)
        if cardTotal>=22:
            a=3
            cardTotal=0
            print("\n\nDealer won\n")
#            money-=bet
#            tLos+=bet
        else:
            print("Do you want another card\n")
            ans = answear()
            if ans == "n":
                a=1
    cardP1=cardTotal
    cardTotal=0
    while a<2:
        input("Dealers turn\nPress enter\n")
        cardTotal+=cardDraw(drawncards, drawncards+2, 2)
        drawncards+=2
        if cardTotal>=cardP1:
            print("Dealer won\n")
            a=3
#            money-=bet
#            tLos+=bet    
        while a<3:
            input("\nPress enter to continiue\n")
            cardTotal+=cardDraw(drawncards, drawncards+1, 1)
            drawncards+=1
            print("Wich is a total of",cardTotal,"\n")
            if cardTotal>=22:
                a=3
#                print("\n\n",name,"won\n")
                print("WIN")
#                money+=bet
#                tWon+=bet
            elif cardP1<=cardTotal:
                print("\n\nDealer won\n")
                a=3
#                money-=bet
#                tLos+=bet
    print("Do you want to play again\n")
    ans = answear()
    if ans == "n":
#        print("Welcome back again",name)
        break
    else:
        a=0
        print("\n\n","RESTART".center(70,"*"),"\n\n")
