#YATZY version 1.7
#This is a yatzy game please enjoy
#Many player mode is available
def reroll(plyr, dice):
    for i in range (0,5):
        print("%s) %s\n"% (i+1,dice[plyr][i]))
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
            print("%s) %s\n" % (i+1,dice[plyr][i]))
    for i in range(1,7):
        print("%s) %s   %s"%(i,stuff[i], points[plyr][i]))
    print("Sum    %s"%(sum[plyr]))
    print("Bonus    %s"%(bonus[plyr])) #you need 63 sum on upper for you to get bonus
    for i in range(7,16):
        print("%s) %s   %s"%(i,stuff[i],points[plyr][i]))
    print("Total %s"%(tot[plyr]))
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
def game(plyr, dice):
    dice[plyr]=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
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
quit=0
print("Welcome to yatzy game")
sum=[]
bonus=[]
tot=[]
sumt=[]
points=[]
dice=[]
ans=int(input("How many players?"))
for i in range(0, ans):
    sum.append(0)
    bonus.append(0)
    tot.append(0)
    sumt.append(0)
    points.append({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0})
    dice.append([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])
stuff={1:"Aces",2:"Twos",3:"Threes",4:"Fours",5:"Fives",6:"Sixes",7:"Pair",8:"Two pairs",9:"Three Of A Kind",10:"Four Of A Kind",11:"Small Straight",12:"Large Straight",13:"Full House",14:"Chance",15:"YATZY"}
while True:
    for i in range(0, ans):
        if (points[ans-1][1]!=0 
        and points[ans-1][2]!=0 
        and points[ans-1][3]!=0 
        and points[ans-1][4]!=0 
        and points[ans-1][5]!=0 
        and points[ans-1][6]!=0
        and points[ans-1][7]!=0 
        and points[ans-1][8]!=0 
        and points[ans-1][9]!=0 
        and points[ans-1][10]!=0 
        and points[ans-1][11]!=0 
        and points[ans-1][12]!=0 
        and points[ans-1][13]!=0 
        and points[ans-1][14]!=0 
        and points[ans-1][15]!=0):
            quit=1
            break
        input("Press enter player %s"%(i+1))
        game(i, dice)
    if quit==1:
        break
for j in range(0, ans):
    for i in range(1, 16):
        if "STRIKE" in str(points[j][i]):
            continue
        else:
            tot[j]+=points[j][i]
    tot[j]+=bonus[j]
print(tot)
prints(False, 0, 0)
