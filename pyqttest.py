import sys
from PyQt4 import QtGui,  QtCore
from random import shuffle
#MAKE BUTON SIZE 0, 0 NÄR MAN INTE SKALL KUNNA CLICK IT T.EX HIT OCH STAND ON DEALERS TURN SAMT NEXT ON OWN TURN
#START WITH GRAPHICAL TEXT BASED PROGRAM
#LATER ON ADD ATT MAN KAN SEE ACTUAL CARD ETC ETC
#To reset deck maby add re shuffel deck och make drawn 0 again
#maby test making button in a list


#Make blackjack win
#SOMTHING IS WRONG RETHINK TESTEN OM DEALERN SKALL STOP

#First ask for bet typ 10 50 100 eller 1000 eller all in (MABY all in)
#Sen hide bet button så man inte kan change it
#Sen add hit button och stand button
#när man press stand så försvinner hit och stand och blir replaced med continue och din total stannar kvar i hörnet och
#en continue knapp addas för att dealern drawn new card

#När man en blir busted så do denn där reset alla variables och make alla buttons size(0,0) förutom bet buttons
def cardDraw(drawncard, OneOrTwo, plyr, name):
    global drawn
    global cardsdranw
    global cardValue
    global I
    global money
    hand=[]
    for i in range(drawn, drawncard):
        hand.append(cardDeck[drawn])
        cardsdranw[plyr].append(cardDeck[drawn])
        drawn+=1
    for i in range(0, OneOrTwo):
        if "Ace" in hand[i]:
            cardValue[plyr].append(11)
        elif "King" in hand[i] or "Queen" in hand[i] or "Jack" in hand[i]:
            cardValue[plyr].append(10)
        else:
            cardValue[plyr].append(int(hand[i][0:2])) #0:2 takes the 2 first letters from the string
    testForAces(plyr)
    if OneOrTwo==2:
        card="%s got a %s and a %s \nWich is a total of %s"%(name, hand[0], hand[1], sum(cardValue[plyr]))
        return card
    elif OneOrTwo==1:
        if sum(cardValue[plyr])>=22:
            card="%s got a %s wich is %s and got busted"%(name, cardDeck[drawn-1], sum(cardValue[plyr]))
            btn5.resize(100, 50)
            btn4.resize(0, 0)
            btn3.resize(0, 0)
            btn2.resize(0, 0)
            btn.resize(0, 0)
            
            return card
        else:
            card="%s got a %s wich is a total of %s"%(name, hand[0], sum(cardValue[plyr]))
            return card
def testForAces(plyr):
    if sum(cardValue[plyr])>=22:
        for i in range(0, len(cardValue[plyr])):
            if "Ace" in cardsdranw[plyr][i]:
                if cardValue[plyr][i]==1:
                    continue
                else:
                    cardValue[plyr][i]=1
                    break
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
        global btn2
        global btn3
        global btn4
        global btn5
        global money
        btn=(QtGui.QPushButton("Draw card", self))
        btn2= (QtGui.QPushButton("Stand", self))
        btn3=(QtGui.QPushButton("Continue", self))
        btn4=(QtGui.QPushButton("Restart?", self))
        btn5=(QtGui.QPushButton("Check?", self))
        btn.clicked.connect(self.close_application)
        btn.resize(100, 50)
        btn.move(100,  100)
        
        btn5.clicked.connect(self.check)
        btn5.resize(0, 0)
        btn5.move(100, 100)
        
        btn4.clicked.connect(self.restart)
        btn4.resize(0, 0)
        btn4.move(100, 100)
        btn3.clicked.connect(self.continueG)
        btn3.resize(0, 0)
        btn3.move(100, 100)
       
        btn2.clicked.connect(self.stand)
        btn2.move(0,  100)
        btn2.resize(100, 50)
        self.money = QtGui.QLabel(("Money %s"%(str(money))), self)
        
        self.money.move(100, 0)
        self.money.resize(400,  100)
        self.styleChoice = QtGui.QLabel("", self)
        
        self.styleChoice.move(50, 220)
        self.styleChoice.resize(400,  100)
        
        self.dealer = QtGui.QLabel("", self)
        
        self.dealer.move(50, 260)
        self.dealer.resize(400,  100)
        
        self.win = QtGui.QLabel("", self)
        
        self.win.move(50, 300)
        self.win.resize(400,  100)
        
        self.show()
    def check(self):
        global money
        global cardValue
        global drawn
        global cardsdranw
        global I
        if sum(cardValue[1])==sum(cardValue[0]):
            self.win.setText("Tie")
        elif sum(cardValue[1])>=22:
            money-=10
            self.money.setText("Money %s"%(str(money)))
            self.win.setText("Dealer won")
        elif sum(cardValue[0])>=22:
            money+=10
            self.money.setText("Money %s"%(str(money)))
            self.win.setText("You won")
        elif sum(cardValue[1])>sum(cardValue[0]):
            money+=10
            self.money.setText("Money %s"%(str(money)))
            self.win.setText("You won")
        else:
            money-=10
            self.money.setText("Money %s"%(str(money)))
            self.win.setText("Dealer won")
        drawn=0
        shuffle(cardDeck)
        print(cardDeck)
        cardsdranw=[[], []]
        cardValue=[[], []]
        I=0
        btn4.resize(100, 50)
        btn5.resize(0, 0)
    def restart(self):
        btn4.resize(0, 0)
        btn.resize(100, 50)
        btn2.resize(100, 50)
        self.win.setText("")
        self.dealer.setText("")
        self.styleChoice.setText("")

    def continueG(self):
        global drawn
        if sum(cardValue[0])>=17 or sum(cardValue[0])>sum(cardValue[1]):
            btn3.resize(0, 0)
            btn5.resize(100, 50)
        else:
            card=cardDraw(drawn+1, 1, 0, "Dealer")
            self.dealer.setText(card)
        
    def stand(self):
        btn.resize(0, 0)
        btn2.resize(0, 0)
        btn3.resize(100, 50)
        #This same code should run after dealer has played

        
    def style_set(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("gtk+"))
    def style_set2(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
    def close_application(self):
        global I
        if I==0:
            card=cardDraw(drawn+2, 2, 1, "Oskar")
        else:
            card=cardDraw(drawn+1, 1, 1, "Oskar")
        I+=1
        self.styleChoice.setText(card)
        self.money.setText("Money %s"%(str(money)))
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
run()
