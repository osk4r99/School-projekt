import sys
from PyQt4 import QtGui,  QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QtGui.QIcon("favicon.ico.png"))
        
        extractAction = QtGui.QAction("&Get TO THE CHOPPAAH", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)
        
        extractAction2 = QtGui.QAction("&Style gtk+", self)
        extractAction2.setShortcut("Ctrl+Alt+E")
        extractAction2.setStatusTip("Change style to gtk+")
        extractAction2.triggered.connect(self.style_set)
        
        extractAction4 = QtGui.QAction("&Style Plastique", self)
        extractAction4.setShortcut("Ctrl+Alt+W")
        extractAction4.setStatusTip("Change style to Plastique")
        extractAction4.triggered.connect(self.style_set2)
        
        extractAction3 = QtGui.QAction("&CMON HURRY UP", self)
        extractAction3.setShortcut("Ctrl+A")
        extractAction3.setStatusTip("Leave the app")
        extractAction3.triggered.connect(self.close_application)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu2 = mainMenu.addMenu("&Edit")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction3)
        fileMenu2.addAction(extractAction2)
        fileMenu2.addAction(extractAction4)

        
        self.home()
        
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        
        btn.resize(100, 100)
        btn.move(0, 100)
        
        
        extractAction = QtGui.QAction(QtGui.QIcon("ha.jpg"), "Flee the scene", self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)
        
        checkBox=QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(100, 25)
        checkBox.resize(150, 40)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        
        self.btn = QtGui.QPushButton("Download porn", self)
        self.btn.move(200, 120)
        self.btn.resize(150, 100)
        self.btn.clicked.connect(self.download)
        
        self.styleChoice = QtGui.QLabel("gtk+", self)
        
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("gtk+")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        
        comboBox.move(50, 250)
        self.styleChoice.move(50, 220)
        comboBox.activated[str].connect(self.style_choice)
        
        self.show()
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
    def style_set(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("gtk+"))
    def style_set2(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
    def download(self):
        self.completed=0
        
        while self.completed <99:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        choice = QtGui.QMessageBox.question(self, "Error", "Download failed", QtGui.QMessageBox.Ok)
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Extract!", "Get into the chopper?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting NOW")
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
run()
