import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore


class MainWindow(qtw.QWidget):
    numberSelected=""
    operatorSelected=""
    result=0
    finalResult=0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("my pyQt app")
        self.setLayout(qtw.QVBoxLayout())
        self.setUI()

        self.show()

    def setUI(self):

        self.label = qtw.QLabel(self)
        self.labelResult = qtw.QLabel(self)
        self.labelResult.setText("0")

        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # create the buttons
        btn_1 = qtw.QPushButton('1', clicked=self.onClickNumber1)
        btn_2 = qtw.QPushButton('2', clicked=self.onClickNumber2)
        btn_3 = qtw.QPushButton('3', clicked=self.onClickNumber3)
        btn_4 = qtw.QPushButton('4', clicked=self.onClickNumber4)
        btn_5 = qtw.QPushButton('5', clicked=self.onClickNumber5)
        btn_6 = qtw.QPushButton('6', clicked=self.onClickNumber6)
        btn_7 = qtw.QPushButton('7', clicked=self.onClickNumber7)
        btn_8 = qtw.QPushButton('8', clicked=self.onClickNumber8)
        btn_9 = qtw.QPushButton('9', clicked=self.onClickNumber9)
        btn_0 = qtw.QPushButton('0', clicked=self.onClickNumber0)
        btn_plus = qtw.QPushButton('+', clicked=self.onClickOperatorPlus)
        btn_minus = qtw.QPushButton('-', clicked=self.onClickOperatorMinus)
        btn_mult = qtw.QPushButton('*', clicked=self.onClickOperatorMult)
        btn_div = qtw.QPushButton('/', clicked=self.onClickOperatorDiv)
        btn_enter = qtw.QPushButton('=', clicked=self.onClickEnter)
        btn_ce = qtw.QPushButton('CE', clicked=self.onClickCE)
        btn_c = qtw.QPushButton('C', clicked=self.onClickC)

        # add buttons to layout
        container.layout().addWidget(btn_7, 3, 0)
        container.layout().addWidget(btn_8, 3, 1)
        container.layout().addWidget(btn_9, 3, 2)

        container.layout().addWidget(btn_4, 4, 0)
        container.layout().addWidget(btn_5, 4, 1)
        container.layout().addWidget(btn_6, 4, 2)

        container.layout().addWidget(btn_1, 5, 0)
        container.layout().addWidget(btn_2, 5, 1)
        container.layout().addWidget(btn_3, 5, 2)

        container.layout().addWidget(btn_0, 6, 0, 1, 3)

        container.layout().addWidget(btn_plus, 3, 3)
        container.layout().addWidget(btn_minus, 4, 3)
        container.layout().addWidget(btn_mult, 5, 3)
        container.layout().addWidget(btn_div, 6, 3)

        container.layout().addWidget(btn_enter, 2, 0, 1, 2)
        container.layout().addWidget(btn_ce, 2, 2, 1, 1)
        container.layout().addWidget(btn_c, 2, 3, 1, 1)

        container.layout().addWidget(self.label, 0, 0, 1, 4)
        container.layout().addWidget(self.labelResult, 1, 0, 1, 4)

        self.layout().addWidget(container)

    def onClickNumber1(self):
        if self.result==0:
            screenResult = self.labelResult.text()
            if screenResult=="0":
                self.labelResult.setText("1")
            else:
                self.labelResult.setText(screenResult + "1")
        else:
            self.labelResult.setText("1")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 1

    def onClickNumber2(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("2")
            else:
                self.labelResult.setText(screenResult + "2")
        else:
            self.labelResult.setText("2")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected=2

    def onClickNumber3(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("3")
            else:
                self.labelResult.setText(screenResult + "3")
        else:
            self.labelResult.setText("3")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 3

    def onClickNumber4(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("4")
            else:
                self.labelResult.setText(screenResult + "4")
        else:
            self.labelResult.setText("4")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 4

    def onClickNumber5(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("5")
            else:
                self.labelResult.setText(screenResult + "5")
        else:
            self.labelResult.setText("5")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 5

    def onClickNumber6(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("6")
            else:
                self.labelResult.setText(screenResult + "6")
        else:
            self.labelResult.setText("6")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 6

    def onClickNumber7(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("7")
            else:
                self.labelResult.setText(screenResult + "7")
        else:
            self.labelResult.setText("7")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 7

    def onClickNumber8(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("8")
            else:
                self.labelResult.setText(screenResult + "8")
        else:
            self.labelResult.setText("8")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 8

    def onClickNumber9(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("9")
            else:
                self.labelResult.setText(screenResult + "9")
        else:
            self.labelResult.setText("9")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 9

    def onClickNumber0(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if screenResult == "0":
                self.labelResult.setText("0")
            else:
                self.labelResult.setText(screenResult + "0")
        else:
            self.labelResult.setText("0")
            self.result = 0
            if self.operatorSelected=="=":
                self.label.setText("")
        self.numberSelected = 0

    def onClickOperatorPlus(self):
        if self.result==0:
            screenResult = self.labelResult.text()
            if self.operatorSelected=="+":
                self.labelResult.setText(str(self.finalResult + int(screenResult)))
            elif self.operatorSelected=="-":
                self.labelResult.setText(str(self.finalResult - int(screenResult)))
            elif self.operatorSelected=="x":
                self.labelResult.setText(str(self.finalResult * int(screenResult)))
            elif self.operatorSelected=="/":
                self.labelResult.setText(str(self.finalResult // int(screenResult)))

            self.finalResult=int(self.labelResult.text())
            screen = self.label.text()
            self.label.setText(screen + screenResult + "+")
            self.operatorSelected = "+"
            self.result=1

    def onClickOperatorMinus(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if self.operatorSelected == "+":
                self.labelResult.setText(str(self.finalResult + int(screenResult)))
            elif self.operatorSelected == "-":
                self.labelResult.setText(str(self.finalResult - int(screenResult)))
            elif self.operatorSelected == "x":
                self.labelResult.setText(str(self.finalResult * int(screenResult)))
            elif self.operatorSelected == "/":
                self.labelResult.setText(str(self.finalResult // int(screenResult)))
            self.finalResult = int(self.labelResult.text())
            screen = self.label.text()
            self.label.setText(screen + screenResult + "-")
            self.operatorSelected = "-"
            self.result = 1

    def onClickOperatorMult(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if self.operatorSelected == "+":
                self.labelResult.setText(str(self.finalResult + int(screenResult)))
            elif self.operatorSelected == "-":
                self.labelResult.setText(str(self.finalResult - int(screenResult)))
            elif self.operatorSelected == "x":
                self.labelResult.setText(str(self.finalResult * int(screenResult)))
            elif self.operatorSelected == "/":
                self.labelResult.setText(str(self.finalResult // int(screenResult)))
            self.finalResult = int(self.labelResult.text())
            screen = self.label.text()
            self.label.setText(screen + screenResult + "x")
            self.operatorSelected = "x"
            self.result = 1

    def onClickOperatorDiv(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if self.operatorSelected == "+":
                self.labelResult.setText(str(self.finalResult + int(screenResult)))
            elif self.operatorSelected == "-":
                self.labelResult.setText(str(self.finalResult - int(screenResult)))
            elif self.operatorSelected == "x":
                self.labelResult.setText(str(self.finalResult * int(screenResult)))
            elif self.operatorSelected == "/":
                self.labelResult.setText(str(self.finalResult // int(screenResult)))
            self.finalResult = int(self.labelResult.text())
            screen = self.label.text()
            self.label.setText(screen + screenResult + "/")
            self.operatorSelected = "/"
            self.result = 1

    def onClickEnter(self):
        if self.result == 0:
            screenResult = self.labelResult.text()
            if self.operatorSelected == "+":
                self.labelResult.setText(str(self.finalResult + int(screenResult)))
            elif self.operatorSelected == "-":
                self.labelResult.setText(str(self.finalResult - int(screenResult)))
            elif self.operatorSelected == "x":
                self.labelResult.setText(str(self.finalResult * int(screenResult)))
            elif self.operatorSelected == "/":
                self.labelResult.setText(str(self.finalResult // int(screenResult)))
            self.finalResult = int(self.labelResult.text())
            screen = self.label.text()
            self.label.setText(screen + screenResult + "=")
            self.operatorSelected = "="
            self.result = 1

    def onClickCE(self):
        if self.operatorSelected=="=":
            self.label.setText("")
            self.labelResult.setText("0")
            self.operatorSelected = ""
            self.result = 0
            self.finalResult = 0
        else:
            self.labelResult.setText("0")

    def onClickC(self):
        self.label.setText("")
        self.labelResult.setText("0")
        self.operatorSelected = ""
        self.result=0
        self.finalResult = 0



app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
