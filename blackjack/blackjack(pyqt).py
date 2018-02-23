# Copyright (C) 2018 Oskar Öhman

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#PyQt5-BlackJack Version 1.1
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow
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
        global btn, money, pic
        btn=[]
        btn.append(QPushButton("Hit", self))
        btn.append(QPushButton("Stand", self))
        btn.append(QPushButton("Continue", self))
        btn.append(QPushButton("Restart?", self))
        btn.append(QPushButton("Bet 10 €", self))
        btn.append(QPushButton("Bet 50 €", self))
        btn.append(QPushButton("Bet 100 €", self))
        btn.append(QPushButton("Bet 1000 €", self))
        
        self.resize()
        
        btn[4].clicked.connect(lambda: self.bet(10))
        btn[4].resize(100, 50)
        btn[4].move(0,  100)
        
        btn[6].clicked.connect(lambda: self.bet(100))
        btn[6].resize(100, 50)
        btn[6].move(200,  100)
        
        btn[5].clicked.connect(lambda: self.bet(50))
        btn[5].resize(100, 50)
        btn[5].move(100,  100)
        
        btn[7].clicked.connect(lambda: self.bet(1000))
        btn[7].resize(100, 50)
        btn[7].move(300,  100)
        
        btn[0].clicked.connect(self.hitMe)
        btn[0].resize(100, 50)
        btn[0].move(100,  100)
        
        btn[3].clicked.connect(self.restart)
        btn[3].move(100, 100)
        
       
        btn[1].clicked.connect(self.stand)
        btn[1].move(0,  100)
        self.money = QLabel(("Money %s €"%(str(money))), self)
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
    def empty(self):
        global drawnCards, cardValue, indentP, pic, p1, indentD, win, charlie
        for i in range(0, len(pic)):
            pic[i].resize(0, 0)
        indentD, indentP, p1, pic, cardValue, drawnCards=150, 150, 0, [], [[], []], [[], []]
        win=0
        charlie=0
    def resize(self):
        for i in range(0, len(btn)):
            btn[i].resize(0, 0)
    def bet(self, n):
        global bet, money
        bet=n
        if bet>money:
            bet=money
        if bet<0:
            bet=0
        self.resize()
        btn[0].resize(100, 50)
    def cardDraw(self, drawncard, OneOrTwo, plyr, name, indent, line):
        global drawn, win, drawnCards, cardValue, I, money, pic, p1, charlie
        hand=[]
        for i in range(drawn, drawncard):
            hand.append(cardDeck[drawn])
            drawnCards[plyr].append(cardDeck[drawn])
            pic.append(QLabel(self))
            pic[p1].setPixmap(QPixmap("img/%s.svg"%(cardDeck[drawn])))
            pic[p1].setGeometry(indent, line, 169, 245)
            indent+=50
            pic[p1].show()
            p1+=1
            
            drawn+=1
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
            if len(cardValue[plyr])>=5:
                card="%s got a %s wich is a five card Charlie"%(name, hand[0])
                charlie=1
                self.check()
            elif sum(cardValue[plyr])==21:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
                self.resize()
                if plyr!=0:
                    self.stand()
            elif sum(cardValue[plyr])>=22:
                card="%s got a %s wich is %s and got busted"%(name, cardDeck[drawn-1], sum(cardValue[plyr]))
                self.resize()
                if plyr==1:
                    self.check()
                btn[3].resize(100, 50)
            else:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
            if plyr==0:
                self.dealer.setText(card)
                self.dealer.setStyleSheet(("background-color: white;"))
            else:
                self.player.setText(card)
                self.player.setStyleSheet(("background-color: white;"))
        return indent
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
        global win, money, cardValue, drawn, drawnCards, I, charlie
        if win == 1:
            money+=bet*1.5
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        elif charlie == 1:
            money+=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        elif sum(cardValue[1])==sum(cardValue[0]):
            self.win.setText("Tie")
        elif (sum(cardValue[1])>=22 or sum(cardValue[1])<sum(cardValue[0])) and not sum(cardValue[0])>=22:
            money-=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("Dealer won")
        elif (sum(cardValue[0])>=22 or sum(cardValue[1])>sum(cardValue[0])) and not sum(cardValue[1])>=22:
            money+=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        self.win.setStyleSheet(("background-color: white;"))
        shuffle(cardDeck)
        print(cardDeck)
        drawnCards, cardValue, I, win, drawn=[[], []], [[], []], -1, 0, 0
        self.resize()
        btn[3].resize(100, 50)
    def restart(self):
        self.resize()
        btn[4].resize(100, 50)
        btn[6].resize(100, 50)
        btn[7].resize(100, 50)
        btn[5].resize(100, 50)
        self.win.setText("")
        self.dealer.setText("")
        self.player.setText("")
        self.dealer.setStyleSheet(("background-color: transparent;"))
        self.player.setStyleSheet(("background-color: transparent;"))
        self.win.setStyleSheet(("background-color: transparent;"))
        self.empty()
    def stand(self):
        self.resize()
        global drawn, indentD
        while True:
            if sum(cardValue[0])<=16 and sum(cardValue[1])!=0 and sum(cardValue[1])<=22:
                indentD=self.cardDraw(drawn+1, 1, 0, "Dealer",indentD , 470)
            else:
                self.resize()
                btn[3].resize(100, 50)
                self.check()
                break
    def style_set(self, n):
        QWidget.QApplication.setStyle(QWidget.QStyleFactory.create(n))
    def hitMe(self):
        global I, indentP, indentD
        if I<=-1:
            I=0
        if I==0:
            btn[1].resize(100, 50)
            indentP=self.cardDraw(drawn+2, 2, 1, "You",indentP , 150)
            indentD=self.cardDraw(drawn+1, 1, 0, "Dealer",indentD , 470)
        elif I>0:
            indentP=self.cardDraw(drawn+1, 1, 1, "You", indentP, 150)
        I+=1
        self.money.setText("Money %s €"%(str(money)))
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
I=0
money=100
drawnCards=[[], []]
cardValue=[[], []]
cardDeck=[]
color=["Hearts", "Diamonds", "Spades", "Clubs"]
card=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
ans=6
#Put in ans how many decks you want to play with
for a in range(0, ans):
    for j in range(0, 4):
        for i in range(0,13):
            var="%s of %s"%(card[i], color[j])
            cardDeck.append(var)
shuffle(cardDeck)
print(cardDeck)
for i in range(0, 10):
    cardDeck[i]="Ace of Spades"
indentP, indentD, pic, p1, win, drawn=150, 150, [], 0, 0, 0
charlie=0
run()
