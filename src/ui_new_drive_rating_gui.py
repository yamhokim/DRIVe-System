from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from WebcamWorker import WebcamWorker
from PlotWindow import PlotWindow
from csv_writer import write_to_csv
from plot_functions import plot_eye_data, plot_mouth_data
from PopUp import PopupWindow
from InfoPopUp import InfoPopupWindow
import os

class Ui_DriveWindow(object):
    def setupUi(self, DriveWindow, time_secs, ear_vals, mar_vals, ear_and_mar_vals, blink_list, yawn_list, temp_ear_data, temp_time_data, ear_threshold, ear_open_value, perclos_vals):
        if DriveWindow.objectName():
            DriveWindow.setObjectName(u"DriveWindow")
        desktop = QDesktopWidget()
        desktop_dimensions = desktop.screenGeometry()
        DriveWindow.resize(int(desktop_dimensions.width() * 0.8), int(desktop_dimensions.height() * 0.8))
        DriveWindow.setStyleSheet(u"background-color:rgb(50, 50, 75)")
        # For later use
        self.webcam_icon = os.path.expanduser(os.getcwd() + "/" + "camera_icon.png")

        self.centralwidget = QWidget(DriveWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftWidget = QWidget(self.centralwidget)
        self.LeftWidget.setObjectName(u"LeftWidget")
        self.LeftWidget.setMinimumSize(QSize(528, 622))
        self.LeftWidget.setMaximumSize(QSize(16777215, 16777215))
        self.LeftWidget.setStyleSheet(u"background-color:rgb(68, 76, 109)")
        self.verticalLayout = QVBoxLayout(self.LeftWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.frame_1 = QFrame(self.LeftWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.Obs1Label_3 = QLabel(self.frame_1)
        self.Obs1Label_3.setObjectName(u"Obs1Label_3")
        font = QFont()
        font.setPointSize(22)
        self.Obs1Label_3.setFont(font)
        self.Obs1Label_3.setStyleSheet(u"background-color:rgb(135, 135, 203); border: 2px solid black; border-radius: 10px")
        self.Obs1Label_3.setTextFormat(Qt.AutoText)
        self.Obs1Label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Obs1Label_3)

        self.StateLabel_3 = QLabel(self.frame_1)
        self.StateLabel_3.setObjectName(u"StateLabel_3")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.StateLabel_3.setFont(font1)
        self.StateLabel_3.setStyleSheet(u"background-color:rgb(135, 135, 203); border: 2px solid black; border-radius: 10px")
        self.StateLabel_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.StateLabel_3)

        self.Obs2Label_3 = QLabel(self.frame_1)
        self.Obs2Label_3.setObjectName(u"Obs2Label_3")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(22)
        self.Obs2Label_3.setFont(font2)
        self.Obs2Label_3.setStyleSheet(u"background-color:rgb(135, 135, 203); border: 2px solid black; border-radius: 10px")
        self.Obs2Label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Obs2Label_3)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 11)
        self.horizontalLayout_2.setStretch(2, 6)

        self.verticalLayout.addWidget(self.frame_1)

        self.frame_4 = QFrame(self.LeftWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:rgb(49, 55, 81); border:2px solid rgb(38, 41, 63); border-radius5px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.Button1_3 = QPushButton(self.frame_6)
        self.Button1_3.setObjectName(u"Button1_3")
        self.Button1_3.setMinimumSize(QSize(56, 56))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)


        self.Button1_3.setFont(font3)
        self.Button1_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_2.addWidget(self.Button1_3)

        self.Button2_3 = QPushButton(self.frame_6)
        self.Button2_3.setObjectName(u"Button2_3")
        self.Button2_3.setMinimumSize(QSize(56, 56))
        self.Button2_3.setFont(font3)
        self.Button2_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_2.addWidget(self.Button2_3)

        self.Button3_3 = QPushButton(self.frame_6)
        self.Button3_3.setObjectName(u"Button3_3")
        self.Button3_3.setMinimumSize(QSize(56, 56))
        self.Button3_3.setFont(font3)
        self.Button3_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_2.addWidget(self.Button3_3)

        self.Button4_3 = QPushButton(self.frame_6)
        self.Button4_3.setObjectName(u"Button4_3")
        self.Button4_3.setMinimumSize(QSize(56, 56))
        self.Button4_3.setFont(font3)
        self.Button4_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_2.addWidget(self.Button4_3)

        self.Button5_3 = QPushButton(self.frame_6)
        self.Button5_3.setObjectName(u"Button5_3")
        self.Button5_3.setMinimumSize(QSize(56, 56))
        self.Button5_3.setFont(font3)
        self.Button5_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_2.addWidget(self.Button5_3)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, 20)
        self.AlertFrame = QFrame(self.frame_7)
        self.AlertFrame.setObjectName(u"AlertFrame")
        self.AlertFrame.setStyleSheet(u"background-color:rgb(194, 255, 82); border: 2px solid black; border-radius: 10px")
        self.AlertFrame.setFrameShape(QFrame.StyledPanel)
        self.AlertFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.AlertFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.AlertLabel = QLabel(self.AlertFrame)
        self.AlertLabel.setObjectName(u"AlertLabel")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.AlertLabel.setFont(font4)
        self.AlertLabel.setStyleSheet(u"border:0px; background-color:rgba(0,0,0,0%)")
        self.AlertLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.AlertLabel)

        self.horizontalLayout_5.setStretch(0, 5)

        self.verticalLayout_4.addWidget(self.AlertFrame)

        self.SlightlyDrowsyFrame = QFrame(self.frame_7)
        self.SlightlyDrowsyFrame.setObjectName(u"SlightlyDrowsyFrame")
        self.SlightlyDrowsyFrame.setStyleSheet(u"background-color:rgb(237, 255, 0); border: 2px solid black; border-radius: 10px")
        self.SlightlyDrowsyFrame.setFrameShape(QFrame.StyledPanel)
        self.SlightlyDrowsyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.SlightlyDrowsyFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SlightDrowsyLabel = QLabel(self.SlightlyDrowsyFrame)
        self.SlightDrowsyLabel.setObjectName(u"SlightDrowsyLabel")
        self.SlightDrowsyLabel.setFont(font4)
        self.SlightDrowsyLabel.setStyleSheet(u"border:0px;background-color:rgba(0,0,0,0%)")
        self.SlightDrowsyLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.SlightDrowsyLabel)


        self.verticalLayout_4.addWidget(self.SlightlyDrowsyFrame)

        self.ModeratelyDrowsyFrame = QFrame(self.frame_7)
        self.ModeratelyDrowsyFrame.setObjectName(u"ModeratelyDrowsyFrame")
        self.ModeratelyDrowsyFrame.setStyleSheet(u"background-color:rgb(255, 208, 130); border: 2px solid black; border-radius: 10px")
        self.ModeratelyDrowsyFrame.setFrameShape(QFrame.StyledPanel)
        self.ModeratelyDrowsyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ModeratelyDrowsyFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 9)
        self.ModeratelyDrowsyLabel = QLabel(self.ModeratelyDrowsyFrame)
        self.ModeratelyDrowsyLabel.setObjectName(u"ModeratelyDrowsyLabel")
        self.ModeratelyDrowsyLabel.setFont(font4)
        self.ModeratelyDrowsyLabel.setStyleSheet(u"border:0px; background-color:rgba(0,0,0,0%)")
        self.ModeratelyDrowsyLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ModeratelyDrowsyLabel)


        self.verticalLayout_4.addWidget(self.ModeratelyDrowsyFrame)

        self.VeryDrowsyFrame = QFrame(self.frame_7)
        self.VeryDrowsyFrame.setObjectName(u"VeryDrowsyFrame")
        self.VeryDrowsyFrame.setStyleSheet(u"background-color:rgb(247, 131, 97); border: 2px solid black; border-radius: 10px")
        self.VeryDrowsyFrame.setFrameShape(QFrame.StyledPanel)
        self.VeryDrowsyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.VeryDrowsyFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.VeryDrowsyLabel = QLabel(self.VeryDrowsyFrame)
        self.VeryDrowsyLabel.setObjectName(u"VeryDrowsyLabel")
        self.VeryDrowsyLabel.setFont(font4)
        self.VeryDrowsyLabel.setStyleSheet(u"border:0px; background-color:rgba(0,0,0,0%)")
        self.VeryDrowsyLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.VeryDrowsyLabel)


        self.verticalLayout_4.addWidget(self.VeryDrowsyFrame)

        self.ExtremelyDrowsyFrame = QFrame(self.frame_7)
        self.ExtremelyDrowsyFrame.setObjectName(u"ExtremelyDrowsyFrame")
        self.ExtremelyDrowsyFrame.setStyleSheet(u"background-color:rgb(196, 72, 35); border: 2px solid black; border-radius: 10px")
        self.ExtremelyDrowsyFrame.setFrameShape(QFrame.StyledPanel)
        self.ExtremelyDrowsyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.ExtremelyDrowsyFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.ExtremelyDrowsyLabel = QLabel(self.ExtremelyDrowsyFrame)
        self.ExtremelyDrowsyLabel.setObjectName(u"ExtremelyDrowsyLabel")
        self.ExtremelyDrowsyLabel.setFont(font4)
        self.ExtremelyDrowsyLabel.setStyleSheet(u"border:0px; background-color:rgba(0,0,0,0%)")
        self.ExtremelyDrowsyLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.ExtremelyDrowsyLabel)


        self.verticalLayout_4.addWidget(self.ExtremelyDrowsyFrame)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.ButtonG_3 = QPushButton(self.frame_8)
        self.ButtonG_3.setObjectName(u"ButtonG_3")
        self.ButtonG_3.setMinimumSize(QSize(56, 56))
        self.ButtonG_3.setFont(font3)
        self.ButtonG_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_3.addWidget(self.ButtonG_3)

        self.ButtonH_3 = QPushButton(self.frame_8)
        self.ButtonH_3.setObjectName(u"ButtonH_3")
        self.ButtonH_3.setMinimumSize(QSize(56, 56))
        self.ButtonH_3.setFont(font3)
        self.ButtonH_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_3.addWidget(self.ButtonH_3)

        self.ButtonJ_3 = QPushButton(self.frame_8)
        self.ButtonJ_3.setObjectName(u"ButtonJ_3")
        self.ButtonJ_3.setMinimumSize(QSize(56, 56))
        self.ButtonJ_3.setFont(font3)
        self.ButtonJ_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_3.addWidget(self.ButtonJ_3)

        self.ButtonK_3 = QPushButton(self.frame_8)
        self.ButtonK_3.setObjectName(u"ButtonK_3")
        self.ButtonK_3.setMinimumSize(QSize(56, 56))
        self.ButtonK_3.setFont(font3)
        self.ButtonK_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        self.verticalLayout_3.addWidget(self.ButtonK_3)

        self.ButtonL_3 = QPushButton(self.frame_8)
        self.ButtonL_3.setObjectName(u"ButtonL_3")
        self.ButtonL_3.setMinimumSize(QSize(56, 56))
        self.ButtonL_3.setFont(font3)
        self.ButtonL_3.setStyleSheet("background-color: rgb(62, 62, 94);")

        # All the buttons should start off as disabled
        self.Button1_3.setEnabled(False)
        self.Button2_3.setEnabled(False)
        self.Button3_3.setEnabled(False)
        self.Button4_3.setEnabled(False)
        self.Button5_3.setEnabled(False)
        self.ButtonG_3.setEnabled(False)
        self.ButtonH_3.setEnabled(False)
        self.ButtonJ_3.setEnabled(False)
        self.ButtonK_3.setEnabled(False)
        self.ButtonL_3.setEnabled(False)


        self.verticalLayout_3.addWidget(self.ButtonL_3)

        self.horizontalLayout_4.addWidget(self.frame_8)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.LeftWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.StartButton_3 = QPushButton(self.frame_3)
        self.StartButton_3.setObjectName(u"StartButton_3")
        self.StartButton_3.setFont(font3)
        self.StartButton_3.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(85, 85, 127); border-radius:15px; border: 3px solid rgb(38, 41, 63); color:rgb(170, 170, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(97, 97, 145)\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.StartButton_3)

        self.Info_Button = QPushButton(self.frame_3)
        self.Info_Button.setObjectName(u"Info_Button")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.Info_Button.setFont(font5)
        self.Info_Button.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0, 127, 190); border-radius:15px; border: 3px solid rgb(38, 41, 63); color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(79, 159, 238)\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.Info_Button)

        self.StopButton_3 = QPushButton(self.frame_3)
        self.StopButton_3.setObjectName(u"StopButton_3")
        self.StopButton_3.setFont(font3)
        self.StopButton_3.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(85, 85, 127); border-radius:15px; border: 3px solid rgb(38, 41, 63); color:rgb(170, 170, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(97, 97, 145)\n"
"}\n"
"")
        self.StopButton_3.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.StopButton_3)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayout.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.LeftWidget)

        self.RightWidget = QWidget(self.centralwidget)
        self.RightWidget.setObjectName(u"RightWidget")
        self.RightWidget.setMinimumSize(QSize(528, 622))
        self.RightWidget.setMaximumSize(QSize(16777215, 16777215))
        self.RightWidget.setToolTipDuration(5)
        self.RightWidget.setStyleSheet(u"background-color:rgb(54, 64, 97)")
        self.verticalLayout_5 = QVBoxLayout(self.RightWidget)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, 20, 50, 20)
        self.widget = QWidget(self.RightWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:rgb(49, 55, 81); border-radius:25px;\n"
"border:5px solid rgb(38, 41, 63)")

        self.horizontalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color:rgb(49, 55, 81); border-radius:25px;\n"
