from app_actions import *
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Spam()
    window.show()
    app.exec_()