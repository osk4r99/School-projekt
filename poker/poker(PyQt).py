#Version 1.2
import sys
import fnmatch
from random import shuffle
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow, QStyleFactory
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(0, 0, 1920, 1070)
        self.setWindowTitle("Poker")
        self.setWindowIcon(QIcon("icon.png"))

        Exit = QAction("&Exit application", self)
        Exit.setShortcut("Ctrl+Alt+E")
        Exit.setStatusTip("Leave the app")
        Exit.triggered.connect(self.close_application)

        StyleChange1 = QAction("&Style gtk+", self)
        StyleChange1.setShortcut("Ctrl+Alt+G")
        StyleChange1.setStatusTip("Change style to gtk+")
        StyleChange1.triggered.connect(lambda: self.style_set("gtk+"))

        StyleChange4 = QAction("&Style Windows", self)
        StyleChange4.setShortcut("Ctrl+Alt+W")
        StyleChange4.setStatusTip("Change style to Windows")
        StyleChange4.triggered.connect(lambda: self.style_set("Windows"))

        self.statusBar().showMessage('Message in statusbar.')  

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
        fileMenu.addAction(Exit)
        editMenu.addAction(StyleChange1)
        editMenu.addAction(StyleChange4)

        sshFile="style.css"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

        self.home()

    def home(self):
        global bet, btn, money, pic, btnC, btnB
        btn=[]
        btnC=[]
        btnB=[]
        btn.append(QPushButton("Deal", self))
        btn.append(QPushButton("Deal", self))
        btn.append(QPushButton("Continue", self))
        btn.append(QPushButton("Deal", self))
        btnB.append(QPushButton("Bet 0,20 €", self))
        btnB.append(QPushButton("Bet 0,40 €", self))
        btnB.append(QPushButton("Bet 0,80 €", self))
        btnB.append(QPushButton("Bet  1 €", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))

        self.resize()

        btnC[0].clicked.connect(lambda: self.change("1"))
        btnC[0].move(130,  400)

        btnC[1].clicked.connect(lambda: self.change("2"))
        btnC[1].move(330,  400)

        btnC[2].clicked.connect(lambda: self.change("3"))
        btnC[2].move(530,  400)

        btnC[3].clicked.connect(lambda: self.change("4"))
        btnC[3].move(730,  400)

        btnC[4].clicked.connect(lambda: self.change("5"))
        btnC[4].move(930,  400)

        btnB[0].clicked.connect(lambda: self.bet(0.2, 0))
        btnB[0].resize(100, 50)
        btnB[0].move(200,  100)
        btnB[0].setStyleSheet("background-color:black;")
        bet=0.2
        btnB[0].setShortcut("1")

        btnB[2].clicked.connect(lambda: self.bet(0.8, 2))
        btnB[2].resize(100, 50)
        btnB[2].move(400,  100)
        btnB[2].setShortcut("3")

        btnB[1].clicked.connect(lambda: self.bet(0.4, 1))
        btnB[1].resize(100, 50)
        btnB[1].move(300,  100)
        btnB[1].setShortcut("2")
    
        btnB[3].clicked.connect(lambda: self.bet(1, 3))
        btnB[3].resize(100, 50)
        btnB[3].move(500,  100)
        btnB[3].setShortcut("4")
        
        btn[0].clicked.connect(self.continueG)
        btn[0].resize(100, 50)
        btn[0].move(100,  100)
    
        btn[3].clicked.connect(self.restart)
        btn[3].move(100, 100)

        btn[1].clicked.connect(self.deal)
        btn[1].move(100,  100)
        btn[1].resize(100, 50)
        btn[1].setShortcut("H")
        self.money = QLabel(("Money %s €"%(str(money))), self)
        self.money.setStyleSheet(("background-color: white;"))

        self.money.move(100, 50)
        self.money.resize(120,  20)
        self.player = QLabel("", self)
        self.player.setStyleSheet(("background-color: transparent;"))

        self.player.move(100, 450)
        self.player.resize(400,  50)

        self.dealer = QLabel("", self)

        self.dealer.move(100, 500)
        self.dealer.resize(400,  50)
        self.dealer.setStyleSheet(("background-color: transparent;"))

        self.win = QLabel("", self)

        self.win.move(400, 50)
        self.win.resize(150,  50)
        self.win.setStyleSheet(("background-color: transparent;"))
        font = QFont()
        font.setPointSize(20)
        self.win.setFont(font)

        self.show()
    def continueG(self):
        btn[0].setShortcut("")
        global changeCard, card, bet, money
        win=""
        ans=""
        for i in changeCard:
            ans+=i
        i=len(changeCard)-1
        while len(changeCard)!=0:
            changeCard.pop(i)
            i-=1
        self.empty()
        self.resize()
        card = self.cardPic(ans, card, 150)
        for x in range(0, len(cards)):
            for i in range(0, 5):
                if cards[x][0:2] in card[i][0:2]:
                    if card[i][0:2] not in ranks:
                        pair[i]=(fnmatch.filter(card, '%s*'%(cards[x])))
                        ranks[i]=card[i][0:2]
                        cardValues[i]=x+1
        for i in range(0, len(ranks)):
            if pair[i]!=0:
                pair[i]=len(pair[i])
        for x in range(0, 5):
            for i in range(0, len(pair)):
                if len(pair)<=i:
                    break
                if pair[i]==0:
                    pair.pop(i)
                    ranks.pop(i)
                    cardValues.pop(i)

        while len(pair)!=5:
            pair.append(False)
            ranks.append(False)
            cardValues.append(False)

        for i in range(0, 5):
            if "Spades" in card[i]:
                suit[i]="Spades"
            elif "Hearts" in card[i]:
                suit[i]="Hearts"
            elif "Clubs" in card[i]:
                suit[i]="Clubs"
            elif "Diamonds" in card[i]:
                suit[i]="Diamonds"
        #Use this for printing how many pairs you have of each card
    #    for i in range(0, 5):
    #        if pair[i]!=False:
    #            print("You got",pair[i],"of",ranks[i])
        for i in range(0, len(ranks)):
            if "Ac" in str(ranks[i]):
                ranks[i]="Ace"
            elif "Ja" in str(ranks[i]):
                ranks[i]="Jack"
            elif "Qu" in str(ranks[i]):
                ranks[i]="Queen"
            elif "Ki" in str(ranks[i]):
                ranks[i]="King"
        cardValues.sort()
        if cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1 and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a straight royal flush in "+str(suit[0])
            money+=bet*800
            win="And won %s €"%(round(bet*800, 2))
        elif 5 in pair:
            playerChoice="You got five of "+str(ranks[0]+"'s")
            money+=bet*800
            win="And won %s €"%(round(bet*800, 2))
        elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a straight flush in "+str(suit[0])
            money+=bet*200
            win="And won %s €"%(round(bet*200, 2))
        elif 4 in pair:
            for i in range(0, 2):
                if pair[i]==4:
                    playerChoice="You got four of a kind with "+str(ranks[i]+"'s")
                    money+=bet*80
                    win="And won %s €"%(round(bet*80, 2))
        elif 3 in pair and 2 in pair:
            I=1
            for i in range(0, 2):
                if pair[i]==3 and pair[I]==2:
                    playerChoice="You got a full house with three "+str(ranks[i]+"'s and two ")+str(ranks[I]+"'s")  
                    money+=bet*30
                    win="And won %s €"%(round(bet*30, 2))
                I-=1
        elif suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a flush in "+str(suit[0])
            money+=bet*15
            win="And won %s €"%(round(bet*15, 2))
        elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 or (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1):
            playerChoice="You got a straight"
            money+=bet*10
            win="And won %s €"%(round(bet*10, 2))
        elif 3 in pair:
            for i in range(0, 3):
                if pair[i]==3:
                    playerChoice="You got a tripple of "+str(ranks[i]+"'s")
                    money+=bet*5
                    win="And won %s €"%(round(bet*5, 2))
                    
        elif pair.count(2)==2:
            II,I=0,1
            for i in range(0, 3):
                if pair[II]==2 and pair[I]==2:
                    playerChoice="You got two pairs one of "+str(ranks[II]+"'s")+str(" and one of ")+str(ranks[I]+"'s")
                    money+=bet*3
                    win="And won %s €"%(round(bet*3, 2))
                if I==1:
                    I+=1
                elif I==2:
                    II+=1
        elif 2 in pair:
            for i in range(0, 5):
                if pair[i]==2:
                    playerChoice="You got a pair of "+str(ranks[i]+"'s")
                    if ranks[i][:1] in ("Q", "J", "K", "A"):
                        win="And lost nothing"
                    else:
                        money-=bet
                        win="And lost %s €"%(round(bet, 2))
        elif "Ace" in ranks:
            playerChoice="You got an Ace high"
            money-=bet
            win="And lost %s €"%(round(bet, 2))
        elif "King" in ranks:
            playerChoice="You got a King high"
            money-=bet
            win="And lost %s €"%(round(bet, 2))
            
        elif "Queen" in ranks:
            playerChoice="You got a Queen high"
            money-=bet
            win="And lost %s €"%(round(bet, 2))
        elif "Jack" in ranks:
            playerChoice="You got a Jack high"
            money-=bet
            win="And lost %s €"%(round(bet, 2))
        else:
            playerChoice=str("You got a ")+str(max(cardValues))+str(" high")
            money-=bet
            win="And lost %s €"%(round(bet, 2))
        print(ranks)
        self.player.setText(playerChoice)
        self.player.setStyleSheet(("background-color: white;"))
        self.dealer.setText(win)
        self.dealer.setStyleSheet(("background-color: white;"))
        print(playerChoice)
        money=round(money, 2)
        self.money.setText("Money %s €"%(str(money)))
        btn[3].resize(100, 50)
        btn[3].setShortcut("H")
        btnB[0].resize(100, 50)
        btnB[1].resize(100, 50)
        btnB[0].setShortcut("1")
        btnB[1].setShortcut("2")
        btnB[2].setShortcut("3")
        btnB[3].setShortcut("4")
        btnB[2].resize(100, 50)
        btnB[3].resize(100, 50)
        #Add here make restart button resize


    def empty(self):
        global drawnCards, cardValue, indent, pic, p1
        for i in range(0, len(pic)):
            pic[i].resize(0, 0)
        indent, p1, pic=100, 0, []
    def resize(self):
        for i in range(0, len(btn)):
            btn[i].resize(0, 0)
        for i in range(0, len(btnC)):
            btnC[i].resize(0, 0)
            btnC[i].setShortcut("")
        for i in range(0, len(btnB)):
            btnB[i].resize(0, 0)
            btnB[i].setShortcut("")
    def bet(self, n, index):
        global bet, money, card
        bet=n
        for i in range(0, 4):
            btnB[i].setStyleSheet("background-color:none;")
        btnB[index].setStyleSheet("background-color:black;")
        if bet>money:
            bet=money
        if bet<0:
            bet=0
