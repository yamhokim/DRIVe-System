import csv
from datetime import datetime
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_new_drive_rating_gui import Ui_DriveWindow

class MainWindow(QMainWindow):

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

        self.ui = Ui_DriveWindow()
        
        self.ui.setupUi(self, self.time_secs, self.ear_vals, self.mar_vals, self.ear_and_mar_vals, self.blink_list, self.yawn_list, self.temp_ear_data, self.temp_time_data, self.ear_threshold, self.ear_open_value, self.perclos_vals)
        
        self.start_datetime = datetime.now().strftime("%d-%m-%Y %H%M%S")    # For file naming purposes
        self.current_time = datetime.now().strftime("%H:%M:%S")     # Tells the start time of each interval
        self.interval_counter = 1   # Keeps track of the interval number in the data file

        self.obs1_rating = "NO RATING"
        self.obs2_rating = "NO RATING"

        self.rating_timer = QTimer()
        self.rating_timer.timeout.connect(self.enable_obs1_buttons)
        self.rating_timer.timeout.connect(self.enable_obs2_buttons)
        self.rating_timer.timeout.connect(self.rating_timer_timeout)
        self.ratingMessageSignal.connect(self.ui.Worker1.start_rating_countdown)

        # ADD IN A FUNCTION THAT OVERLAYS A MESSAGE TO BEGIN RATING, OVER THE WEBCAM FOOTAGE
        #self.rating_timer.timeout.connect()

        self.second_timer = QTimer()
        self.second_timer.timeout.connect(self.disable_obs1_buttons)
        self.second_timer.timeout.connect(self.disable_obs2_buttons)
        self.second_timer.timeout.connect(self.second_timer_timeout)

        self.ui.Worker1.StartMainTimer.connect(self.start_timer)    # CONNECT START_TIMER to the StartMainTimer signal in WebcamWorker

        self.ui.Worker1.StartMainTimer.connect(self.initialize_logfile)


        # Stop logging to CSV when user clicks the stop button
        self.stop_logging = False
        self.ui.Worker1.StopLogging.connect(self.stop_rating)

        
    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        

    # Timer to keep track of the 1 minute intervals that we will be assessing the driver within
    def start_timer(self):
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.rating_timer.start(10000)


    # Once the 10 seconds has passes, the buttons will enable themselves and observes can give ratings in a 5 second interval
    ratingMessageSignal = pyqtSignal()

    def rating_timer_timeout(self):
        self.ratingMessageSignal.emit()
        self.rating_timer.stop()
        self.second_timer.start(5000)


    # Observers just had 5 seconds to rate, buttons disable, and we enter the next interval
    def second_timer_timeout(self):
        self.second_timer.stop()
        self.log_ratings()
        self.current_time = datetime.now().strftime("%H:%M:%S") 
        self.rating_timer.start(10000)


    def initialize_logfile(self):
        with open(f"{self.ui.popup.participant_info}-observer-ratings-{self.start_datetime}.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Interval #", "Interval Start Time", "Observer 1 Rating", "Observer 2 Rating"])


    def on_button_click(self, state, observer):
        if observer == "1":
            self.obs1_rating = state
        elif observer == "2":
            self.obs2_rating = state

    
    def stop_rating(self, stop_pressed):
        print(stop_pressed)
        if stop_pressed:
            self.stop_logging = True


    def log_ratings(self):
        with open(f"{self.ui.popup.participant_info}-observer-ratings-{self.start_datetime}.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.interval_counter, self.current_time, self.obs1_rating, self.obs2_rating])
        self.interval_counter += 1
        self.obs1_rating = "NO RATING"
        self.obs2_rating = "NO RATING"


    def keyPressEvent(self, event):

        key = event.key()

        # Map the keys to the corresponding buttons
        if key == Qt.Key_1:
            self.on_button_click("Alert", "1")
            self.disable_obs1_buttons()
        elif key == Qt.Key_2:
            self.on_button_click("Slightly Drowsy", "1")
            self.disable_obs1_buttons()
        elif key == Qt.Key_3:
            self.on_button_click("Moderately Drowsy", "1")
            self.disable_obs1_buttons()
        elif key == Qt.Key_4:
            self.on_button_click("Very Drowsy", "1")
            self.disable_obs1_buttons()
        elif key == Qt.Key_5:
            self.on_button_click("Extremely Drowsy", "1")
            self.disable_obs1_buttons()
        elif key == Qt.Key_G:
            self.on_button_click("Alert", "2")
            self.disable_obs2_buttons()
        elif key == Qt.Key_H:
            self.on_button_click("Slightly Drowsy", "2")
            self.disable_obs2_buttons()
        elif key == Qt.Key_J:
            self.on_button_click("Moderately Drowsy", "2")
            self.disable_obs2_buttons()
        elif key == Qt.Key_K:
            self.on_button_click("Very Drowsy", "2")
            self.disable_obs2_buttons()
        elif key == Qt.Key_L:
            self.on_button_click("Extremely Drowsy", "2")
            self.disable_obs2_buttons()


    def enable_obs1_buttons(self):
        # Enable observer 1's buttons to be pressed at the start of the rating interval
        self.ui.Button1_3.setEnabled(True)
        self.ui.Button2_3.setEnabled(True)
        self.ui.Button3_3.setEnabled(True)
        self.ui.Button4_3.setEnabled(True)
        self.ui.Button5_3.setEnabled(True)

    
    def enable_obs2_buttons(self):
        # Enable observer 2's buttons to be pressed at the start of the rating interval
        self.ui.ButtonG_3.setEnabled(True)
        self.ui.ButtonH_3.setEnabled(True)
        self.ui.ButtonJ_3.setEnabled(True)
        self.ui.ButtonK_3.setEnabled(True)
        self.ui.ButtonL_3.setEnabled(True)


    def disable_obs1_buttons(self):
        # Disable all the buttons for observer 1 until the next interval
        self.ui.Button1_3.setEnabled(False)
        self.ui.Button2_3.setEnabled(False)
        self.ui.Button3_3.setEnabled(False)
        self.ui.Button4_3.setEnabled(False)
        self.ui.Button5_3.setEnabled(False)


    def disable_obs2_buttons(self):
        # Disable all the buttons for observer 2 until the next interval
        self.ui.ButtonG_3.setEnabled(False)
        self.ui.ButtonH_3.setEnabled(False)
        self.ui.ButtonJ_3.setEnabled(False)
        self.ui.ButtonK_3.setEnabled(False)
        self.ui.ButtonL_3.setEnabled(False)

        
    def change_button_color(self, button, state):
        # Change the button's background color
        if state == "press":
            button.setStyleSheet("QPushButton{background-color:rgb(56, 56, 85); border-radius:15px; border: 3px solid rgb(38, 41, 63); color:rgb(170, 170, 255)} QPushButton:hover{background-color:rgb(97, 97, 145)}")
        elif state == "release":
            button.setStyleSheet("QPushButton{background-color:rgb(85, 85, 127); border-radius:15px; border: 3px solid rgb(38, 41, 63); color:rgb(170, 170, 255)} QPushButton:hover{background-color:rgb(97, 97, 145)}")
