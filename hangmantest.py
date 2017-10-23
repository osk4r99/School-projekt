print("Hangmantest")
print("Step 1")
print("-------------")
print("Step 2")
print("        \n        |\n        |\n        |\n        |\n        |\n-------------")
print("Step 3")
print("   _____\n        |\n        |\n        |\n        |\n        |\n-------------")
print("Step 4")
print("   _____\n   |    |\n        |\n        |\n        |\n        |\n-------------")
print("Step 5")
print("   _____\n   |    |\n   O    |\n        |\n        |\n        |\n-------------")
print("Step 6")
print("   _____\n   |    |\n   O    |\n   |    |\n        |\n        |\n-------------")
print("Step 7")
print("   _____\n   |    |\n   O    |\n  /|    |\n        |\n        |\n-------------")
print("Step 8")
print("   _____\n   |    |\n   O    |\n  /|\\   |\n        |\n        |\n-------------")
print("Step 9")
print("   _____\n   |    |\n   O    |\n  /|\\   |\n  /     |\n        |\n-------------")
print("Step 10")
print("   _____\n   |    |\n   O    |\n  /|\   |\n  / \\   |\n        |\n-------------")
word="test"
secret=["t", "e", "s", "t"]
quessed=["_", "_", "_", "_"]
used=[]

while True:
    ans=input("Guess a letter")
    used.append(ans)
    for i in range(0, 4):
        if secret[i]==ans:
            quessed[i]=ans
    print(quessed)
    print(used)