"border:5px solid rgb(38, 41, 63)")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.EARLabel = QLabel(self.widget_4)
        self.EARLabel.setObjectName(u"EARLabel")
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.EARLabel.setFont(font6)
        self.EARLabel.setStyleSheet(u"border-radius:0px; border:0px")

        self.verticalLayout_6.addWidget(self.EARLabel)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        self.label_2.setFont(font7)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet(u"border-radius:2px; border:0px; color: rgb(133, 133, 199)")

        self.verticalLayout_6.addWidget(self.label_2)

        self.MARLabel = QLabel(self.widget_4)
        self.MARLabel.setObjectName(u"MARLabel")
        self.MARLabel.setFont(font6)
        self.MARLabel.setStyleSheet(u"border-radius:0px; border:0px")

        self.verticalLayout_6.addWidget(self.MARLabel)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setStyleSheet(u"border-radius:2px; border:0px; color: rgb(133, 133, 199)")

        self.verticalLayout_6.addWidget(self.label_6)

        self.PERCLOSLabel = QLabel(self.widget_4)
        self.PERCLOSLabel.setObjectName(u"PERCLOSLabel")
        self.PERCLOSLabel.setFont(font6)
        self.PERCLOSLabel.setStyleSheet(u"border-radius:0px; border:0px")

        self.verticalLayout_6.addWidget(self.PERCLOSLabel)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setStyleSheet(u"border-radius:2px; border:0px; color: rgb(133, 133, 199)")

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_10.addWidget(self.widget_4)

        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.RightWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:rgb(49, 55, 81); border-radius:25px;\n"
