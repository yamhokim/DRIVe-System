from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_protocol_info import Ui_MainWindow

class InfoPopupWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.protocol_window = Ui_MainWindow()

        self.protocol_window.setupUi(self)
        

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

