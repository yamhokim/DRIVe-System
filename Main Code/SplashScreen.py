from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWindow import MainWindow
from ui_drive_splashscreen import Ui_SplashWindow

counter = 0

class SplashScreen(QMainWindow):
    
    def __init__(self, time_secs, ear_vals, mar_vals, ear_and_mar_vals, blink_list, yawn_list, temp_ear_data, temp_time_data, ear_threshold, ear_open_value, perclos_vals):
        QMainWindow.__init__(self)

        self.time_secs= time_secs
        self.ear_vals = ear_vals
        self.mar_vals = mar_vals
        self.ear_and_mar_vals = ear_and_mar_vals
        self.blink_list = blink_list
        self.yawn_list = yawn_list
        self.temp_ear_data = temp_ear_data
        self.temp_time_data = temp_time_data
        self.ear_threshold = ear_threshold
        self.ear_open_value = ear_open_value
        self.perclos_vals = perclos_vals

        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.center()

        self.show()
    

    def progress(self):
        global counter

        # Setting value of the progress bar
        self.ui.progressBar.setValue(counter)

        # Increment the progress value of the bar
        if counter > 100:   # Once counter reaches 100, close the splashscreen and open up the main screen
            # Stop the timer
            self.timer.stop()

            # Show the main window
            
            self.main = MainWindow(self.time_secs, self.ear_vals, self.mar_vals, self.ear_and_mar_vals, self.blink_list, self.yawn_list, self.temp_ear_data, self.temp_time_data, self.ear_threshold, self.ear_open_value, self.perclos_vals)
            self.main.center()
            self.main.show()

            # Close the splash screen
            self.close()
        
        # Increase counter
        counter += 1


    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())