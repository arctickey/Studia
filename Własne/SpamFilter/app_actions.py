from PyQt5.QtWidgets import QMessageBox
from Checker import *
from Algorithm import *

from app import *



class Spam(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Spam, self).__init__(parent)
        self.setupUi(self)
        self.checkButton.clicked.connect(self.rob)

    def rob(self):
        try:
            text = self.textEdit.toPlainText()
            wynik = checker(text)
            print(wynik)
            if wynik == 0:
                self.outputText.setText("This is not spam")
            else:
                self.outputText.setText('This is spam')
        except:
            QMessageBox.warning(self, "Błąd", "Blędne dane", QMessageBox.Ok)
