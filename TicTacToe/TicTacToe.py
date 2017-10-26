def printinf():
        print ("-------------\n| %s | %s | %s |\n-------------"%(board[0], board[1], board[2]))
        print ("| %s | %s | %s |\n-------------"%(board[3], board[4], board[5]))
        print ("| %s | %s | %s |\n-------------\n"%(board[6], board[7], board[8]))
def test(xeo,players,name):
        player=[0,0]
        i=0
        for x in range(0, 3):
                if board[i]==board[i+1]==board[i+2]==xeo:
                        print("{} wins".format(name))
                        player[players]=1
                        break
                elif board[x]==board[x+3]==board[x+6]==xeo:
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
        return player
def crashtest(playr,xo):
        print("%s where do you want to put a %s"%(playr,xo))
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
                        board[ans]="X"
                        player = test("X",0,Player[0])
                        if player[0]==1:
                                p1wins+=1
                                break
                        printinf()
                        if 0 not in board and 1 not in board and 2 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board:
                                print("Its a tie!")
                                break
                        ans = crashtest(Player[1],"Y")
                        board[ans]="O"
                        player = test("O",1,Player[1])
                        if player[1]==1:
                                p2wins+=1
                                break
                printinf()
                ans = input("Do you want to rematch??\ny/n")
                if "n" in ans:
                        break
                print("{} has won {} game(s)".format(Player[0],p1wins))
                print("{} has won {} game(s)".format(Player[1],p2wins))
                input("\npress any key to start")
        if "n" in ans:
                ans = input("Do you want to quit\ny/n")
                if "n" in ans:
                        continue
                else:
                        break
                         
                 
#This is a program made by Oskar
#No rights reserved Oskar Öhman
