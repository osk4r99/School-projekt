#Roulette v 0.2
#This is just testing
import random
numbers=[]
red=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
even=[]
odd=[]
low=[]
hi=[]
first12=[]
secound12=[]
third12=[]
for i in range(0, 37):
    numbers.append(i)
print("ALL NUMBERS")
print(numbers)
for i in range(1, 37, 2):
    even.append(i+1)
    odd.append(i)
for i in range(1, 19):
    low.append(i)
    hi.append(i+18)
for i in range(1, 13):
    first12.append(i)
    secound12.append(i+12)
    third12.append(i+12+12)
number=random.sample(numbers,1)
print("\nRED")
print(red)
print("\nBLACK")
print(black)
print("\nEVEN")
print(even)
print("\nODD")
print(odd)
print("\n19 to 36")
print(hi)
print("\n1 to 18")
print(low)
print("\nFIRST")
print(first12)
print("\nSECOUND")
print(secound12)
print("\nTHIRD")
print(third12)
print("\n\nCHOOSEN NUMBER")
print(number[0])
bet=int(input("Enter bet"))
ans=input("What do you bet on 1 red 2 black 3 high 4 low 5 odd 6 even 7 first 8 secound 9 third 0 straight on")
if "7" in ans or "8" in ans or "9" in ans:
    for i in range(0, 12):
        if "7" in ans:
            if number[0]==first12[i]:
                print("Its in the first 12")
                break
        elif "8" in ans:
            if number[0]==secound12[i]:
                print("Its in the secound 12")
                break
        elif "9" in ans:
            if number[0]==third12[i]:
                print("Its in the third 12")
                break
if "1" in ans or "2" in ans:
    for i in range(0, 18):
        if "1" in ans:
            if number[0]==red[i]:
                print("its a red card")
                break
        if "2" in ans:
            if number[0]==black[i]:
                print("its a black card")
                break
if "3" in ans or "4" in ans:
    for i in range(0, 18):
        if "3" in ans:
            if number[0]==hi[i]:
                print("its a high card")
                break
        if "4" in ans:
            if number[0]==low[i]:
                print("its a low card")
                break
if "5" in ans or "6" in ans:
    for i in range(1, 18):
        if "6" in ans:
            if number[0]==even[i]:
                print("its a even card")
                break
        if "5" in ans:
            if number[0]==odd[i]:
                print("its a odd card")
                break
if "0" in ans:
    ans=input("number")
    if int(ans)==int(number[0]):
        print("Straight on")