#        card = self.cardPic(ans, card, 150)
    def deal(self):
        global card
        btn[1].setShortcut("")
        self.resize()
        btn[0].resize(100, 50)
        btn[0].setShortcut("H")
        btnC[0].resize(100, 50)
        btnC[0].setShortcut("1")
        btnC[1].resize(100, 50)
        btnC[1].setShortcut("2")
        btnC[2].resize(100, 50)
        btnC[2].setShortcut("3")
        btnC[3].resize(100, 50)
        btnC[3].setShortcut("4")
        btnC[4].resize(100, 50)
        btnC[4].setShortcut("5")
        card = self.cardPic("12345", card, 150)

    def cardPic(self, ans, card, line):
        global drawn, indent, p1
        I = 1
        for i in range(0, 5):
            if str(I) in ans:
                card[i]=cardDeck[drawn]
                drawn+=1
            I+=1
        I = 1
        for i in range(0, 5):
            pic.append(QLabel(self))
            pic[p1].setPixmap(QPixmap("img/%s.svg"%(card[i])))
            pic[p1].setGeometry(indent, line, 169, 245)
            indent+=200
            pic[p1].show()
            p1+=1
            I+=1
        return card
    def restart(self):
        btn[3].setShortcut("")
        global suit, card, pair, ranks, cardValues, playerChoice, drawn, changeCard
        self.resize()
        self.win.setText("")
        self.dealer.setText("")
        self.player.setText("")
        self.dealer.setStyleSheet(("background-color: transparent;"))
        self.player.setStyleSheet(("background-color: transparent;"))
        self.win.setStyleSheet(("background-color: transparent;"))
        self.empty()
        playerChoice=False
        suit, card, pair, ranks, cardValues = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
        shuffle(cardDeck)
        changeCard=["1", "2", "3", "4", "5"]
        btnC[0].setStyleSheet(("background-color: none;"))
        btnC[1].setStyleSheet(("background-color: none;"))
        btnC[2].setStyleSheet(("background-color: none;"))
        btnC[3].setStyleSheet(("background-color: none;"))
        btnC[4].setStyleSheet(("background-color: none;"))
        drawn=0
        self.deal()
    def style_set(self, n):
        QApplication.setStyle(QStyleFactory.create(n))
    def change(self, n):
        global changeCard
        if str(n) in changeCard:
            temp=False
            for i in range(0, len(changeCard)):
                if changeCard[i] == n:
                    temp=i
            changeCard.pop(temp)
            btnC[int(n)-1].setStyleSheet(("background-color: Black;"))
        else:
            changeCard.append(str(n))
            btnC[int(n)-1].setStyleSheet(("background-color: none;"))
#        btnC[big].resize(100, 50)
#        btnC[small].resize(0, 0)
    def close_application(self):
        sys.exit()
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
global bet
changeCard=["1", "2", "3", "4", "5"]
drawn, cardDeck = 0, []
color = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
money=100
ans=1
#Put in ans how many decks you want to play with
for a in range(0, ans):
    for j in range(0, 4):
        for i in range(0,13):
            var = "%s of %s"%(cards[i], color[j])
            cardDeck.append(var)
shuffle(cardDeck)
playerChoice=False
suit, card, pair, ranks, cardValues = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
p1=0
card.sort()
indent, pic, p1, win, drawn=100, [], 0, 0, 0
run()
