def printinf():
        print ("-------------")
        print ("|",board[0],"|",board[1],"|",board[2],"|")
        print ("-------------")
        print ("|",board[3],"|",board[4],"|",board[5],"|")
        print ("-------------")
        print ("|",board[6],"|",board[7],"|",board[8],"|")
        print ("-------------","\n")
def test(xeo,players):
        player=[0,0]
        count=0
        i=0
        j=1
        I=2
        si=0
        sj=3
        sI=6
        while 3 > count:
                if board[i]==board[j]==board[I]==xeo:
                        print("Player {} wins".format(xeo))
                        player[players]=1
                        break
                elif board[si]==board[sj]==board[sI]==xeo:
                        print("Player {} wins".format(xeo))
                        player[players]=1
                        break
                elif board[0]==board[4]==board[8]==xeo:
                        print("Player {} wins".format(xeo))
                        player[players]=1
                        break
                elif board[2]==board[4]==board[6]==xeo:
                        print("Player {} wins".format(xeo))
                        player[players]=1
                        break
                i=i+3
                j=j+3
                I=I+3
                si=si+1
                sj=sj+1
                sI=sI+1
                count=count+1
        return player
board = [0,1,2,3,4,5,6,7,8]
player1=0
player2=0
while True:
        printinf()
        print("Player 1 where do you want to input??")
        ans = int(input(""))
        while board[ans]=="O" or board[ans]=="X":
                ans = int(input("Enter new tal"))
        board[ans]="X"
        player = test("X",0)
        if player[0]==1:
                break
        printinf()
        print("Player 2 where do you want to input??")
        ans = int(input(""))
        while board[ans]=="O" or board[ans]=="X":
                ans = int(input("Enter new tal"))
        board[ans]="O"
        player = test("X",0)
        if player[1]==1:
                break
printinf()
