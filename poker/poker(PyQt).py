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
#make locked buttons more grayed out typ gray background
#SQLITE CONNECT efter man enter uname password and click button (maby only uname)
# sen också create user password
# sen save sku UPDATE rowen
# story in game pay bank debt 1 k easy 5 k med 10 k hard in 3 H maby more if needed
# MAke att dina money blir removed före du ha change cards att du inte kan cheat de system save game mid hand
# Add possibility to delete a load save
# When a item has BG color black set text color WHITE
# https://stackoverflow.com/questions/9764298/is-it-possible-to-sort-two-listswhich-reference-each-other-in-the-exact-same-w
import sys
import fnmatch
import sqlite3 as lite
from random import shuffle
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow, QStyleFactory, QInputDialog
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
        self.saveFile.setStatusTip('Save File')
        self.saveFile.triggered.connect(self.file_save)
        self.saveFile.setEnabled(False) 
        
        self.loadFile = QAction("&Load File", self)
        self.loadFile.setShortcut("Ctrl+L")
        self.loadFile.setStatusTip('Load File')
        self.loadFile.triggered.connect(self.load_file)
        
        
        self.statusBar().showMessage('Message in statusbar.')  

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
        self.start.setStyleSheet('font-size: 100px;')
        
        self.delete = QPushButton("Delete", self)
        #self.delete.clicked.connect(self.deletesave)
        self.delete.resize(500, 300)
        self.delete.move(700, 200)
        self.delete.setStyleSheet('font-size: 100px;')
        
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
        self.changeCard=["1", "2", "3", "4", "5"]
        self.drawn = 0
        self.p1 = 0
        self.indent=100
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
        
    def loadsave(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:\n(Enter a new name to create new user\nEnter previous name to load)') 
        print(text)
        print(ok)
        if ok:
            con = None
            try:
                con = lite.connect('player.db')
                cur = con.cursor()    
                cur.execute("SELECT * FROM player")
                
            except:
                cur.execute("CREATE TABLE player(Id INTEGER PRIMARY KEY, Name TEXT, Money REAL);")

            finally:
                
                if con:
                    con.close()
                    
            self.name = text

            con = lite.connect('player.db')

            with con:    
                cur = con.cursor()
                cur.execute("SELECT * FROM player")
                rows = cur.fetchall()
                exists = 0
                for row in rows:
                    if row[1]==self.name:
                        exists=1
                if exists == 0:
                    cur.execute("INSERT INTO player(Name,Money) VALUES ('%s',100);" % (self.name))
                cur.execute("SELECT Money FROM player WHERE Name=='%s'" % self.name)
                cur.execute("SELECT Money FROM player WHERE Name=='%s'" % self.name)
                rows = cur.fetchall()
                for row in rows:
                    self.var_money = row[0]
                    self.money.setText("Money %s €"%(str(self.var_money)))
                    self.saveFile.setEnabled(True) 
            self.start.resize(0, 0)
            self.delete.resize(0, 0)
            self.btn.resize(100, 50)
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
    def play(self):
        if self.play_test == 1:
            self.deal()
        elif self.play_test == 2:
            self.continueG()
        elif self.play_test == 3:
            self.restart()
        self.play_test+=1
        if self.play_test == 4:
            self.play_test=2
            
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
        cards = ("Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Joker")
        for x in range(0, len(cards)):
            for i in range(0, 5):
                if cards[x][0:2] in self.card[i][0:2]:
                    if self.card[i][0:2] not in ranks:
                        if cards[x] is not "Joker":
                            pair[i]=(fnmatch.filter(self.card, '%s*'%(cards[x])))
                            cardValues[i]=x+1
                        ranks[i]=self.card[i][0:2]
        print(pair)
        print(cardValues)
        print(ranks)
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
        print(pair)
        print(cardValues)
        print(ranks)
        while len(pair)!=5:
            pair.append(False)
            ranks.append(False)
            cardValues.append(False)

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
        print(pair)
        print(cardValues)
        print(ranks)
#        if cardValues[0]+3==cardValues[1]+2==cardValues[2]+1==cardValues[3]==13 and suits[4]==1:
#            print("ACE IS JOKER")
        print(cardValues[2])
        print(cardValues[1])
        print(cardValues[0])
        print(suits[4])
        if cardValues[2]==cardValues[1]+2==cardValues[0]+3 and suits[4]==2:
            print("OK")
        # This should now work ment testa endå alla diffrent combinations
        # FIND OUT WHY CARD VALUES HAR 2 false i start and not after sen måst du change alla rader med joker att det lägsta 0 högsta de högsta
        # because it is sorted false is allways first men not to worry it is not a problem
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
            self.var_money+=self.var_bet*976
            self.tWon+=self.var_bet*976
            win="And won %s €"%(round(self.var_bet*976, 2))
        elif (5 in pair) or (4 in pair and suits[4]==1) or (3 in pair and suits[4]==2):
            # MABY HERE DO same som i pari 4 for i in range whatever tar mindre rader
            if ranks[0] == "Joker":
                if ranks[1] == "Joker":
                    playerChoice="You got five of "+str(ranks[2]+"'s")
                else:
                    playerChoice="You got five of "+str(ranks[1]+"'s")
            else:
                playerChoice="You got five of "+str(ranks[0]+"'s")
            self.var_money+=self.var_bet*976
            self.tWon+=self.var_bet*976
            win="And won %s €"%(round(self.var_bet*976, 2))
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
            print(cardValues)
            print(suit)
            playerChoice="You got a straight flush in "+str(suit[0])
            self.var_money+=self.var_bet*200
            self.tWon+=self.var_bet*200
            win="And won %s €"%(round(self.var_bet*200, 2))
        elif (4 in pair) or (3 in pair and suits[4]==1) or (2 in pair and suits[4]==2):
            for i in range(0, 4):
                print(pair)
                if (pair[i]==4) or (pair[i]==3 and suits[4]==1) or (pair[i]==2 and suits[4]==2) :
                    playerChoice="You got four of a kind with "+str(ranks[i]+"'s")
                    self.var_money+=self.var_bet*50
                    self.tWon+=self.var_bet*50
                    win="And won %s €"%(round(self.var_bet*50, 2))
        elif (3 in pair and 2 in pair) or (2 in pair and 2 in pair and suits[4]==1):
            I=1
            print(pair)
            print(suits)
            print("HERE")
            for i in range(0, 2):
                if (pair[i]==3 and pair[I]==2) or (pair[i]==2 and pair[I]==2 and suits[4]==1):
                    playerChoice="You got a full house with three "+str(ranks[i]+"'s and two ")+str(ranks[I]+"'s")  
                    self.var_money+=self.var_bet*25
                    self.tWon+=self.var_bet*25
                    win="And won %s €"%(round(self.var_bet*25, 2))
                I-=1
        elif suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a flush in "+str(suit[0])
            self.var_money+=self.var_bet*15
            self.tWon+=self.var_bet*15
            win="And won %s €"%(round(self.var_bet*15, 2))
        # THIS ONE WILL HAVE MANY DIFFRENT POSSIBILITES 5 olika med ace and 5 olika utan single jack and med 2 jack 10 på båda?
        elif (cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 )or \
            (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1):
            playerChoice="You got a straight"
            self.var_money+=self.var_bet*10
            self.tWon+=self.var_bet*10
            win="And won %s €"%(round(self.var_bet*10, 2))
        elif 3 in pair:
            for i in range(0, 3):
                if pair[i]==3:
                    playerChoice="You got a tripple of "+str(ranks[i]+"'s")
                    self.var_money+=self.var_bet*4
                    self.tWon+=self.var_bet*4
                    win="And won %s €"%(round(self.var_bet*4, 2))
                    
        elif pair.count(2)==2:
            II,I=0,1
            for i in range(0, 3):
                if pair[II]==2 and pair[I]==2:
                    playerChoice="You got two pairs one of "+str(ranks[II]+"'s")+str(" and one of ")+str(ranks[I]+"'s")
                    self.var_money+=self.var_bet*2
                    self.tWon+=self.var_bet*2
                    win="And won %s €"%(round(self.var_bet*2, 2))
                if I==1:
                    I+=1
                elif I==2:
                    II+=1
        elif 2 in pair:
            for i in range(0, 5):
                if pair[i]==2:
                    playerChoice="You got a pair of "+str(ranks[i]+"'s")
#                    if ranks[i][:1] in ("Q", "J", "K", "A"):
#                        win="And lost nothing"
#                    else:
#uncomment this and indent money- bet and win= for no loss with jacks or beter
                    self.tLos+=self.var_bet
                    win="And lost %s €"%(round(self.var_bet, 2))
        elif "Ace" in ranks:
            playerChoice="You got an Ace high"
            self.tLos+=self.var_bet
            win="And lost %s €"%(round(self.var_bet, 2))
        elif "King" in ranks:
            playerChoice="You got a King high"
            self.tLos+=self.var_bet
            win="And lost %s €"%(round(self.var_bet, 2))
            
        elif "Queen" in ranks:
            playerChoice="You got a Queen high"
            self.tLos+=self.var_bet
            win="And lost %s €"%(round(self.var_bet, 2))
        elif "Jack" in ranks:
            playerChoice="You got a Jack high"
            self.tLos+=self.var_bet
            win="And lost %s €"%(round(self.var_bet, 2))
        else:
            playerChoice=str("You got a ")+str(max(cardValues))+str(" high")
            self.tLos+=self.var_bet
            win="And lost %s €"%(round(self.var_bet, 2))
        print(ranks)
        self.player.setText(playerChoice)
        self.player.setStyleSheet(("background-color: white;"))
        self.dealer.setText(win)
        self.dealer.setStyleSheet(("background-color: white;"))
        print(playerChoice)
        self.var_money=round(self.var_money, 2)
        self.money.setText("Money %s €"%(str(self.var_money)))
        for i in range(0, len(self.btnB)):
            self.btnB[i].setEnabled(True) 
    def empty(self):
        for i in range(0, len(self.pic)):
            self.pic[i].resize(0, 0)
        self.indent, self.p1, self.pic=100, 0, []
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
        I = 1
        self.card = [ "Ace of Hearts", "Joker", "Joker", "Jack of Hearts","10 of Hearts"]
        for i in range(0, 5):
            self.pic.append(QLabel(self))
            self.pic[self.p1].setPixmap(QPixmap("img/%s.svg"%(self.card[i])))
            self.pic[self.p1].setGeometry(self.indent, line, 169, 245)
            self.indent+=200
            self.pic[self.p1].show()
            self.p1+=1
            I+=1
        return self.card
    def restart(self):
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
        con = lite.connect('player.db')

        with con:    
            cur = con.cursor()
            print(self.var_money)
            print(self.name)
            cur.execute("UPDATE player SET Money=%s WHERE Name='%s'" % (self.var_money, self.name))
#            cur.execute("SELECT * FROM player WHERE Name=='%s'" % self.name)
#            rows = cur.fetchall()
#            for row in rows:
#                print(row)
        
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
        con = lite.connect('player.db')

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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())
