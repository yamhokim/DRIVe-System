import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_modified_ear_threshold_window import Ui_MainWindow
from ThresholdWorker import ThresholdWorker

class ThresholdCalc(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.desktop = QDesktopWidget()
        self.desktop_dimensions = self.desktop.screenGeometry()

        self.open_eye_ear = None
        self.closed_eye_ear = None
        self.modified_ear_threshold = None
        self.ear_counter = 0                                            # If this value is 2, this indicates both ear values have been calculated and that this window can close

        self.ui.camera_button_2.clicked.connect(self.log_open_eye_ear)  # Connect to function that logs the open eye ear
        self.ui.camera_button.clicked.connect(self.log_closed_eye_ear)  # Connect to a function which logs the closed eye ear
        self.stop_signal.connect(self.calculate_modified_ear_threshold) # This signal will set the ear threshold and will close this window

        self.worker = ThresholdWorker(self.desktop_dimensions)
        self.stop_worker_signal.connect(self.worker.terminate_run)      # This signal indicates for the threshold worker object to stop its run() function
        self.worker.webcamSignal.connect(self.webcamUpdateSlot)
        self.worker.start()

    stop_signal = pyqtSignal()          # Indicates that both ear values were logged and that the threshold can be calculated, also closes the ThresholdCalc window
    stop_worker_signal = pyqtSignal()   # Signal that stops the threshold worker from running in the back once its job is done

    def log_open_eye_ear(self):
        self.open_eye_ear = self.worker.ear_vals[-1]
        self.ear_counter += 1
        self.ui.camera_button_2.setDisabled(True)
        if self.ear_counter == 2:
            self.stop_signal.emit()
            self.stop_worker_signal.emit()


    def log_closed_eye_ear(self):
        self.closed_eye_ear = self.worker.ear_vals[-1]
        self.ear_counter += 1
        self.ui.camera_button.setDisabled(True)
        if self.ear_counter == 2:
            self.stop_signal.emit()
            self.stop_worker_signal.emit()


    modified_ear_signal = pyqtSignal(float)
    
    def calculate_modified_ear_threshold(self):
        self.modified_ear_threshold = (self.open_eye_ear + self.closed_eye_ear) / 2
        self.modified_ear_signal.emit(self.modified_ear_threshold)
        self.close()


    def webcamUpdateSlot(self, image):
        self.ui.webcam_label.setPixmap(QPixmap.fromImage(image))


    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())




