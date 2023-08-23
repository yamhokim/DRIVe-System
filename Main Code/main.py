import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SplashScreen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)

    time_secs = []          # Keeps track of the time in seconds
    ear_vals = []           # Keeps track of EAR value as a ratio
    mar_vals = []           # Keeps track of MAR value as a ratio
    ear_and_mar_vals = []   # List containining the time data, EAR data, and MAR data as a tuple; (time, EAR, MAR), to be used for csv file
    blink_list = []         # Keeps track of blinks throughout runtime
    yawn_list = []          # Keeps track of yawns throughout runtime
    perclos_vals = []

    # Lists holding values for the animation plotting function
    # --------------------------------------------------------
    temp_ear_data = []      # Copy of the ear_vals list
    temp_time_data = []     # Copy of the time_secs list
    # --------------------------------------------------------
    
    ear_threshold = 0.15
    ear_open_value = 0.7

    window = SplashScreen(time_secs, ear_vals, mar_vals, ear_and_mar_vals, blink_list, yawn_list, temp_ear_data, temp_time_data, ear_threshold, ear_open_value, perclos_vals)
    
    sys.exit(app.exec())
