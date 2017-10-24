print("Hangmantest")
#print("Step 1")
#print("-------------")
#print("Step 2")
#print("        \n        |\n        |\n        |\n        |\n        |\n-------------")
#print("Step 3")
#print("   _____\n        |\n        |\n        |\n        |\n        |\n-------------")
#print("Step 4")
#print("   _____\n   |    |\n        |\n        |\n        |\n        |\n-------------")
#print("Step 5")
#print("   _____\n   |    |\n   O    |\n        |\n        |\n        |\n-------------")
#print("Step 6")
#print("   _____\n   |    |\n   O    |\n   |    |\n        |\n        |\n-------------")
#print("Step 7")
#print("   _____\n   |    |\n   O    |\n  /|    |\n        |\n        |\n-------------")
#print("Step 8")
#print("   _____\n   |    |\n   O    |\n  /|\\   |\n        |\n        |\n-------------")
#print("Step 9")
#print("   _____\n   |    |\n   O    |\n  /|\\   |\n  /     |\n        |\n-------------")
#print("Step 10")
#print("   _____\n   |    |\n   O    |\n  /|\   |\n  / \\   |\n        |\n-------------")
success=0
hangman=0
lista=["-------------",
       "        \n        |\n        |\n        |\n        |\n        |\n-------------",
       "   _____\n        |\n        |\n        |\n        |\n        |\n-------------",
       "   _____\n   |    |\n        |\n        |\n        |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n        |\n        |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n   |    |\n        |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n  /|    |\n        |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n  /|\\   |\n        |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n  /|\\   |\n  /     |\n        |\n-------------",
       "   _____\n   |    |\n   O    |\n  /|\   |\n  / \\   |\n        |\n-------------"]
import random
word=random.choice(("hangman","hello","Why dont you choose the word?","cool","Turkmenistan"))
win=0
secret=[]
guessed=[]
used=[]
word=word.lower()
for i in range(0,len(word)):
    secret.append(word[i])
    guessed.append("_")
print("\nThe secret word:")
print(" ".join(guessed))
print("\n")
while hangman<=8:
    if "_" in guessed:
        print()
    else:
        win=1
        break
    success=0
    print(lista[hangman])
    print("\n\nUsed letters:")
    print(" ".join(used))
    ans=input("\nGuess a letter")
    used.append(ans)
    for i in range(0, len(secret)):
        if secret[i]==ans:
            guessed[i]=ans
            success=1
    if success==0:
        hangman+=1
    print("\n\n\nThe secret word:")
    print(" ".join(guessed))
    print("\n")
if win==1:
    print(lista[hangman])
    print("YOU WIN")
else:
    print(lista[hangman])
    print("YOU LOOSE")

