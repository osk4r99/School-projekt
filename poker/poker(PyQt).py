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

#PyQt5-Poker version 1.4

#Connect till database username password money
#SQLITE CONNECT efter man enter uname password and click button (maby only uname)
# sen också create user password
# sen save sku UPDATE rowen
# story in game pay bank debt 1 k easy 5 k med 10 k hard in 3 H maby more if needed
# Add possibility to delete a load save
# https://stackoverflow.com/questions/9764298/is-it-possible-to-sort-two-listswhich-reference-each-other-in-the-exact-same-w

# NOW JOKER WORKS DEN KAN INTE ENNU PIC RIGHT CARD NAME
#
# MAKE VINSTERNA ALLA LITE SÄMMRE OCH ADD TUPPLAUS MED EN VETTIG GRÄNS FÖR HUR MYCKET MAN MAX KAN FÅ

# Nu borde det fungera med jocker perfectly enda ner till triss där den ibland kan välja fel kort som par om du har 2 jokers same for par med 1 joker

# make save att det save also twon tlos set time elapsed in a variable och sen när man exit game tar 
# det total from time elapsed and current session time and print it out stating this is your total time
# 
#State the license for the card backs side in the start of the file somewhere ask tore
#
#
#räkna tLos and tWon i en statement if money-moneybefor > 0: is won else is los och då addas difference till tlos annors twon
#
#
#
import sys
import fnmatch
import sqlite3 as lite
from random import shuffle, choice
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow, QStyleFactory, QInputDialog, QMessageBox
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
        
        self.saveFile = QAction("&Save File", self)
        self.saveFile.setShortcut("Ctrl+S")
        self.saveFile.setStatusTip("Save File")
        self.saveFile.triggered.connect(self.file_save)
        self.saveFile.setEnabled(False) 
        
        self.loadFile = QAction("&Load File", self)
        self.loadFile.setShortcut("Ctrl+L")
        self.loadFile.setStatusTip("Load File")
        self.loadFile.triggered.connect(self.load_file)
        
        
        self.statusBar().showMessage("Message in statusbar.")  

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
        fileMenu.addAction(Exit)
        editMenu.addAction(StyleChange1)
        editMenu.addAction(StyleChange4)
        fileMenu.addAction(self.saveFile)
        fileMenu.addAction(self.loadFile)

        sshFile="style.css"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

        self.home()

    def home(self):
        self.btnC=[]
        self.btnB=[]
        self.btn = QPushButton("Deal", self)
        self.btnDouble = QPushButton("Double", self)
        self.btnRed = QPushButton("Red", self)
        self.btnBlack = QPushButton("Black", self)
        self.btnB.append(QPushButton("Bet 0,20 €", self))
        self.btnB.append(QPushButton("Bet 0,50 €", self))
        self.btnB.append(QPushButton("Bet 1 €", self))
        self.btnB.append(QPushButton("Bet 2 €", self))
        self.btnC.append(QPushButton("Hold", self))
        self.btnC.append(QPushButton("Hold", self))
        self.btnC.append(QPushButton("Hold", self))
        self.btnC.append(QPushButton("Hold", self))
        self.btnC.append(QPushButton("Hold", self))

        self.resize()
        
        self.start = QPushButton("Start", self)
        self.start.clicked.connect(self.loadsave)
        self.start.resize(500, 300)
        self.start.move(200, 200)
        self.start.setStyleSheet("font-size: 100px;")
        
        self.delete = QPushButton("Delete", self)
        self.delete.clicked.connect(self.deletesave)
        self.delete.resize(500, 300)
        self.delete.move(700, 200)
        self.delete.setStyleSheet("font-size: 100px;")
        
        self.btnC[0].clicked.connect(lambda: self.change("1"))
        self.btnC[0].move(130,  400)
        self.btnC[0].resize(0, 0)
        self.btnC[0].setEnabled(False)
        
        self.btnC[1].clicked.connect(lambda: self.change("2"))
        self.btnC[1].move(330,  400)
        self.btnC[1].resize(0, 0)
        self.btnC[1].setEnabled(False)

        self.btnC[2].clicked.connect(lambda: self.change("3"))
        self.btnC[2].move(530,  400)
        self.btnC[2].resize(0, 0)
        self.btnC[2].setEnabled(False)

        self.btnC[3].clicked.connect(lambda: self.change("4"))
        self.btnC[3].move(730,  400)
        self.btnC[3].resize(0, 0)
        self.btnC[3].setEnabled(False)

        self.btnC[4].clicked.connect(lambda: self.change("5"))
        self.btnC[4].move(930,  400)
        self.btnC[4].resize(0, 0)
        self.btnC[4].setEnabled(False)

        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(True) 
            
        self.btnB[0].clicked.connect(lambda: self.bet(0.2, 0))
        self.btnB[0].resize(0, 0)
        self.btnB[0].move(200,  100)
        self.btnB[0].setStyleSheet("background-color:black;color:white;")
        self.var_bet = 0.2
        self.var_money = 100
        self.tWon = 0 
        self.tLos = 0
        self.card = [0,0,0,0,0]
        self.pic = []
        self.pic2 = QLabel(self)
        self.changeCard=["1", "2", "3", "4", "5"]
        self.drawn = 0
        self.picIndex = 0
        self.indent=100
        self.toWin=0
        self.btnB[0].setEnabled(False)

        self.btnB[2].clicked.connect(lambda: self.bet(1, 2))
        self.btnB[2].resize(0, 0)
        self.btnB[2].move(400,  100)
        self.btnB[2].setEnabled(False)

        self.btnB[1].clicked.connect(lambda: self.bet(0.5, 1))
        self.btnB[1].resize(0, 0)
        self.btnB[1].move(300,  100)
        self.btnB[1].setEnabled(False)
    
        self.btnB[3].clicked.connect(lambda: self.bet(2, 3))
        self.btnB[3].resize(0, 0)
        self.btnB[3].move(500,  100)
        self.btnB[3].setEnabled(False)
        
        self.btn.clicked.connect(self.play)
        self.btn.resize(0, 0)
        self.btn.move(100,  100)
        self.btn.setEnabled(False)
        
        self.btnDouble.clicked.connect(self.double)
        self.btnDouble.resize(0, 0)
        self.btnDouble.move(0,  100)
        self.btnDouble.setEnabled(False)
        self.btnDouble.setShortcut("D")
        
        self.btnRed.clicked.connect(lambda: self.blackRed("R"))
        self.btnRed.resize(0, 0)
        self.btnRed.move(667,  700)
        self.btnRed.setEnabled(False)
        
        self.btnBlack.clicked.connect(lambda: self.blackRed("B"))
        self.btnBlack.resize(0, 0)
        self.btnBlack.move(400,  700)
        self.btnBlack.setEnabled(False)
        
        self.money = QLabel(("Money %s €"%(str(self.var_money))), self)
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

        self.play_test=1
    
        self.show()
    def double(self):
        self.btnBlack.resize(100, 50)
        self.btnRed.resize(100, 50)
        self.btnBlack.setEnabled(True)
        self.btnRed.setEnabled(True)
        self.btn.setEnabled(False)
        card="back"
        self.pic2.setPixmap(QPixmap("img/%s.svg"%(card)))
        self.pic2.setGeometry(500, 500, 169, 245)
        self.pic2.show()
    def blackRed(self, blackOrRed):
        self.btn.setEnabled(True)
        card=choice(("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King" ))
        suit=choice(("Hearts", "Spades", "Diamonds", "Clubs"))
        random="%s of %s" % (card, suit)
        self.pic2.setPixmap(QPixmap("img/%s.svg"%(random)))
        self.pic2.setGeometry(500, 500, 169, 245)
        self.pic2.show()
        print(random)
        # HERE YOU EITHER GET MORE MONEY OR LOOSE EVERYTHING
        #Gör att man ser sitt card om man van eller ej sen turn det back till back card
    def deletesave(self):
        text, ok = QInputDialog.getText(self, "Delete save", "Enter your name:\n(The name of your save)") 
        print(text)
        print(ok)
        if ok:
            con = None
            try:
                con = lite.connect("player.db")
                cur = con.cursor()    
                cur.execute("SELECT * FROM player")
                
            except:
                cur.execute("CREATE TABLE player(Id INTEGER PRIMARY KEY, Name TEXT, Money REAL, tLos REAL, tWon REAL);")

            finally:
                
                if con:
                    con.close()
                    
            self.name = text.lower()

            con = lite.connect("player.db")

            with con:    
                cur = con.cursor()
                cur.execute("SELECT * FROM player")
                rows = cur.fetchall()
                exists = 0
                for row in rows:
                    if row[1]==self.name:
                        exists=1
                        cur.execute("DELETE FROM player WHERE Name=='%s'" % self.name)
                if exists == 0:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Name not found")
                    msg.setWindowTitle("Error")
                    msg.exec_()
    def loadsave(self):
        text, ok = QInputDialog.getText(self, "Load save", "Enter your name:\n(This name will be used to identify your save)") 
        print(text)
        print(ok)
        if ok:
            con = None
            try:
                con = lite.connect("player.db")
                cur = con.cursor()    
                cur.execute("SELECT * FROM player")
                
            except:
                cur.execute("CREATE TABLE player(Id INTEGER PRIMARY KEY, Name TEXT, Money REAL, tLos REAL, tWon REAL);")

            finally:
                
                if con:
                    con.close()
                    
            self.name = text.lower()

            con = lite.connect("player.db")

            with con:    
                cur = con.cursor()
                cur.execute("SELECT * FROM player")
                rows = cur.fetchall()
                exists = 0
                for row in rows:
                    if row[1]==self.name:
                        exists=1
                if exists == 0:
                    cur.execute("INSERT INTO player(Name,Money,tLos,tWon) VALUES ('%s',100,0,0);" % (self.name))
                cur.execute("SELECT Money,tLos,tWon FROM player WHERE Name=='%s'" % self.name)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                    self.var_money = row[0]
                    self.tWon = row[2]
                    self.tLos = row[1]
                    self.money.setText("Money %s €"%(str(self.var_money)))
                    self.saveFile.setEnabled(True) 
            self.start.resize(0, 0)
            self.delete.resize(0, 0)
            self.btn.resize(100, 50)
            self.btnDouble.resize(100, 50)
            self.btn.setEnabled(True)
            self.btn.setShortcut("space")
            for i in range(0, len(self.btnC)):
                self.btnC[i].resize(100, 50)
                self.btnC[i].setShortcut("%s" % (i+1))
            for i in range(0, len(self.btnB)):
                self.btnB[i].resize(100, 50)
                self.btnB[i].setEnabled(True)
                self.btnB[i].setShortcut("%s" % (i+1))
            self.start.setEnabled(False)
            picIndex = 0
            indent=100
            card=["back", "back", "back", "back", "back"]
            for i in range(0, 5):
                self.pic.append(QLabel(self))
                self.pic[picIndex].setPixmap(QPixmap("img/%s.svg"%(card[i])))
                self.pic[picIndex].setGeometry(indent, 150, 169, 245)
                indent+=200
                self.pic[picIndex].show()
                picIndex+=1
    def play(self):
        if self.play_test == 1:
            self.restart()
        elif self.play_test == 2:
            self.continueG()
        self.play_test+=1
        if self.play_test == 3:
            self.play_test=1
            
    def continueG(self):
        suit, pair, ranks, cardValues = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
        ans=""
        for i in self.changeCard:
            ans+=i
        i=len(self.changeCard)-1
        while len(self.changeCard)!=0:
            self.changeCard.pop(i)
            i-=1
        self.empty()
        self.resize()
        self.card = self.cardPic(ans, 150)
        # why did changing fixing if not to != in the joker if statement 
        cards = ("Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Joker")
        for x in range(0, len(cards)):
            for i in range(0, 5):
                if cards[x][0:2] in self.card[i][0:2]:
                    if self.card[i][0:2] not in ranks:
                        if cards[x] != "Joker":
                            pair[i]=(fnmatch.filter(self.card, "%s*"%(cards[x])))
                            cardValues[i]=x+1
                        ranks[i]=self.card[i][0:2]
        for i in range(0, len(ranks)):
            if pair[i]!=0:
                pair[i]=len(pair[i])
        # Maby that cardValues pop is uneccesary 
        for x in range(0, 5):
            for i in range(0, len(pair)):
                if len(pair)<=i:
                    break
                if pair[i]==0:
                    pair.pop(i)
                    ranks.pop(i)
                    cardValues.pop(i)
        while len(pair)!=5:
            pair.append(None)
            ranks.append(None)
            cardValues.append(-10000)

        for i in range(0, 5):
            if "Spades" in self.card[i]:
                suit[i]="Spades"
            elif "Hearts" in self.card[i]:
                suit[i]="Hearts"
            elif "Clubs" in self.card[i]:
                suit[i]="Clubs"
            elif "Diamonds" in self.card[i]:
                suit[i]="Diamonds"
            elif "Joker" in self.card[i]:
                suit[i]="Joker"
