def printinf():
        #Printar ut bilden av spel planen
        print ("-------------\n|",board[0],"|",board[1],"|",board[2],"|\n-------------")
        print ("|",board[3],"|",board[4],"|",board[5],"|\n-------------")
        print ("|",board[6],"|",board[7],"|",board[8],"|\n-------------","\n")
def test(xeo,players,name):
        #xeo är X eller o players är spelare 1 eller 2 name är spelarens namn
        #
        #Definitionen Testar alla möjliga 3 i rad kombinationer för att se om någon vunnit
        player=[0,0]
        #En lista som är till för att få reda på vilken slepare har vunnit
        i,j,I,si,sj,sI=0,1,2,0,3,6
        #variabler som gör testningen mera lätt
        #Utan dem skulle if else satsen innehålla 8 if else satser
        #i j och I testar vågrätt om man får 3 i rad
        #si sj och sI testar lodrätt om man får 3 i rad
        #dom 2 nedarsta testar om man får 3 i rad i kors
        for x in range(0, 3):
                #loopar 3 gånger för det finns 3 rader åt båda hållen
                if board[i]==board[j]==board[I]==xeo:
                        print("{} wins".format(name))
                        player[players]=1
                        break
                elif board[si]==board[sj]==board[sI]==xeo:
                        print("{} wins".format(name))
                        player[players]=1
                        break
                elif board[0]==board[4]==board[8]==xeo:
                        print("{} wins".format(name))
                        player[players]=1
                        break
                elif board[2]==board[4]==board[6]==xeo:
                        print("{} wins".format(name))
                        player[players]=1
                        break
                i=i+3
                j=j+3
                I=I+3
                #lägger till 3 för det första vågrätta 3 i rad är
                #0 1 2 sen
                #3 4 5 sen
                #6 7 8 senär loopen klar
                si=si+1
                sj=sj+1
                sI=sI+1
                #lägger till 1 för den för den första lodrätta 3 i rad är
                #0 3 6 sen
                #1 4 7
                #2 5 8
        return player
def crashtest(playr,xo):
        #playr är spelarens namn xo står för X eller O
        #Defenionen Testar om användar inputten är ok
        print("{} where do you want to put a {}".format(playr,xo))
        ok=0
        while ok==0:
                while True:
                        try:
                                ans = int(input("Use numbers 0 - 8 "))
                                break
                        except ValueError:
                                print("That was not a valid number")
                while True:
                        try:
                            board[ans]
                        except IndexError:
                            print("Index out of range")
                            printinf()
                            break
                        if board[ans]!="O" and board[ans]!="X":
                                ok=1
                        else:
                                print("That spot is allready taken")
                                printinf()
                        break
        return ans
while True:
        Player = [input("Enter name player 1 "),input("Enter name player 2 ")]
        p1wins = 0
        p2wins = 0
        #player = False
        #if player insta wins use this to clear out the array
        while True:
                board = [0,1,2,3,4,5,6,7,8]
                player1=0
                player2=0
                while True:
                        printinf()
                        if 0 not in board and 1 not in board and 2 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board:
                                print("Its a tie!")
                                break
                        ans = crashtest(Player[0],"X")
                        #Player[0] är player 1 och "X" är för att han är spelaren som använder X
                        board[ans]="X"
                        #sätter på spel planens index som spelaren har valt ett X
                        player = test("X",0,Player[0])
                        #Testar om spelare 1 har vunnit
                        if player[0]==1:
                                #detta körs när spelare 1 vinner
                                p1wins+=1
                                break
                        printinf()
                        #printar ut bilden
                        if 0 not in board and 1 not in board and 2 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board:
                                print("Its a tie!")
                                break
                        #Testar om det finns oanvända platser kvar på brädan
                        ans = crashtest(Player[1],"Y")
                        #Samma men för player 2
                        board[ans]="O"
                        #samma men player 2
                        player = test("O",1,Player[1])
                        #samma men player 2
                        if player[1]==1:
                                p2wins+=1
                                break
                printinf()
                ans = input("Do you want to rematch??\ny/n")
                if "n" in ans:
                        break
                        #om man svarar nej så frågar den om du vill quit
                print("{} has won {} game(s)".format(Player[0],p1wins))
                print("{} has won {} game(s)".format(Player[1],p2wins))
                #Säger hur många gånger spelare 1 och 2 har vunnit
                input("\npress any key to start")
        if "n" in ans:
                ans = input("Do you want to quit\ny/n")
                #om man svarar nej resettas namn och winster
                if "n" in ans:
                        continue
                else:
                        break
                         
                 
#This is a program made by Oskar
#No rights reserved Oskar Öhman
