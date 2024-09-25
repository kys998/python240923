# DemoForm.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 출력")

# 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
