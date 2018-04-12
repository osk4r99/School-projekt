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
import sys
import fnmatch
from random import shuffle
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QMainWindow, QStyleFactory, QFileDialog
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
        
        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        loadFile = QAction("&Load File", self)
        loadFile.setShortcut("Ctrl+L")
        loadFile.setStatusTip('Load File')
        loadFile.triggered.connect(self.load_file)
        
        self.statusBar().showMessage('Message in statusbar.')  

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        editMenu = mainMenu.addMenu("&Edit")
        fileMenu.addAction(Exit)
        editMenu.addAction(StyleChange1)
        editMenu.addAction(StyleChange4)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(loadFile)

        sshFile="style.css"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

        self.home()

    def home(self):
        global bet, money, pic, btnC, btnB
        btnC=[]
        btnB=[]
        btn = QPushButton("Deal", self)
        btnB.append(QPushButton("Bet 0,20 €", self))
        btnB.append(QPushButton("Bet 0,50 €", self))
        btnB.append(QPushButton("Bet 1 €", self))
        btnB.append(QPushButton("Bet 2 €", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))
        btnC.append(QPushButton("Hold", self))

        self.resize()

        btnC[0].clicked.connect(lambda: self.change("1"))
        btnC[0].move(130,  400)
        btnC[0].resize(100, 50)
        btnC[0].setShortcut("1")

        btnC[1].clicked.connect(lambda: self.change("2"))
        btnC[1].move(330,  400)
        btnC[1].resize(100, 50)
        btnC[1].setShortcut("2")

        btnC[2].clicked.connect(lambda: self.change("3"))
        btnC[2].move(530,  400)
        btnC[2].resize(100, 50)
        btnC[2].setShortcut("3")

        btnC[3].clicked.connect(lambda: self.change("4"))
        btnC[3].move(730,  400)
        btnC[3].resize(100, 50)
        btnC[3].setShortcut("4")

        btnC[4].clicked.connect(lambda: self.change("5"))
        btnC[4].move(930,  400)
        btnC[4].resize(100, 50)
        btnC[4].setShortcut("5")
        
        for i in range(0, len(btnB)):
            btnB[i].setEnabled(True) 
            
        btnB[0].clicked.connect(lambda: self.bet(0.2, 0))
        btnB[0].resize(100, 50)
        btnB[0].move(200,  100)
        btnB[0].setStyleSheet("background-color:black;")
        bet=0.2
        btnB[0].setShortcut("1")

        btnB[2].clicked.connect(lambda: self.bet(1, 2))
        btnB[2].resize(100, 50)
        btnB[2].move(400,  100)
        btnB[2].setShortcut("3")

        btnB[1].clicked.connect(lambda: self.bet(0.5, 1))
        btnB[1].resize(100, 50)
        btnB[1].move(300,  100)
        btnB[1].setShortcut("2")
    
        btnB[3].clicked.connect(lambda: self.bet(2, 3))
        btnB[3].resize(100, 50)
        btnB[3].move(500,  100)
        btnB[3].setShortcut("4")
        
        btn.clicked.connect(self.play)
        btn.resize(100, 50)
        btn.move(100,  100)
        btn.setShortcut("H")
        
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
        
        
    def play(self):
        global play_test
        if play_test == 1:
            self.deal()
        elif play_test == 2:
            self.continueG()
        elif play_test == 3:
            self.restart()
        play_test+=1
        if play_test == 4:
            play_test=2
            
            
    def continueG(self):
        global changeCard, card, bet, money, tWon, tLos
        bet=bet
        suit, pair, ranks, cardValues = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
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
        cards = ("Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
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
            money+=bet*976
            tWon+=bet*976
            win="And won %s €"%(round(bet*976, 2))
        elif 5 in pair:
            playerChoice="You got five of "+str(ranks[0]+"'s")
            money+=bet*976
            tWon+=bet*976
            win="And won %s €"%(round(bet*976, 2))
        elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 and suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a straight flush in "+str(suit[0])
            money+=bet*200
            tWon+=bet*200
            win="And won %s €"%(round(bet*200, 2))
        elif 4 in pair:
            for i in range(0, 2):
                if pair[i]==4:
                    playerChoice="You got four of a kind with "+str(ranks[i]+"'s")
                    money+=bet*50
                    tWon+=bet*50
                    win="And won %s €"%(round(bet*50, 2))
        elif 3 in pair and 2 in pair:
            I=1
            for i in range(0, 2):
                if pair[i]==3 and pair[I]==2:
                    playerChoice="You got a full house with three "+str(ranks[i]+"'s and two ")+str(ranks[I]+"'s")  
                    money+=bet*25
                    tWon+=bet*25
                    win="And won %s €"%(round(bet*25, 2))
                I-=1
        elif suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
            playerChoice="You got a flush in "+str(suit[0])
            money+=bet*15
            tWon+=bet*15
            win="And won %s €"%(round(bet*15, 2))
        elif cardValues[4]==cardValues[3]+1==cardValues[2]+2==cardValues[1]+3==cardValues[0]+4 or (cardValues[1]+3==cardValues[2]+2==cardValues[3]+1==cardValues[4]==13 and cardValues[0]==1):
            playerChoice="You got a straight"
            money+=bet*10
            tWon+=bet*10
            win="And won %s €"%(round(bet*10, 2))
        elif 3 in pair:
            for i in range(0, 3):
                if pair[i]==3:
                    playerChoice="You got a tripple of "+str(ranks[i]+"'s")
                    money+=bet*4
                    tWon+=bet*4
                    win="And won %s €"%(round(bet*4, 2))
                    
        elif pair.count(2)==2:
            II,I=0,1
            for i in range(0, 3):
                if pair[II]==2 and pair[I]==2:
                    playerChoice="You got two pairs one of "+str(ranks[II]+"'s")+str(" and one of ")+str(ranks[I]+"'s")
                    money+=bet*2
                    tWon+=bet*2
                    win="And won %s €"%(round(bet*2, 2))
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
                    money-=bet
                    tLos+=bet
                    win="And lost %s €"%(round(bet, 2))
        elif "Ace" in ranks:
            playerChoice="You got an Ace high"
            money-=bet
            tLos+=bet
            win="And lost %s €"%(round(bet, 2))
        elif "King" in ranks:
            playerChoice="You got a King high"
            money-=bet
            tLos+=bet
            win="And lost %s €"%(round(bet, 2))
            
        elif "Queen" in ranks:
            playerChoice="You got a Queen high"
            money-=bet
            tLos+=bet
            win="And lost %s €"%(round(bet, 2))
        elif "Jack" in ranks:
            playerChoice="You got a Jack high"
            money-=bet
            tLos+=bet
            win="And lost %s €"%(round(bet, 2))
        else:
            playerChoice=str("You got a ")+str(max(cardValues))+str(" high")
            money-=bet
            tLos+=bet
            win="And lost %s €"%(round(bet, 2))
        print(ranks)
        self.player.setText(playerChoice)
        self.player.setStyleSheet(("background-color: white;"))
        self.dealer.setText(win)
        self.dealer.setStyleSheet(("background-color: white;"))
        print(playerChoice)
        money=round(money, 2)
        self.money.setText("Money %s €"%(str(money)))
        for i in range(0, len(btnB)):
            btnB[i].setEnabled(True) 
    def empty(self):
        global drawnCards, cardValue, indent, pic, p1
        for i in range(0, len(pic)):
            pic[i].resize(0, 0)
        indent, p1, pic=100, 0, []
    def resize(self):
        for i in range(0, len(btnC)):
            btnC[i].setEnabled(False) 
        for i in range(0, len(btnB)):
            btnB[i].setEnabled(False) 
    def bet(self, n, index):
        global bet, money, card
        bet=n
        for i in range(0, 4):
            btnB[i].setStyleSheet("background-color:none;")
        btnB[index].setStyleSheet("background-color:black;")
#        card = self.cardPic(ans, card, 150)
    def deal(self):
        global card, bet, money
        self.resize()
        for i in range(0, len(btnC)):
            btnC[i].setEnabled(True) 
        if bet>money:
            bet=money
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
        global card, drawn, changeCard
        self.resize()
        self.win.setText("")
        self.dealer.setText("")
        self.player.setText("")
        self.dealer.setStyleSheet(("background-color: transparent;"))
        self.player.setStyleSheet(("background-color: transparent;"))
        self.win.setStyleSheet(("background-color: transparent;"))
        self.empty()
        card = [0,0,0,0,0]
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
    def file_save(self):
        global money, tLos, tWon
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save file",  "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
        try:
            file = open(fileName,'w')
            file.write("%s\n%s\n%s"%(str(money), str(tWon), str(tLos)))
            file.close()
        except FileNotFoundError:
            pass
    def load_file(self):
        global money, tWon, tLos
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Load file",  "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
        try:
            file = open(fileName, "r")
            content = file.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content]
            print(content)
            money=int(content[0])
            tWon=int(content[1])
            tLos=int(content[2])
            self.money.setText("Money %s €"%(str(money)))
            #add here file.close() it may fix crashing error
            file.close()
        except FileNotFoundError:
            pass
    def close_application(self):
        sys.exit()
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
changeCard=["1", "2", "3", "4", "5"]
drawn, cardDeck = 0, []
money=100
ans=1
#Put in ans how many decks you want to play with
for a in range(0, ans):
    for j in ("Hearts", "Diamonds", "Spades", "Clubs"):
        for i in ("Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"):
            cardDeck.append("%s of %s"%(i, j))
shuffle(cardDeck)
card = [0,0,0,0,0]
p1=0
tWon, tLos=0, 0
card.sort()
indent, pic, p1, win, drawn=100, [], 0, 0, 0
play_test=1
run()
