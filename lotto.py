#lotto
#lottorad=random.sample(lottoTal,7)
import random
lottoTal=[]

minRad=[1, 12, 15, 25, 29, 30, 34]

for i in range(0,35):
    lottoTal.append(i+1)
lottoRad=random.sample(lottoTal,7)
success=0
j=1
sex=0
fem=0
fyra=0
tre=0
while success<=6:
    success=0
    lottoRad=random.sample(lottoTal,7)
    lottoRad.sort()
    for i in range(0,7):
        if minRad[i]==lottoRad[i]:
            success+=1
    lottoRad.sort()
    j+=1
    if success==5:
        sex+=1
    elif success==4:
        fem+=1
    elif success==3:
        fyra+=1
    elif success==2:
        tre+=1
print(j)
print(lottoRad)

print()
print("du hade",sex,"st 6 i rad")
print("du hade",fem,"st 5 i rad")
print("du hade",fyra,"st 4 i rad")
print("du hade",tre,"st 3 i rad")
