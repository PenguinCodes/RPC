from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import random

class Ui_RockPaperScisor(object):
    def setupUi(self, RockPaperScisor):
        RockPaperScisor.setObjectName("RockPaperScisor")
        RockPaperScisor.resize(717, 594)
        font = QtGui.QFont()
        font.setPointSize(22)
        RockPaperScisor.setFont(font)
        self.rock = QtWidgets.QPushButton(RockPaperScisor)
        self.rock.setGeometry(QtCore.QRect(230, 170, 111, 111))
        self.rock.setStyleSheet("background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (1).png);")
        self.rock.setText("")
        self.rock.setObjectName("rock")
        self.paper = QtWidgets.QPushButton(RockPaperScisor)
        self.paper.setGeometry(QtCore.QRect(370, 170, 121, 111))
        self.paper.setAutoFillBackground(False)
        self.paper.setStyleSheet("background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (2).png);")
        self.paper.setText("")
        self.paper.setObjectName("paper")
        self.scissor = QtWidgets.QPushButton(RockPaperScisor)
        self.scissor.setGeometry(QtCore.QRect(520, 170, 121, 111))
        self.scissor.setMouseTracking(False)
        self.scissor.setAutoFillBackground(False)
        self.scissor.setStyleSheet("background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (3).png);")
        self.scissor.setText("")
        self.scissor.setObjectName("scissor")
        self.label = QtWidgets.QLabel(RockPaperScisor)
        self.label.setGeometry(QtCore.QRect(60, 50, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setLineWidth(32)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.botlabel = QtWidgets.QLabel(RockPaperScisor)
        self.botlabel.setGeometry(QtCore.QRect(290, 330, 261, 101))
        self.botlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botlabel.setText("")
        self.botlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.botlabel.setObjectName("botlabel")
        self.result = QtWidgets.QLabel(RockPaperScisor)
        self.result.setGeometry(QtCore.QRect(100, 480, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.label_4 = QtWidgets.QLabel(RockPaperScisor)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(RockPaperScisor)
        self.label_5.setGeometry(QtCore.QRect(60, 350, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(RockPaperScisor)
        QtCore.QMetaObject.connectSlotsByName(RockPaperScisor)
        def game(user):
            #user = input("Rock Paper or Scissors ?")
            tools = ["Rock", "Paper", "Scissor"]
            bot = tools[random.randrange(len(tools))]
            if bot == "Rock":
                self.botlabel.setStyleSheet("background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (1).png);")
            elif bot == "Paper":
                self.botlabel.setStyleSheet(
                    "background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (2).png);")

            else:
                self.botlabel.setStyleSheet(
                    "background-image: url(/home/pavan/PycharmProjects/untitled/venv/Webp.net-resizeimage (3).png);")

            print("Bot Picks ", bot)
            if user == bot:
                self.result.setText("Draw")
            elif user == "Rock":
                if bot == "Paper":
                    self.result.setText("I Win")
                else:
                    self.result.setText("You Win")
            elif user == "Paper":
                if bot == "Scissors":
                    self.result.setText("I Win")
                else:
                    self.result.setText("You Win")
            elif user == "Scissor":
                if bot == "Rock":
                    self.result.setText("I Wins")
                else:
                    self.result.setText("You Win")
            else:
                print("Choose Between Rock Paper And Scissors")
        self.rock.clicked.connect(partial(game, "Rock"))
        self.paper.clicked.connect(partial(game, "Paper"))
        self.scissor.clicked.connect(partial(game, "Scissor"))

    def retranslateUi(self, RockPaperScisor):
        _translate = QtCore.QCoreApplication.translate
        RockPaperScisor.setWindowTitle(_translate("RockPaperScisor", "RockPaperScissor"))
        self.rock.setToolTip(_translate("RockPaperScisor", "Rock"))
        self.paper.setToolTip(_translate("RockPaperScisor", "Paper"))
        self.scissor.setToolTip(_translate("RockPaperScisor", "Scissors"))
        self.label.setText(_translate("RockPaperScisor", "Rock Paper Scissor"))
        self.label_4.setText(_translate("RockPaperScisor", "You Choose"))
        self.label_5.setText(_translate("RockPaperScisor", "I Choose"))
#import r_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RockPaperScisor = QtWidgets.QWidget()
    ui = Ui_RockPaperScisor()
    ui.setupUi(RockPaperScisor)
    RockPaperScisor.show()
    sys.exit(app.exec_())
