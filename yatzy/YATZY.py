#YATZY version 1.6
#This is a yatzy game please enjoy
#2 player mode
def reroll(plyr, dice):
    for i in range (0,5):
        print("%s) %s\n"  % (i+1,dice[plyr][i]))
    ans=[]
    while True:
        answ=input("enter 1-5 ")
        try:
            answ=int(answ)
            break
        except ValueError:
            if answ=="":
                break
            continue
    print("")
    answ=str(answ)
    for i in range(0, len(answ)):
        ans.append("")
        ans[i]=int(answ[i])-1
    for j in range(0, len(ans)):
        for i in range(0,5):
            i = str(i)
            if i in str(ans[j]):
                i=int(i)
                dice[plyr][i]=random.randint(1,6)
            i=int(i)
def prints(dices, plyr, dice):
    if dices:
        for i in range (0,5):
            print("%s) %s\n"  % (i+1,dice[plyr][i]))    
    for i in range(1,7):
        print("%s) %s   %s   %s"%(i,stuff[i],points[0][i], points[1][i]))
    print("Sum    %s   %s"%(sum[0], sum[1]))
    print("Bonus    %s   %s"%(bonus[0], bonus[1])) #you need 63 sum on upper for you to get bonus
    for i in range(7,16):
        print("%s) %s   %s   %s"%(i,stuff[i],points[0][i], points[1][i]))
    print("Total %s   %s"%(tot[0], tot[1]))
    print("\n")
def check(plyr, dice):
    while True:
        ans = input("enter 1-15 ")
        try:
            ans=int(ans)
            break
        except ValueError:
            continue    
    print("\n\n")
    if ans == 1 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 2 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 3 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 4 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 5 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 6 and points[plyr][ans]==0:
        for i in range (0,5):
            if ans == dice[plyr][i]:
                points[plyr][ans]+=ans
        if points[plyr][ans]==0:
            points[plyr][ans]="STRIKE"
    elif ans == 7 and points[plyr][ans]==0:
        for i in range(4,0,-1):
            if dice[plyr][i]==dice[plyr][i-1]:
                points[plyr][ans]=dice[plyr][i]*2
                break
            else:
                points[plyr][ans]="STRIKE"
    elif ans == 8 and points[plyr][ans]==0:
        if dice[plyr][0]==dice[plyr][1] and dice[plyr][2]==dice[plyr][3]:
            points[plyr][ans]=dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]
        elif dice[plyr][1]==dice[plyr][2] and dice[plyr][3]==dice[plyr][4]:
            points[plyr][ans]=dice[plyr][4]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]
        elif dice[plyr][0]==dice[plyr][1] and dice[plyr][3]==dice[plyr][4]:
            points[plyr][ans]=dice[plyr][0]+dice[plyr][1]+dice[plyr][3]+dice[plyr][4]
        else:
            points[plyr][ans]="STRIKE"
    elif ans == 9 and points[plyr][ans]==0:
        for i in range(4,1,-1):
            if dice[plyr][i]==dice[plyr][i-1]==dice[plyr][i-2]:
                points[plyr][ans]=dice[plyr][i]*3
                break
            else:
                points[plyr][ans]="STRIKE"
    elif ans == 10 and points[plyr][ans]==0:
        for i in range(4,2,-1):
            if dice[plyr][i]==dice[plyr][i-1]==dice[plyr][i-2]==dice[plyr][i-3]:
                points[plyr][ans]=dice[plyr][i]*4
                break
            else:
                points[plyr][ans]="STRIKE"
    elif ans == 11 and points[plyr][ans]==0:
        if dice[plyr][0]==1 and dice[plyr][1]==2 and dice[plyr][2]==3 and dice[plyr][3]==4 and dice[plyr][4]==5:
            points[plyr][ans] = dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]+dice[plyr][4]
        else:
            points[plyr][ans]="STRIKE"
    elif ans == 12 and points[plyr][ans]==0:
        if dice[plyr][0]==2 and dice[plyr][1]==3 and dice[plyr][2]==4 and dice[plyr][3]==5 and dice[plyr][4]==6:
            points[plyr][ans] = dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]+dice[plyr][4]
        else:
            points[plyr][ans]="STRIKE"
    elif ans == 13 and points[plyr][ans]==0:
        if dice[plyr][0]==dice[plyr][1] and dice[plyr][2]==dice[plyr][3]==dice[plyr][4]:
            points[plyr][ans] = dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]+dice[plyr][4]
        elif dice[plyr][0]==dice[plyr][1]==dice[plyr][2] and dice[plyr][3]==dice[plyr][4]:
            points[plyr][ans] = dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]+dice[plyr][4]
        else:
            points[plyr][ans]="STRIKE"
    elif ans == 14 and points[plyr][ans]==0:
        points[plyr][ans]=dice[plyr][0]+dice[plyr][1]+dice[plyr][2]+dice[plyr][3]+dice[plyr][4]
    elif ans == 15 and points[plyr][ans]==0:
        if dice[plyr][0]==dice[plyr][1]==dice[plyr][2]==dice[plyr][3]==dice[plyr][4]:
            points[plyr][ans]=50
        else:
            points[plyr][ans]="STRIKE"
    else:
        while True:
            randomNum=random.randint(1,15)
            if points[plyr][randomNum]==0:
                points[plyr][randomNum]="STRIKE"
                break
            else:
                continue
