# Copyright (C) 2018 Oskar Öhman

# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2, as published by the
# Free Software Foundation

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#PyQt5-BlackJack Version 1.1
# MAKE USE OF BTN SET TEXT
# REMOVE ALLA MÄLLAN STEG
# AFTER RESTART SOMETIME EXTRA MELLANSTÄG
# Enable insurance button if dealer has 10 showing in the situation när man får ha en insurance and split button
# FIGURE OUT WHY du must do if oneortwocard is less than 0 and if u set it 0 it start on 1
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow, QStyleFactory
from PyQt5.QtGui import QIcon, QPixmap, QFont
from random import shuffle

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(0, 0, 1920, 1070)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("favicon.ico.png"))
        
        Exit = QAction("&Exit application", self)
        Exit.setShortcut("Ctrl+Alt+E")
        Exit.setStatusTip("Leave the app")
        Exit.triggered.connect(self.hitMe)
        
        StyleChange1 = QAction("&Style gtk+", self)
        StyleChange1.setShortcut("Ctrl+Alt+G")
        StyleChange1.setStatusTip("Change style to gtk+")
        StyleChange1.triggered.connect(lambda: self.style_set("gtk+"))
        
        StyleChange2 = QAction("&Style Plastique", self)
        StyleChange2.setShortcut("Ctrl+Alt+P")
        StyleChange2.setStatusTip("Change style to Plastique")
        StyleChange2.triggered.connect(lambda: self.style_set("Plastique"))
    
        StyleChange3 = QAction("&Style Cleanlooks", self)
        StyleChange3.setShortcut("Ctrl+Alt+C")
        StyleChange3.setStatusTip("Change style to Cleanlooks")
        StyleChange3.triggered.connect(lambda: self.style_set("Cleanlooks"))

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
        editMenu.addAction(StyleChange2)
        editMenu.addAction(StyleChange3)
        editMenu.addAction(StyleChange4)

        sshFile="style.css"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

        self.home()
        
    def home(self):
        self.btn=[]
        self.btnB=[]
        self.btn.append(QPushButton("Hit", self))
        self.btn.append(QPushButton("Stand", self))
        self.btnB.append(QPushButton("Bet 0,20 €", self))
        self.btnB.append(QPushButton("Bet 0,50 €", self))
        self.btnB.append(QPushButton("Bet 1 €", self))
        self.btnB.append(QPushButton("Bet 2 €", self))
        
        self.resize()
        self.var_bet = 0.2
        self.var_money=100
        self.pic = []
        self.drawn = 0
        self.picIndex = 0
        self.indent=[150, 150]
        self.play_test = 1
        self.oneOrTwoCards = 0
        # FIrst is player 2nd is dealer
        self.btnB[0].clicked.connect(lambda: self.bet(0.2, 0))
        self.btnB[0].resize(100, 50)
        self.btnB[0].move(200,  100)
        self.btnB[0].setEnabled(True)
        self.btnB[0].setStyleSheet("background-color:black;color:white;")
        self.btnB[0].setShortcut("1")
        
        self.btnB[2].clicked.connect(lambda: self.bet(1, 2))
        self.btnB[2].resize(100, 50)
        self.btnB[2].move(400,  100)
        self.btnB[2].setEnabled(True)
        self.btnB[2].setShortcut("3")
        
        self.btnB[1].clicked.connect(lambda: self.bet(0.5, 1))
        self.btnB[1].resize(100, 50)
        self.btnB[1].move(300,  100)
        self.btnB[1].setEnabled(True)
        self.btnB[1].setShortcut("2")
        
        self.btnB[3].clicked.connect(lambda: self.bet(2, 3))
        self.btnB[3].resize(100, 50)
        self.btnB[3].move(500,  100)
        self.btnB[3].setEnabled(True)
        self.btnB[3].setShortcut("4")
        
        self.btn[0].clicked.connect(self.play)
        self.btn[0].resize(100, 50)
        self.btn[0].move(100,  100)
        self.btn[0].setShortcut("h")
       
        self.btn[1].clicked.connect(self.stand)
        self.btn[1].move(0,  100)
        self.btn[1].resize(100, 50)
        self.btn[1].setShortcut("S")
        self.money = QLabel(("Money %s €"%(str(self.var_money))), self)
        self.money.setStyleSheet(("background-color: white;"))
        
        self.money.move(100, 50)
        self.money.resize(120,  20)
        self.player = QLabel("", self)
        self.player.setStyleSheet(("background-color: transparent;"))
        
        self.player.move(100, 400)
        self.player.resize(400,  50)
        
        self.dealer = QLabel("", self)
        
        self.dealer.move(100, 720)
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
    def play(self):
        if self.play_test == 1:
            self.hitMe()
            #HITME
        elif self.play_test == 2:
            self.restart()
            #RESTART
    def empty(self):
        global drawnCards, cardValue, win, charlie
        for i in range(0, len(self.pic)):
            self.pic[i].resize(0, 0)
        self.indent[0], self.indent[1], self.picIndex, self.pic, cardValue, drawnCards=150, 150, 0, [], [[], []], [[], []]
        win=0
        charlie=0
    def resize(self):
        self.btn[1].setEnabled(False)
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(False)
    def bet(self, n, index):
        self.var_bet=n
        for i in range(0, 4):
            self.btnB[i].setStyleSheet("background-color:none;")
        self.btnB[index].setStyleSheet("background-color:black;color:white;")
        if self.var_bet>self.var_money:
            self.var_bet=self.var_money
        if self.var_bet<0:
            self.var_bet=0
