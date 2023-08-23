from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ThresholdCalculator import ThresholdCalc

class PopupWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()


    popupSignal = pyqtSignal()  # Signal to check if a name has been entered
    
    def initUI(self):
        self.setWindowTitle("Participant Info")
        self.setGeometry(1919, 1127, 600, 200)
        self.function_label = QLabel(text="Enter Participant Info")
        self.input_text = QLineEdit()
        self.enter_button = QPushButton("Enter")
        self.enter_button.clicked.connect(self.on_enter_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.enter_button)

        self.setLayout(layout)


    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


    threshold_created = pyqtSignal()

    def on_enter_button_clicked(self):
        self.participant_info = self.input_text.text()
        #self.popupSignal.emit()

        self.threshold_calc = ThresholdCalc()
        self.threshold_created.emit()       # Emit this signal so that we can start checking for the modified_ear_signal
        self.threshold_calc.center()
        self.threshold_calc.show()

        self.close()