def game(plyr):
    dice=[[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)], [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]]
    reroll(plyr, dice)
    reroll(plyr, dice)
    dice[plyr].sort()
    print("chose from the list which one you want\"if you want to strike something you pick something you cannot do\"")
    prints(True, plyr, dice)
    check(plyr, dice)
    sum[plyr]=0
    for i in range(1, 7):
        if str(points[plyr][i])=="STRIKE":
            continue
        else:
            sum[plyr]+=points[plyr][i]
    if points[plyr][1]!=0 and points[plyr][2]!=0 and points[plyr][3]!=0 and points[plyr][4]!=0 and points[plyr][5]!=0 and points[plyr][6]!=0 and sumt[plyr]==0:
        sum[plyr]=0
        for i in range(1, 7):
            if "STRIKE" in str(points[plyr][i]):
                continue
            else:
                sum[plyr]+=points[plyr][i]
        if sum[plyr]>=63:
            bonus[plyr]=50
        sumt[plyr]=1
    prints(False, plyr, dice)
import random
sum=[0, 0]
bonus=[0, 0]
tot=[0, 0]
sumt=[0, 0]
stuff={1:"Aces",2:"Twos",3:"Threes",4:"Fours",5:"Fives",6:"Sixes",7:"Pair",8:"Two pairs",9:"Three Of A Kind",10:"Four Of A Kind",11:"Small Straight",12:"Large Straight",13:"Full House",14:"Chance",15:"YATZY"}
points=[{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0}, {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0}]
while True:
    game(0)
    if (points[0][1]!=0 and points[0][2]!=0 and points[0][3]!=0 and points[0][4]!=0 and points[0][5]!=0 and points[0][6]!=0
    and points[0][7]!=0 and points[0][8]!=0 and points[0][9]!=0 and points[0][10]!=0 and points[0][11]!=0 and points[0][12]!=0 
    and points[0][13]!=0 and points[0][14]!=0 and points[0][15]!=0  and points[1][1]!=0  and points[1][2]!=0 and points[1][3]!=0
    and points[1][4]!=0 and points[1][5]!=0 and points[1][6]!=0  and points[1][7]!=0 and points[1][8]!=0 and points[1][9]!=0
    and points[1][10]!=0 and points[1][11]!=0 and points[1][12]!=0 and points[1][13]!=0 and points[1][14]!=0 and points[1][15]!=0):
        break
    input("Press enter player 2")
    game(1)
    if (points[0][1]!=0 and points[0][2]!=0 and points[0][3]!=0 and points[0][4]!=0 and points[0][5]!=0 and points[0][6]!=0
    and points[0][7]!=0 and points[0][8]!=0 and points[0][9]!=0 and points[0][10]!=0 and points[0][11]!=0 and points[0][12]!=0 
    and points[0][13]!=0 and points[0][14]!=0 and points[0][15]!=0  and points[1][1]!=0  and points[1][2]!=0 and points[1][3]!=0
    and points[1][4]!=0 and points[1][5]!=0 and points[1][6]!=0  and points[1][7]!=0 and points[1][8]!=0 and points[1][9]!=0
    and points[1][10]!=0 and points[1][11]!=0 and points[1][12]!=0 and points[1][13]!=0 and points[1][14]!=0 and points[1][15]!=0):
        break
    input("Press enter player 1")
    
for i in range(1, 16):
    if "STRIKE" in str(points[0][i]):
        continue
    else:
        tot[0]+=points[0][i]
tot[0]+=bonus[0]
for i in range(1, 16):
    if "STRIKE" in str(points[1][i]):
        continue
    else:
        tot[1]+=points[1][i]
tot[1]+=bonus[1]
prints(False, 0, 0)
#TODO ADD CHOICE TO PICK 1 or 2 player