#        suit = ["Clubs", "Clubs", "Clubs", "Clubs", "Clubs"]
#        if suit[0]==suit[1]==suit[2]==suit[3] and suit[4]=="Joker":
#            pass
        #Use this for printing how many pairs you have of each card
    #    for i in range(0, 5):
    #        if pair[i]!=None:
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
            elif "Jo" in str(ranks[i]):
                ranks[i]="Joker"
        suits=[0, 0, 0, 0, 0]
        if "Joker" in suit:
            # index 0 is hearts 1 is spades 2 is diamond 3 is clubs 4 is for jokers
            for i in suit:
                if i == "Spades":
                    suits[1]+=1
                elif i == "Clubs":
                    suits[3]+=1
                elif i == "Diamonds":
                    suits[2]+=1
                elif i == "Hearts":
                    suits[0]+=1
                elif i == "Joker":
                    suits[4]+=1
            for x in range(0, 4):
                for i in range(0, 5):
                    if suits[x] >= 3:
                        if suit[i] == "Joker":
                            if x == 0:
                                suit[i]="Hearts"
                            elif x == 1:
                                suit[i]="Spades"
                            elif x == 2:
                                suit[i]="Diamonds"
                            elif x == 3:
                                suit[i]="Clubs"
        cardValues.sort()
