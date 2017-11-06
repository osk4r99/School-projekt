#try adding fixe card charile o
#och om man har 2 kort så blir en split button size 150,50 
#Same for double down en double down button blir 100, 50 om man har en card value på mindre än 11s

#Före du börjar do 2 player graphical version try the logic in txt base programming first
#Och also make it convinient så att man kan use same functions med diffrent paraments for the mode to bet 2 players 
#Hell try to make it so dynamic att same code sku gå att use på 3 player eller hell 4
#See sentdex tutorials till slut ifall något mindblowing eller game changing tas up
#make till image att if this is first card but it here in first spot elif it is secound card put it here in secound spot elif elif elif
#try to make it dynamic att t.ex om firts card är ace of hearts så do den att den ser på card 1 och tar namet och
#add jpg eller png så du bara need en for loop

#eller att du att en secound deck som den testar all korten med dom du har och if true så do then same tar imagen till
#Matching card och sen ser den till att den move image to right place self.update() maby can help with that
#Try finding out how to add a widget after gamet har start
#MAby self.update is the key for that

import sys
from PyQt4 import QtGui,  QtCore
from random import shuffle
#MAKE BUTON SIZE 0, 0 NÄR MAN INTE SKALL KUNNA CLICK IT T.EX HIT OCH STAND ON DEALERS TURN SAMT NEXT ON OWN TURN
#START WITH GRAPHICAL TEXT BASED PROGRAM
#LATER ON ADD ATT MAN KAN SEE ACTUAL CARD ETC ETC
#maby test making button in a list