#        self.resize()
#        self.btn[0].resize(100, 50)
#    def bet(self, n):
#        global bet, money
#        bet=n
#        if bet>money:
#            bet=money
#        if bet<0:
#            bet=0
#        self.resize()
#        self.btn[0].resize(100, 50)
    def cardDraw(self, handLength, OneOrTwo, plyr, name, indentIndex, line):
        global win, drawnCards, cardValue, charlie
        hand=[]
        # maby make range 0, n?
        for i in range(0, handLength):
            hand.append(cardDeck[self.drawn])
            drawnCards[plyr].append(cardDeck[self.drawn])
            self.pic.append(QLabel(self))
            self.pic[self.picIndex].setPixmap(QPixmap("img/%s.svg"%(cardDeck[self.drawn])))
            self.pic[self.picIndex].setGeometry(self.indent[indentIndex], line, 169, 245)
            self.indent[indentIndex]+=50
            self.pic[self.picIndex].show()
            self.picIndex+=1
            
            self.drawn+=1
        for i in range(0, OneOrTwo):
            if "Ace" in hand[i]:
                cardValue[plyr].append(11)
            elif hand[i][:1] in ("Q", "J", "K"):
                cardValue[plyr].append(10)
            else:
                cardValue[plyr].append(int(hand[i][0:2])) #0:2 takes the 2 first letters from the string
        self.testForAces(plyr)
        if OneOrTwo==2:
            if sum(cardValue[plyr])==21:
                card="%s got a %s and a %s \nWich is a blackjack"%(name, hand[0], hand[1])
                win=1
                self.check()
            else:
                card="%s got a %s and a %s \nWich is a total of %s"%(name, hand[0], hand[1], sum(cardValue[plyr]))
            self.player.setText(card)
            self.player.setStyleSheet(("background-color: white;"))
        elif OneOrTwo==1:
            if len(cardValue[plyr])>=5 and sum(cardValue[plyr])<=21 and plyr == 1: # ADD KRAV NOT OVER 21 and only for player
                card="%s got a %s wich is a five card Charlie"%(name, hand[0])
                charlie=1
                self.check()
            elif sum(cardValue[plyr])==21:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
                self.resize()
                if plyr!=0:
                    self.stand()
            elif sum(cardValue[plyr])>=22:
