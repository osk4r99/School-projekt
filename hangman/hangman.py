import random
print("Hangman\nYou have 8 chanses before the man gets executed")
sh={1:0,2:0}
hanged=["\n\n\n\n\n\n-------------","        \n        |\n        |\n        |\n        |\n        |\n-------------","   _____\n        |\n        |\n        |\n        |\n        |\n-------------","   _____\n   |    |\n        |\n        |\n        |\n        |\n-------------","   _____\n   |    |\n   O    |\n        |\n        |\n        |\n-------------","   _____\n   |    |\n   O    |\n   |    |\n        |\n        |\n-------------","   _____\n   |    |\n   O    |\n  /|    |\n        |\n        |\n-------------","   _____\n   |    |\n   O    |\n  /|\\   |\n        |\n        |\n-------------","   _____\n   |    |\n   O    |\n  /|\\   |\n  /     |\n        |\n-------------","   _____\n   |    |\n   O    |\n  /|\\   |\n  / \\   |\n        |\n-------------"]
word=random.choice(("hangman","hello","Why dont you choose the word?","cool","Turkmenistan"))
sgu={1:[],2:[],3:[]}
word=word.lower()
for i in range(0,len(word)):
    sgu[1].append(word[i])
    sgu[2].append("_")
print("\n\n\nThe secret word:"," ".join(sgu[2]),"\n")
while sh[2]<=8:
    if "_" not in sgu[2]:
        break
    sh[1]=0
    print(hanged[sh[2]])
    print("\n\nUsed letters:\n"," ".join(sgu[3]))
    ans=input("\nGuess a letter")
    sgu[3].append(ans)
    for i in range(0, len(sgu[1])):
        if sgu[1][i]==ans:
            sgu[2][i]=ans
            sh[1]=1
    if sh[1]==0:
        sh[2]+=1
    print("\n\n\nThe secret word:"," ".join(sgu[2]),"\n")
if sh[2]==9:
    print("%s \nYOU LOOSE"%(hanged[sh[2]]))
else:
    print("%s \nYOU WIN"%(hanged[sh[2]]))



