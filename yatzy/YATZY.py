#YATZY version 1.0
#This game is not yet ready
def reroll():
    for i in range (0,5):
        print("%s) %s\n"  % (i,dice[i]))
    print("wich dice do you want to change")
    ans = input("enter")
    for i in range(0,5):
        i = str(i)
        if i in ans:
            i=int(i)
            dice[i]=random.randint(1,6)
        i=int(i)
def prints():
    for i in range (0,5):
        print("%s) %s\n"  % (i,dice[i]))    
    for i in range(1,7):
        print("%s( %s   %s"%(i,stuff[i],points[i]))
    print("Summa    %s"%(sum))
    print("Bonus")
    for i in range(7,16):
        print("%s( %s   %s"%(i,stuff[i],points[i]))
    print("total")
def check():
    ans = int(input("enter 1-15"))
    if ans == 1 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 2 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 3 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 4 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 5 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 6 and points[ans]==0:
        for i in range (0,5):
            if ans == dice[i]:
                points[ans]+=ans
        if points[ans]==0:
            points[ans]="STRIKE"
    elif ans == 7 and points[ans]==0:
        j=3
        for i in range(4,0,-1):
            if dice[i]==dice[j]:
                points[ans]=dice[i]*2
                break
            else:
                points[ans]="STRIKE"
            j-=1
    elif ans == 8 and points[ans]==0:
        if dice[0]==dice[1] and dice[2]==dice[3]:
            points[ans]=dice[0]+dice[1]+dice[2]+dice[3]
        elif dice[1]==dice[2] and dice[3]==dice[4]:
            points[ans]=dice[4]+dice[1]+dice[2]+dice[3]
        elif dice[0]==dice[1] and dice[3]==dice[4]:
            points[ans]=dice[0]+dice[1]+dice[3]+dice[4]
        else:
            points[ans]="STRIKE"
    elif ans == 9 and points[ans]==0:
        j=3
        I=2
        for i in range(4,1,-1):
            if dice[i]==dice[j]==dice[I]:
                points[ans]=dice[i]*3
                break
            else:
                points[ans]="STRIKE"
            j-=1
            I-=1
    elif ans == 10 and points[ans]==0:
        J=1
        j=3
        I=2
        for i in range(4,2,-1):
            if dice[i]==dice[j]==dice[I]==dice[J]:
                points[ans]=dice[i]*4
                break
            else:
                points[ans]="STRIKE"

            j-=1
            I-=1
            J-=1
    elif ans == 11 and points[ans]==0:
        if dice[0]==1 and dice[1]==2 and dice[2]==3 and dice[3]==4 and dice[4]==5:
            points[ans] = dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
        else:
            points[ans]="STRIKE"
    elif ans == 12 and points[ans]==0:
        if dice[0]==2 and dice[1]==3 and dice[2]==4 and dice[3]==5 and dice[4]==6:
            points[ans] = dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
        else:
            points[ans]="STRIKE"
    elif ans == 13 and points[ans]==0:
        if dice[0]==dice[1] and dice[2]==dice[3]==dice[4]:
            points[ans] = dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
        elif dice[0]==dice[1]==dice[2] and dice[3]==dice[4]:
            points[ans] = dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
        else:
            points[ans]="STRIKE"
    elif ans == 14 and points[ans]==0:
        points[ans]=dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
    elif ans == 15 and points[ans]==0:
        if dice[0]==dice[1]==dice[2]==dice[3]==dice[4]:
            points[ans]=50
        else:
            points[ans]="STRIKE"
    else:
        while True:
            randomNum=random.randint(1,15)
            if points[randomNum]==0:
                points[randomNum]="STRIKE"
                break
            else:
                continue
        
#    return points[ans]
import random
sum=0
sumt=0
stuff={1:"Aces",2:"Twos",3:"Threes",4:"Fours",5:"Fives",6:"Sixes",7:"Pair",8:"Two pairs",9:"Three Of A Kind",10:"Four Of A Kind",11:"Small Straight",12:"Large Straight",13:"Full House",14:"Chance",15:"YATZY"}
points={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,}
while True:
    dice=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    #dice=[6,2,3,4,5] #use this to test
    reroll()
    reroll()
    dice.sort()
    for i in range (0,5):
        print("%s) %s\n"  % (i,dice[i]))
    print("chose from the list which one you want\"if you want to strike something you pick something you cannot do\"")
    prints()
    if (points[1]!=0 
    and points[2]!=0
    and points[3]!=0
    and points[4]!=0
    and points[5]!=0
    and points[6]!=0
    and points[7]!=0
    and points[8]!=0
    and points[9]!=0
    and points[10]!=0
    and points[11]!=0
    and points[12]!=0
    and points[13]!=0
    and points[14]!=0
    and points[15]!=0):
        break
    check()
    if points[1]!=0 and points[2]!=0 and points[3]!=0 and points[4]!=0 and points[5]!=0 and points[6]!=0 and sumt==0:
        for i in range(1, 7):
            if "STRIKE" in str(points[i]):
                continue
            else:
                sum=sum+points[i]
        sumt=1
    prints()
