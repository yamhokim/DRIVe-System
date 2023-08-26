from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.desktop = QDesktopWidget()
        self.desktop_dimensions = self.desktop.screenGeometry()
        MainWindow.resize(int(self.desktop_dimensions.width() * 0.5), int(self.desktop_dimensions.height() * 0.7))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.resize(int(self.desktop_dimensions.width() * 0.5), int(self.desktop_dimensions.height() * 0.7))
        self.widget.setStyleSheet(u"background-color:rgb(85, 85, 127); border-radius: 20px; border: 5px solid black")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, -1)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:rgb(108, 108, 162); border-radius: 20px; border: 5px solid rgb(108, 108, 162)")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.webcam_label = QLabel(self.widget_2)
        self.webcam_label.setObjectName(u"webcam_label")
        self.webcam_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.webcam_label)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:rgb(85, 85, 127); border: 5px solid rgb(85, 85, 127)")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, 0, 80, 0)
        self.camera_button_2 = QPushButton(self.widget_3)
        self.camera_button_2.setObjectName(u"camera_button_2")
        self.camera_button_2.setMinimumSize(QSize(0, 160))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.camera_button_2.setFont(font)
        self.camera_button_2.setStyleSheet(u"""
                                           QPushButton{background-color:rgb(0, 170, 255); border-radius: 10px; border: 5px solid white; color: rgb(0, 62, 94)}
                                           QPushButton:hover{background-color: rgb(0, 111, 166)}
                                           QPushButton:pressed{background-color:rgb(0, 111, 166); border-radius: 10px; border: 5px solid  rgb(0, 62, 94); color: rgb(0, 62, 94)}
                                           """)

        self.horizontalLayout.addWidget(self.camera_button_2)

        self.camera_button = QPushButton(self.widget_3)
        self.camera_button.setObjectName(u"camera_button")
        self.camera_button.setMinimumSize(QSize(0, 160))
        self.camera_button.setFont(font)
        self.camera_button.setStyleSheet(u"""
                                         QPushButton{background-color:rgb(0, 170, 255); border-radius: 10px; border: 5px solid white; color: rgb(0, 62, 94)}
                                         QPushButton:hover{background-color:rgb(0, 111, 166)}
                                         QPushButton:pressed{background-color:rgb(0, 111, 166); border-radius: 10px; border: 5px solid  rgb(0, 62, 94); color: rgb(0, 62, 94)}
                                         """)

        self.horizontalLayout.addWidget(self.camera_button)


        self.verticalLayout.addWidget(self.widget_3)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.webcam_label.setText("")
        self.camera_button_2.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.camera_button.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
    # retranslateUi