#Läs hur man print images

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QtGui.QIcon("favicon.ico.png"))
        
        Exit = QtGui.QAction("&Exit application", self)
        Exit.setShortcut("Ctrl+Alt+E")
        Exit.setStatusTip("Leave the app")
        Exit.triggered.connect(self.close_application)
        
        StyleChange1 = QtGui.QAction("&Style gtk+", self)
        StyleChange1.setShortcut("Ctrl+Alt+G")
        StyleChange1.setStatusTip("Change style to gtk+")
        StyleChange1.triggered.connect(self.style_set)
        
        StyleChange2 = QtGui.QAction("&Style Plastique", self)
        StyleChange2.setShortcut("Ctrl+Alt+P")
        StyleChange2.setStatusTip("Change style to Plastique")
        StyleChange2.triggered.connect(self.style_set2)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
        fileMenu.addAction(Exit)
        editMenu.addAction(StyleChange1)
        editMenu.addAction(StyleChange2)

        
        self.home()
        
    def home(self):
        global btn
        global money
        global pic
        btn=[]
        btn.append(QtGui.QPushButton("Hit", self))
        btn.append(QtGui.QPushButton("Stand", self))
        btn.append(QtGui.QPushButton("Continue", self))
        btn.append(QtGui.QPushButton("Restart?", self))
        btn.append(QtGui.QPushButton("Bet 10 €", self))
        btn.append(QtGui.QPushButton("Bet 50 €", self))
        btn.append(QtGui.QPushButton("Bet 100 €", self))
        btn.append(QtGui.QPushButton("Bet 1000 €", self))
        
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
        
        btn[0].clicked.connect(self.close_application)
        btn[0].resize(100, 50)
        btn[0].move(100,  100)
        
        btn[3].clicked.connect(self.restart)
        btn[3].move(100, 100)
        
        btn[2].clicked.connect(self.continueG)
        btn[2].move(100, 100)
       
        btn[1].clicked.connect(self.stand)
        btn[1].move(0,  100)
        self.money = QtGui.QLabel(("Money %s €"%(str(money))), self)
        
        self.money.move(100, 0)
        self.money.resize(400,  100)
        self.styleChoice = QtGui.QLabel("", self)
        
        self.styleChoice.move(50, 400)
        self.styleChoice.resize(400,  100)
        
        self.dealer = QtGui.QLabel("", self)
        
        self.dealer.move(50, 710)
        self.dealer.resize(400,  100)
        
        self.win = QtGui.QLabel("", self)
        
        self.win.move(400, 0)
        self.win.resize(400,  100)
        
        self.show()
    def empty(self):
        global cardsdranw, cardValue, indentP, pic, p1, indentD
        cardsdranw=[[], []]
        cardValue=[[], []]
        indentP=150
        for i in range(0, len(pic)):
            global pic
            pic[i].resize(0, 0)
        print(pic)
        pic=[]
        p1=0
        indentD=150
        print(pic)
    def resize(self):
        #The reason why I have buttons in lists is to make this easier
        for i in range(0, len(btn)):
            btn[i].resize(0, 0)
    def bet(self, n):
        global bet
        global money
        bet=n
        if bet>money:
            bet=money
        if bet<0:
            bet=0
        self.resize()
        btn[0].resize(100, 50)
    def cardDraw(self, drawncard, OneOrTwo, plyr, name, indent, line):
        global drawn, win
        global cardsdranw
        global cardValue
        global I
        global money
        global pic
        global p1
        hand=[]
        for i in range(drawn, drawncard):
            hand.append(cardDeck[drawn])
            cardsdranw[plyr].append(cardDeck[drawn])
            pic.append(QtGui.QLabel(self))
            pic[p1].setPixmap(QtGui.QPixmap("img/%s.svg"%(cardDeck[drawn])))
            pic[p1].setGeometry(indent, line, 209, 303)
            pic[p1].setGeometry(indent, line, 209, 303)
            print(indent)
            indent+=100
            #indent is 150
            #line is 100 
            #line is 503 for dealer
            pic[p1].show()
            p1+=1
            
            drawn+=1
        for i in range(0, OneOrTwo):
            if "Ace" in hand[i]:
                cardValue[plyr].append(11)
            elif "King" in hand[i] or "Queen" in hand[i] or "Jack" in hand[i]:
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
            self.styleChoice.setText(card)
        elif OneOrTwo==1:
            if sum(cardValue[plyr])==21:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
                self.resize()
                btn[2].resize(100, 50)
            elif sum(cardValue[plyr])>=22:
                card="%s got a %s wich is %s and got busted"%(name, cardDeck[drawn-1], sum(cardValue[plyr]))
                self.check()
                self.resize()
                btn[3].resize(100, 50)
            else:
                card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
            if plyr==0:
                self.dealer.setText(card)
            else:
                self.styleChoice.setText(card)
        return indent
    def testForAces(self, plyr):
        if sum(cardValue[plyr])>=22:
            for i in range(0, len(cardValue[plyr])):
                if "Ace" in cardsdranw[plyr][i]:
                    if cardValue[plyr][i]==1:
                        continue
                    else:
                        cardValue[plyr][i]=1
                        break
    def check(self):
        global win
        global money
        global cardValue
        global drawn
        global cardsdranw
        global I
        if win == 1:
            money+=bet*1.5
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        elif sum(cardValue[1])==sum(cardValue[0]):
            self.win.setText("Tie")
        elif sum(cardValue[1])>=22:
            money-=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("Dealer won")
        elif sum(cardValue[0])>=22:
            money+=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        elif sum(cardValue[1])>sum(cardValue[0]):
            money+=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("You won")
        else:
            money-=bet
            self.money.setText("Money %s €"%(str(money)))
            self.win.setText("Dealer won")
        drawn=0
        shuffle(cardDeck)
        print(cardDeck)
        cardsdranw=[[], []]
        cardValue=[[], []]
        I=-1
        win=0
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
        self.styleChoice.setText("")
        self.empty()
    def continueG(self):
        global drawn, indentD
        if sum(cardValue[0])>=17:
            self.resize()
            btn[3].resize(100, 50)
            self.check()
        else:
            indentD=self.cardDraw(drawn+1, 1, 0, "Dealer",indentD , 470)
        
    def stand(self):
        self.resize()
        btn[2].resize(100, 50)
        #This same code should run after dealer has played

        
    def style_set(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("gtk+"))
    def style_set2(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
    def close_application(self):
        global I
        global indentP, indentD
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
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
I=0
money=100
cardsdranw=[[], []]
cardValue=[[], []]
cardDeck=[]
color=["Hearts", "Diamonds", "Spades", "Clubs"]
card=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
for i in range(0,13):
    var="%s of %s"%(card[i], color[0])
    var2="%s of %s"%(card[i], color[1])
    var3="%s of %s"%(card[i], color[2])
    var4="%s of %s"%(card[i], color[3])
    cardDeck.extend((var, var2, var3, var4))
shuffle(cardDeck)
print(cardDeck)
drawn=0
win=0
indentP=150
indentD=150
pic=[]
p1=0
run()