#        if cardValues[0]+3==cardValues[1]+2==cardValues[2]+1==cardValues[3]==13 and suits[4]==1:
#            print("ACE IS JOKER")
#        print(cardValues[2])
#        print(cardValues[1])
#        print(cardValues[0])
#        print(suits[4])
# JOKER SHOULD NOW WORK IN EVERY SCNEARIO BUT TEST SO THAT IT PRINTS RIGHT NAME FOR CARDS
        # This should now work ment testa endå alla diffrent combinations
        # FIND OUT WHY CARD VALUES HAR 2 false i start and not after sen måst du change alla rader med joker att det lägsta 0 högsta de högsta
        # because it is sorted false is allways first men not to worry it is not a problem
        #
        # Make function that does playerchoice win var_money ant tlos and twon
        # so it uses parameter to test if tlos or twon
        #
        #
        # Maby playerChoice didnt get set cuz 1 if sats blev triggered utan att det sen efter blev accepted
        #
        #
        print("Suit:")
        print(suit)
        print("ranks:")
        print(ranks)
        print("pair:")
        print(pair)
        print("cardValues:")
        print(cardValues)
        print("Cards:")
        print(self.card)
        print("Suits:")
        print(suits)
        playerChoice="THIS DIDNT WORK"
        if ((cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1 and suits[4]==0) or \
            (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and suits[4]==1) or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]+1==13 and suits[4]==1 and cardValues[1]==1) or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]==13 and suits[4]==1 and cardValues[1]==1) or \
            (cardValues[2]+3==cardValues[3]+1==cardValues[4]==13 and suits[4]==1 and cardValues[1]==1) or \
            (cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and suits[4]==1 and cardValues[1]==1) or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]+1==13 and suits[4]==2) or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[2]+3==cardValues[3]+1==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[3]+3==cardValues[4]+2==13 and suits[4]==2 and cardValues[2]==1) or \
            (cardValues[3]+3==cardValues[4]+1==13 and suits[4]==2 and cardValues[2]==1) or \
            (cardValues[3]+2==cardValues[4]+1==13 and suits[4]==2 and cardValues[2]==1) or \
            (cardValues[3]+3==cardValues[4]==13 and suits[4]==2 and cardValues[2]==1) or \
            (cardValues[3]+2==cardValues[4]==13 and suits[4]==2 and cardValues[2]==1) or \
            (cardValues[3]+1==cardValues[4]==13 and suits[4]==2 and cardValues[2]==1)  \
            )and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a straight royal flush in "+str(suit[0])
            self.toWin=self.var_bet*800
            self.tWon+=self.var_bet*800
            win="And won %s €"%(round(self.var_bet*800, 2))
            self.btnDouble.setEnabled(True)
        elif (5 in pair) or (4 in pair and suits[4]==1) or (3 in pair and suits[4]==2):
            # MABY HERE DO same som i pari 4 for i in range whatever tar mindre rader
            for i in range(0, 4):
               if (pair[i]==5) or (pair[i]==4 and suits[4]==1) or (pair[i]==3 and suits[4]==2) :
                    playerChoice="You got five of "+str(ranks[i]+"'s")
                    self.toWin=self.var_bet*800
                    self.tWon+=self.var_bet*800
                    win="And won %s €"%(round(self.var_bet*800, 2))
                    self.btnDouble.setEnabled(True)
                    break
        # IMPLEMENT SAME THING FROM STRAIGHT ROYAL FLUSH TO HERE
        elif ((cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 and suits[4]==0) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+3==cardValues[1]+4 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+3==cardValues[1]+4 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+3==cardValues[1]+4 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+4 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3 and suits[4]==1) or \
            (cardValues[4]+2==cardValues[3]+3==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+3==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+3 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+3==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+3 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+4 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+3 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2 and suits[4]==2)  \
            )and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a straight flush in "+str(suit[0])
            self.toWin=self.var_bet*50
            self.tWon+=self.var_bet*50
            win="And won %s €"%(round(self.var_bet*50, 2))
            self.btnDouble.setEnabled(True)
        elif (4 in pair) or (3 in pair and suits[4]==1) or (2 in pair and suits[4]==2):
            for i in range(0, 4):
                if (pair[i]==4) or (pair[i]==3 and suits[4]==1) or (pair[i]==2 and suits[4]==2) :
                    playerChoice="You got four of a kind with "+str(ranks[i]+"'s")
                    self.toWin=self.var_bet*10
                    self.tWon+=self.var_bet*10
                    win="And won %s €"%(round(self.var_bet*10, 2))
                    self.btnDouble.setEnabled(True)
                    break
        elif (3 in pair and 2 in pair) or (pair.count(2)==2 and suits[4]==1):
            I=1
            for i in range(0, 4):
                if (pair[i]==3 and pair[I]==2) or (pair[i]==2 and pair[I]==2 and suits[4]==1):
                    if suits[4] == 1:
                        bigger = max(cardValues)
                        smaller = 14
                        for i in range(0, 5):
                            if cardValues[i]!=None and cardValues[i]<=smaller:
                                smaller = cardValues[i]
                        if smaller==1:
                            bigger, smaller = smaller, bigger
                        if bigger == 1:
                            bigger="Ace"
                        elif bigger == 13:
                            bigger="King"
                        elif bigger == 12:
                            bigger="Queen"
                        elif bigger == 11:
                            bigger = "Jack"
                        if smaller == 13:
                            smaller="King"
                        elif smaller == 12:
                            smaller="Queen"
                        elif smaller == 11:
                            smaller = "Jack"
                        playerChoice="You got a full house with three "+str(bigger)+"'s and two "+str(smaller)+"'s"  
                    else:
                        playerChoice="You got a full house with three "+str(ranks[i]+"'s and two ")+str(ranks[I]+"'s")  
                    self.toWin=self.var_bet*7
                    self.tWon+=self.var_bet*7
                    win="And won %s €"%(round(self.var_bet*7, 2))
                    self.btnDouble.setEnabled(True)
                    break
                I-=1
        elif suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a flush in "+str(suit[0])
            self.toWin=self.var_bet*5
            self.tWon+=self.var_bet*5
            win="And won %s €"%(round(self.var_bet*5, 2))
            self.btnDouble.setEnabled(True)
        # Testa typ every combo du kan think of alla combon med ace to 10 alla med ace to 5 sen alla i mitten
        elif (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 )or \
            (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3 and suits[4]==1)or \
            (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+4 and suits[4]==1)or \
            (cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[1]==1 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+3==cardValues[1]+4 and suits[4]==1)or \
            (cardValues[2]+3==cardValues[3]+1==cardValues[4]==13 and cardValues[1]==1 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+3==cardValues[1]+4 and suits[4]==1)or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]==13 and cardValues[1]==1 and suits[4]==1) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+3==cardValues[1]+4 and suits[4]==1)or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]+1==13 and cardValues[1]==1 and suits[4]==1) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+2 and suits[4]==2)or \
            (cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+3 and suits[4]==2)or \
            (cardValues[2]+3==cardValues[3]+1==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+3 and suits[4]==2)or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]==13 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+3 and suits[4]==2)or \
            (cardValues[2]+3==cardValues[3]+2==cardValues[4]+1==13 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+1==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+1==cardValues[4]==13 and cardValues[2]==1 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+2==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+2==cardValues[4]==13 and cardValues[2]==1 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+2==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+2==cardValues[4]+1==13 and cardValues[2]==1 and suits[4]==2) or \
            (cardValues[4]==cardValues[3]+3==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+3==cardValues[4]==13 and cardValues[2]==1 and suits[4]==2) or \
            (cardValues[4]+1==cardValues[3]+3==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+3==cardValues[4]+1==13 and cardValues[2]==1 and suits[4]==2) or \
            (cardValues[4]+2==cardValues[3]+3==cardValues[2]+4 and suits[4]==2)or \
            (cardValues[3]+3==cardValues[4]+2==13 and cardValues[2]==1 and suits[4]==2):
            playerChoice="You got a straight"
            self.toWin=self.var_bet*4
            self.tWon+=self.var_bet*4
            win="And won %s €"%(round(self.var_bet*4, 2))
            self.btnDouble.setEnabled(True)
        elif (3 in pair) or (2 in pair and suits[4]==1) or (1 in pair and suits[4]==2):
            for i in range(0, 5):
                 if (pair[i]==3) or (pair[i]==2 and suits[4]==1) or (pair[i]==1 and suits[4]==2) :
                    playerChoice="You got a tripple of "+str(ranks[i]+"'s")
                    self.toWin=self.var_bet*2
                    self.tWon+=self.var_bet*2
                    win="And won %s €"%(round(self.var_bet*2, 2))
                    self.btnDouble.setEnabled(True)
                    break
                    
        elif pair.count(2)==2:
            II,I=0,1
            for i in range(0, 3):
                if pair[II]==2 and pair[I]==2:
                    playerChoice="You got two pairs one of "+str(ranks[II]+"'s")+str(" and one of ")+str(ranks[I]+"'s")
                    self.toWin=self.var_bet
                    self.tWon+=self.var_bet
                    win="And won %s €"%(round(self.var_bet, 2))
                    self.btnDouble.setEnabled(True)
                    break
                if I==1:
                    I+=1
                elif I==2:
                    II+=1
        elif (2 in pair) or (1 in pair and suits[4]==1):
            for i in range(0, 5):
                # add same thing here som i high card test
                if (pair[i]==2) or (pair[i]==1 and suits[4]==1):
                    playerChoice="You got a pair of "+str(ranks[i]+"'s")
