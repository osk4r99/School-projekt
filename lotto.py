import random
lottoTal=[]
myRow=[]
#myRow=[1, 12, 15, 25, 29, 30, 34]
for i in range(0,7):
    myRow.append(input("Enter number between 1-35 and dont use same number twice"))
    while True:
        try:
            myRow[i]=int(myRow[i])
            break
        except:
            myRow[i]=input("Enter number between 1-35 and dont use same number twice")
    myRow.sort()
    print(myRow)
for i in range(0,35):
    lottoTal.append(i+1)
lottoRow=random.sample(lottoTal,7)
success=0
counter=1
six=0
five=0
four=0
three=0
two=0
while success<=6:
    success=0
    lottoRow=random.sample(lottoTal,7)
    lottoRow.sort()
    for j in range(0,7):
        for i in range(0,7):
            if myRow[j]==lottoRow[i]:
                success+=1
    lottoRow.sort()
    counter+=1
    if success==5:
        six+=1
    elif success==4:
        five+=1
    elif success==3:
        four+=1
    elif success==2:
        three+=1
    elif success==1:
        two+=1
print(counter)
print(lottoRow)

print()
print("You had %s 6 in a row"%(six))
print("You had %s 5 in a row"%(five))
print("You had %s 4 in a row"%(four))
print("You had %s 3 in a row"%(three))
print("You had %s 2 in a row"%(two))