"border:5px solid rgb(38, 41, 63)")

        self.verticalLayout_5.addWidget(self.widget_2)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)                  # CHANGE THIS LATERTRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

        # Initialize the different inputs for the opencv and plot windows
        self.time_secs = time_secs
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
        
        # Adding layouts to hold the opencv and plot windows

        # Setup the layout for the opencv window
        self.vbl_opencv = QVBoxLayout(self.widget_3)
        self.FeedLabel = QLabel()
        self.FeedLabel.setStyleSheet(u"background-color:rgb(49, 55, 81); border-radius: 0px; border:0px solid rgb(38, 41, 63)")
        self.FeedLabel.setAlignment(Qt.AlignCenter)
        webcam_pixmap = QPixmap(self.webcam_icon)
        self.FeedLabel.setPixmap(webcam_pixmap)
        self.vbl_opencv.addWidget(self.FeedLabel)

        self.feed_dimensions = self.widget_3.size()

        self.Worker1 = WebcamWorker(self.time_secs, self.ear_vals, self.mar_vals, self.ear_and_mar_vals, self.blink_list, self.yawn_list, self.temp_ear_data, self.temp_time_data, self.ear_threshold, self.ear_open_value, self.perclos_vals, self.feed_dimensions)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker1.RatioLabelUpdate.connect(self.updateRatioLabels)
        self.Worker1.PerclosLabelUpdate.connect(self.updatePerclosLabel)
        self.widget.setLayout(self.vbl_opencv)

        # Setup the layout for the plot animation window
        self.vbl_plot = QVBoxLayout(self.widget_2)
        self.animatedWidget = PlotWindow()
        self.animatedWidget.setStyleSheet(u"background-color:rgb(49, 55, 81); border-radius: 0px; border:0px solid rgb(38, 41, 63)")
        self.Worker1.PlotUpdate.connect(self.animatedWidget.change_data)
        self.vbl_plot.addWidget(self.animatedWidget)

        self.StartButton_3.clicked.connect(self.open_popup)
        self.StartButton_3.clicked.connect(self.Worker1.start_switch)
        self.StartButton_3.clicked.connect(self.disable_start_button)
        self.StopButton_3.clicked.connect(self.Worker1.stop_switch)
        self.StopButton_3.clicked.connect(self.animatedWidget.stop_switch)
        self.StopButton_3.clicked.connect(self.set_webcam_pixmap)
        self.StopButton_3.clicked.connect(self.Worker1.log_and_clear_data)
        self.StopButton_3.clicked.connect(self.disable_stop_button)

        self.Info_Button.clicked.connect(self.open_info_screen)

        self.changeImage = False        # Determines whether to change the opencv label image to the camera icon

        self.horizontalLayout.addWidget(self.RightWidget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        DriveWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DriveWindow)
        self.statusbar.setObjectName(u"statusbar")
        DriveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DriveWindow)

        QMetaObject.connectSlotsByName(DriveWindow)
    # setupUi


    def retranslateUi(self, DriveWindow):
        DriveWindow.setWindowTitle(QCoreApplication.translate("DriveWindow", u"DRIVe System", None))
        self.Obs1Label_3.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">OBS. 1</span></p></body></html>", None))
        self.StateLabel_3.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">STATES</span></p></body></html>", None))
        self.Obs2Label_3.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">OBS. 2</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.Button1_3.setWhatsThis(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p>a button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button1_3.setText(QCoreApplication.translate("DriveWindow", u"1", None))
        self.Button2_3.setText(QCoreApplication.translate("DriveWindow", u"2", None))
        self.Button3_3.setText(QCoreApplication.translate("DriveWindow", u"3", None))
        self.Button4_3.setText(QCoreApplication.translate("DriveWindow", u"4", None))
        self.Button5_3.setText(QCoreApplication.translate("DriveWindow", u"5", None))