#                    if ranks[i][:1] in ("Q", "J", "K", "A"):
#                        win="And lost nothing"
#                    else:
#uncomment this and indent money- bet and win= for no loss with jacks or beter
                    win="And lost %s €"%(round(self.var_bet, 2))
                    break
#        elif "Ace" in ranks:
#            playerChoice="You got an Ace high"
#            self.tLos+=self.var_bet
#            win="And lost %s €"%(round(self.var_bet, 2))
#        elif "King" in ranks:
#            playerChoice="You got a King high"
#            self.tLos+=self.var_bet
#            win="And lost %s €"%(round(self.var_bet, 2))
#            
#        elif "Queen" in ranks:
#            playerChoice="You got a Queen high"
#            self.tLos+=self.var_bet
#            win="And lost %s €"%(round(self.var_bet, 2))
#        elif "Jack" in ranks:
#            playerChoice="You got a Jack high"
#            self.tLos+=self.var_bet
#            win="And lost %s €"%(round(self.var_bet, 2))
        else:
            if "Ace" in ranks:
                playerChoice=str("You got a Ace high")
            elif "King" in ranks:
                playerChoice=str("You got a King high")
            elif "Queen" in ranks:
                playerChoice=str("You got a Queen high")
            elif "Jack" in ranks:
                playerChoice=str("You got a Jack high")
            else:
                playerChoice=str("You got a ")+str(max(cardValues))+str(" high")
            win="And lost %s €"%(round(self.var_bet, 2))
        self.player.setText(playerChoice)
        self.player.setStyleSheet(("background-color: white;"))
        self.dealer.setText(win)
        self.dealer.setStyleSheet(("background-color: white;"))
        print(playerChoice)
        self.var_money=round(self.var_money, 2)
        self.money.setText("Money %s €"%(str(self.var_money+self.toWin)))
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(True) 
    def empty(self):
        self.pic2.resize(0, 0)
        for i in range(0, len(self.pic)):
            self.pic[i].resize(0, 0)
        self.indent, self.picIndex, self.pic=100, 0, []
    def resize(self):
        for i in range(0, len(self.btnC)):
            self.btnC[i].setEnabled(False) 
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(False) 
    def bet(self, n, index):
        self.var_bet=n
        for i in range(0, 4):
            self.btnB[i].setStyleSheet("background-color:none;")
        self.btnB[index].setStyleSheet("background-color:black;color:white;")
