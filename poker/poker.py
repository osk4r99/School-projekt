# coding: UTF-8
#Version 1.0
import datetime, fnmatch
from random import shuffle
def cardPic(ans, card):
    global drawn
    I = 1
    for i in range(0, 5):
        if str(I) in ans:
            card[i]=cardDeck[drawn]
            drawn+=1
        I+=1
    I = 1
    for i in card:
        print("%s) %s\n"%(I, i))
        I+=1
    return card
timeNow=datetime.datetime.now()
while True:
    drawn, cardDeck = 0, []
    color = ["Hearts", "Diamonds", "Spades", "Clubs"]
    cards = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    ans = 1
    #Put in ans how many decks you want to play with
    for a in range(0, ans):
        for j in range(0, 4):
            for i in range(0,13):
                var = "%s of %s"%(cards[i], color[j])
                cardDeck.append(var)
    shuffle(cardDeck)
#    cardDeck[0]="Ace of Hearts"
#    cardDeck[1]="King of Hearts"
#    cardDeck[2]="Queen of Hearts"
#    cardDeck[3]="Jack of Hearts"
#    cardDeck[4]="10 of Hearts"
    #print(cardDeck)
    playerChoice=False
    suit, card, pair, ranks, cardValues = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
    card = cardPic("12345", card)
    ans = input("Wich card/s do you want to change?\nType all numbers you want to change 1 - 5\n\n")
    card = cardPic(ans, card)
    card.sort()
    currentcard = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for x in range(0, len(cards)):
        for i in range(0, 5):
            if cards[x][0:2] in card[i][0:2]:
                if card[i][0:2] not in ranks:
                    pair[i]=(fnmatch.filter(card, '%s*'%(cards[x])))
                    ranks[i]=card[i][0:2]
                    cardValues[i]=x+1
    for i in range(0, len(ranks)):
        if pair[i]!=0:
            pair[i]=len(pair[i])
    for x in range(0, 5):
        for i in range(0, len(pair)):
            if len(pair)<=i:
                break
            if pair[i]==0:
                pair.pop(i)
                ranks.pop(i)
                cardValues.pop(i)
        
    while len(pair)!=5:
        pair.append(False)
        ranks.append(False)
        cardValues.append(False)
        
    for i in range(0, 5):
        if "Spades" in card[i]:
            suit[i]="Spades"
        elif "Hearts" in card[i]:
            suit[i]="Hearts"
        elif "Clubs" in card[i]:
            suit[i]="Clubs"
        elif "Diamonds" in card[i]:
            suit[i]="Diamonds"
    par2=pair.count(2)
    #Use this for printing how many pairs you have of each card
#    for i in range(0, 5):
#        if pair[i]!=False:
#            print("You got",pair[i],"of",ranks[i])
    for i in range(0, len(ranks)):
        if "Ac" in str(ranks[i]):
            ranks[i]="Ace"
        elif "Ja" in str(ranks[i]):
            ranks[i]="Jack"
        elif "Qu" in str(ranks[i]):
            ranks[i]="Queen"
        elif "Ki" in str(ranks[i]):
            ranks[i]="King"
    cardValues.sort()
    if cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1 and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
        playerChoice="You got a straight royal flush in "+str(suit[0])
    elif 5 in pair:
        playerChoice="You got five of "+str(ranks[0]+"'s")
    elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 and playerChoice==False and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
        playerChoice="You got a straight flush in "+str(suit[0])
    elif 4 in pair:
        for i in range(0, 2):
            if pair[i]==4:
                playerChoice="You got four of a kind with "+str(ranks[i]+"'s")
    elif 3 in pair and 2 in pair:
        I=1
        for i in range(0, 2):
            if pair[i]==3 and pair[I]==2:
                playerChoice="You got a full house with three "+str(ranks[i]+"'s and two ")+str(ranks[I]+"'s")  
            I-=1
    elif suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
        playerChoice="You got a flush in "+str(suit[0])
    elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4:
        playerChoice="You got a straight"
    elif cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1:
        playerChoice="You got a straight"
    elif 3 in pair:
        for i in range(0, 3):
            if pair[i]==3:
                playerChoice="You got a tripple of "+str(ranks[i]+"'s")
    elif par2==2:
        II,I=0,1
        for i in range(0, 3):
            if pair[II]==2 and pair[I]==2:
                playerChoice="You got two pairs one of "+str(ranks[II]+"'s")+str(" and one of ")+str(ranks[I]+"'s")
            if I==1:
                I+=1
            elif I==2:
                II+=1
    elif 2 in pair:
        for i in range(0, 5):
            if pair[i]==2:
                playerChoice="You got a pair of "+str(ranks[i]+"'s")
    elif "Ace" in ranks:
        playerChoice="You got an Ace high"
    elif "King" in ranks:
        playerChoice="You got a King high"
    elif "Queen" in ranks:
        playerChoice="You got a Queen high"
    elif "Jack" in ranks:
        playerChoice="You got a Jack high"
    else:
        playerChoice=str("You got a ")+str(max(cardValues))+str(" high")
    print(playerChoice)
    ans=input("\n\n\nDo you want to play again y/n")
    ans=ans.lower()
    if "n" in ans:
        break
    elif "y" in ans:
        continue
    else:
        print("I'll take that as a yes\n\n")
timeAfter=datetime.datetime.now()
timeTotal=timeAfter-timeNow
print(timeTotal,"total time playing poker")