#if QT_CONFIG(tooltip)
        self.AlertFrame.setToolTip(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p>bruh</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.AlertLabel.setText(QCoreApplication.translate("DriveWindow", u"Alert", None))
        self.SlightDrowsyLabel.setText(QCoreApplication.translate("DriveWindow", u"Slightly Drowsy", None))
        self.ModeratelyDrowsyLabel.setText(QCoreApplication.translate("DriveWindow", u"Moderately Drowsy", None))
        self.VeryDrowsyLabel.setText(QCoreApplication.translate("DriveWindow", u"Very Drowsy", None))
        self.ExtremelyDrowsyLabel.setText(QCoreApplication.translate("DriveWindow", u"Extremely Drowsy", None))
        self.ButtonG_3.setText(QCoreApplication.translate("DriveWindow", u"G", None))
        self.ButtonH_3.setText(QCoreApplication.translate("DriveWindow", u"H", None))
        self.ButtonJ_3.setText(QCoreApplication.translate("DriveWindow", u"J", None))
        self.ButtonK_3.setText(QCoreApplication.translate("DriveWindow", u"K", None))
        self.ButtonL_3.setText(QCoreApplication.translate("DriveWindow", u"L", None))
        self.StartButton_3.setText(QCoreApplication.translate("DriveWindow", u"START", None))
        self.Info_Button.setText(QCoreApplication.translate("DriveWindow", u"INFO", None))
        self.StopButton_3.setText(QCoreApplication.translate("DriveWindow", u"STOP", None))
        self.EARLabel.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline; color:#aaaaff;\">EAR</span></p></body></html>", None))
        self.label_2.setText("")
        self.MARLabel.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline; color:#aaaaff;\">MAR</span></p></body></html>", None))
        self.label_6.setText("")
        self.PERCLOSLabel.setText(QCoreApplication.translate("DriveWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline; color:#aaaaff;\">PERCLOS</span></p></body></html>", None))
        self.label_5.setText("")
    # retranslateUi

    def ImageUpdateSlot(self, image):
        if self.changeImage == True:
            webcam_pixmap = QPixmap(self.webcam_icon)
            self.FeedLabel.clear()
            self.FeedLabel.setPixmap(webcam_pixmap)
        else:
            self.FeedLabel.setPixmap(QPixmap.fromImage(image))

    
    def updateRatioLabels(self, mar, ear):
        self.label_6.setText(mar)

        self.label_2.setText(ear)
    
    
    def updatePerclosLabel(self, perclos):
        self.label_5.setText(perclos)
    
    def set_webcam_pixmap(self):
        self.changeImage = True


    def open_popup(self):
        self.popup = PopupWindow()
        self.popup.center()
        self.popup.show()
        self.popup.threshold_created.connect(self.check_for_ear_threshold)      # The threshold_created signal is emitted when the popup object creates a ThresholdCalc object
        self.popup.participant_info_created.connect(self.Worker1.create_participant_info)
    
    def check_for_ear_threshold(self):
        self.popup.threshold_calc.modified_ear_signal.connect(self.Worker1.set_modified_ear_threshold)  # The webcamworker object receives the threshold through the signal
    
    
    def open_info_screen(self):
        self.info_popup = InfoPopupWindow()
        self.info_popup.center()
        self.info_popup.show()

    
    def disable_start_button(self):
        self.StartButton_3.setEnabled(False)
        self.StopButton_3.setEnabled(True)

    def disable_stop_button(self):
        self.StopButton_3.setEnabled(False)
        self.StartButton_3.setEnabled(True)

        