#                print(cardDeck[self.drawn-1])
#                print(hand[0])
                #DEBUG THIS
                card="%s got a %s wich is %s and got busted"%(name, hand[0], sum(cardValue[plyr]))
                self.resize()
                if plyr==1:
                    self.check()
                self.play_test = 2
                self.enableBet()
            else:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
            if plyr==0:
                self.dealer.setText(card)
                self.dealer.setStyleSheet(("background-color: white;"))
            else:
                self.player.setText(card)
                self.player.setStyleSheet(("background-color: white;"))
    def testForAces(self, plyr):
        if sum(cardValue[plyr])>=22:
            for i in range(0, len(cardValue[plyr])):
                if "Ace" in drawnCards[plyr][i]:
                    if cardValue[plyr][i]==1:
                        continue
                    else:
                        cardValue[plyr][i]=1
                        break
    def check(self):
        global win, cardValue, drawnCards, charlie
        self.var_money=round(self.var_money, 2)
        if win == 1:
            print("OK BLACKJACK")
            self.var_money+=self.var_bet*1.5
            self.money.setText("Money %s €"%(str(self.var_money)))
            self.win.setText("You won")
        elif charlie == 1:
            print("CHARILIE")
            self.var_money+=self.var_bet
            self.money.setText("Money %s €"%(str(self.var_money)))
            self.win.setText("You won")
        elif sum(cardValue[1])==sum(cardValue[0]):
            print("TIE")
            self.win.setText("Tie")
        elif (sum(cardValue[1])>=22 or sum(cardValue[1])<sum(cardValue[0])) and not sum(cardValue[0])>=22:
            print("LOOSE")
            self.var_money-=self.var_bet
            self.money.setText("Money %s €"%(str(self.var_money)))
            self.win.setText("Dealer won")
        elif (sum(cardValue[0])>=22 or sum(cardValue[1])>sum(cardValue[0])) and not sum(cardValue[1])>=22:
            print("WIN")
            self.var_money+=self.var_bet
            self.money.setText("Money %s €"%(str(self.var_money)))
            self.win.setText("You won")
        self.win.setStyleSheet(("background-color: white;"))
        shuffle(cardDeck)
#        print(cardDeck)
        drawnCards, cardValue, self.oneOrTwoCards, win, self.drawn=[[], []], [[], []], -1, 0, 0
        self.resize()
        self.play_test = 2
        self.enableBet()
    def enableBet(self):
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(True)
    def restart(self):
        self.resize()
        self.play_test = 1
        self.win.setText("")
        self.dealer.setText("")
        self.player.setText("")
        self.dealer.setStyleSheet(("background-color: transparent;"))
        self.player.setStyleSheet(("background-color: transparent;"))
        self.win.setStyleSheet(("background-color: transparent;"))
        self.empty()
        self.hitMe()
    def stand(self):
        self.resize()
        while True:
            if sum(cardValue[0])<=16 and sum(cardValue[1])!=0 and sum(cardValue[1])<=22:
                self.cardDraw(1, 1, 0, "Dealer",1 , 470)
            else:
                self.resize()
                self.play_test = 2
                self.enableBet()
                self.check()
                break
    def style_set(self, n):
        QApplication.setStyle(QStyleFactory.create(n))
    def hitMe(self):
        # TRY INSTEAD TRY IF ONEORTWO EXIST IF EXIST IT RUN ELIF EXCEPTION IT CRATE VARIABLE AND RUN FIRST ONE AND ON RESTART IT DELETE VARIABLE
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(False)
        print(self.oneOrTwoCards)
#        if self.oneOrTwoCards<=-1:
#            self.oneOrTwoCards=0
        if self.oneOrTwoCards<=0:
            self.oneOrTwoCards=0
        if self.oneOrTwoCards==0:
            self.btn[1].setEnabled(True)
            self.cardDraw(2, 2, 1, "You",0 , 150)
            self.cardDraw(1, 1, 0, "Dealer",1 , 470)
        elif self.oneOrTwoCards>0:
            self.cardDraw(1, 1, 1, "You", 0, 150)
        self.oneOrTwoCards+=1
        self.var_money=round(self.var_money, 2)
        self.money.setText("Money %s €"%(str(self.var_money)))
drawnCards=[[], []]
cardValue=[[], []]
cardDeck=[]
ans=6
#Put in ans how many decks you want to play with
for a in range(0, ans):
    for j in ("Hearts", "Diamonds", "Spades", "Clubs"):
        for i in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"):
            cardDeck.append("%s of %s"%(i, j))
shuffle(cardDeck)
#print(cardDeck)
#print(cardDeck)
#for i in range(0, 200):
#    cardDeck[i]="Ace of Spades"
win = 0
charlie=0
# COMBINE THESE TWO list called win eller dict
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())