#        self.card = self.cardPic(ans, 150)
    def deal(self):
        self.resize()
        for i in range(0, len(self.btnC)):
            self.btnC[i].setEnabled(True) 
        if self.var_bet>self.var_money:
            self.var_bet=self.var_money
        self.var_money -= self.var_bet
        self.tLos += self.var_bet
        self.var_money=round(self.var_money, 2)
        self.money.setText("Money %s €"%(str(self.var_money)))
        self.card = self.cardPic("12345", 150)

    def cardPic(self, ans, line):
        I = 1
        for i in range(0, 5):
            if str(I) in ans:
                self.card[i]=cardDeck[self.drawn]
                self.drawn+=1
            I+=1
#        self.card =  [ "3 of Spades","2 of Hearts","Joker", "3 of Clubs", "4 of Diamonds"]
#        self.card =  [ "3 of Spades","2 of Hearts","Joker", "4 of Clubs", "5 of Diamonds"]
        for i in range(0, 5):
            self.pic.append(QLabel(self))
            self.pic[self.picIndex].setPixmap(QPixmap("img/%s.svg"%(self.card[i])))
            self.pic[self.picIndex].setGeometry(self.indent, line, 169, 245)
            self.indent+=200
            self.pic[self.picIndex].show()
            self.picIndex+=1
        return self.card
    def restart(self):
        self.var_money+=self.toWin
        self.toWin=0
        self.btnDouble.setEnabled(False)
        self.resize()
        self.win.setText("")
        self.dealer.setText("")
        self.player.setText("")
        self.dealer.setStyleSheet(("background-color: transparent;"))
        self.player.setStyleSheet(("background-color: transparent;"))
        self.win.setStyleSheet(("background-color: transparent;"))
        self.empty()
        self.card = [0,0,0,0,0]
        shuffle(cardDeck)
        self.changeCard=["1", "2", "3", "4", "5"]
        self.btnC[0].setStyleSheet(("background-color: none;"))
        self.btnC[1].setStyleSheet(("background-color: none;"))
        self.btnC[2].setStyleSheet(("background-color: none;"))
        self.btnC[3].setStyleSheet(("background-color: none;"))
        self.btnC[4].setStyleSheet(("background-color: none;"))
        self.drawn=0
        self.deal()
    def style_set(self, n):
        QApplication.setStyle(QStyleFactory.create(n))
    def change(self, n):
        if str(n) in self.changeCard:
            temp=False
            for i in range(0, len(self.changeCard)):
                if self.changeCard[i] == n:
                    temp=i
            self.changeCard.pop(temp)
            self.btnC[int(n)-1].setStyleSheet("background-color:black;color:white;")
        else:
            self.changeCard.append(str(n))
            self.btnC[int(n)-1].setStyleSheet(("background-color: none;"))
    def file_save(self):
        con = lite.connect("player.db")

        with con:    
            cur = con.cursor()
            print(self.var_money)
            print(self.name)
            cur.execute("UPDATE player SET Money=%s, tLos=%s, tWon=%s WHERE Name='%s'" % (self.var_money, self.tLos, self.tWon ,  self.name))
            cur.execute("SELECT * FROM player WHERE Name=='%s'" % self.name)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getSaveFileName(self, "Save file",  "",
#                                                  "All Files (*);;Text Files (*.txt)", options=options)
#        if fileName:
#            print(fileName)
#        try:
#            file = open(fileName,'w')
#            file.write("%s\n%s\n%s"%(str(self.var_money), str(self.tWon), str(self.tLos)))
#            file.close()
#        except FileNotFoundError:
#            pass
    def load_file(self):
        con = lite.connect("player.db")

        with con:    
            cur = con.cursor()
            cur.execute("UPDATE player SET Money=%s WHERE Name='%s'" % (self.money, self.name))
            cur.execute("SELECT * FROM player WHERE Name=='%s'" % self.name)
            rows = cur.fetchall()
            for row in rows:
                print(row)
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getOpenFileName(self, "Load file",  "",
#                                                  "All Files (*);;Text Files (*.txt)", options=options)
#        if fileName:
#            print(fileName)
#        try:
#            file = open(fileName, "r")
#            content = file.readlines()
#            # you may also want to remove whitespace characters like `\n` at the end of each line
#            content = [x.strip() for x in content]
#            print(content)
#            self.var_money=int(content[0])
#            self.tWon=int(content[1])
#            self.tLos=int(content[2])
#            self.money.setText("Money %s €"%(str(self.var_money)))
#            #add here file.close() it may fix crashing error
#            file.close()
#        except FileNotFoundError:
#            pass
    def close_application(self):
        sys.exit()
    def closeEvent(self, event):
        print(event)
        # HERE YOU MAKE YES SAVE AND EXIT NO EXIT OCH CANCEL STAY IN GAME OCH IN MESSAGE BOX U PUT ALL STATISTIC HOW LONG YOU HAVE PLAYED ETC
        msgBox = QMessageBox()
        msgBox.setText("What to do?")
        cancel_button = msgBox.addButton("Cancel", QMessageBox.YesRole)
        no_button = msgBox.addButton("Exit without saving", QMessageBox.YesRole)        
        yes_button = msgBox.addButton("Save and Exit", QMessageBox.YesRole)        
        msgBox.exec_()
        if msgBox.clickedButton() == yes_button:
            self.file_save()
            sys.exit()
        elif msgBox.clickedButton() == no_button:
            sys.exit()  
        elif msgBox.clickedButton() == cancel_button:
            print("Response to warning: Cancel")   
            event.ignore()
        # MAKE SO WHEN YOU EXIT VIA MENU ELLER HERE SÅ OPEN EN FINAL POPUP MED STATISTICS OCH EN SAVE BUTTON IF IT WORKS

cardDeck = []
ans=1
#Put in ans how many decks you want to play with
for a in range(0, ans):
    for j in ("Hearts", "Diamonds", "Spades", "Clubs"):
        for i in ("Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"):
            cardDeck.append("%s of %s"%(i, j))
cardDeck.append("Joker")
cardDeck.append("Joker")
shuffle(cardDeck)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())
