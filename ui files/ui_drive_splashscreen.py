# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drive_splashscreenKvjHqK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        desktop = QDesktopWidget()
        desktop_dimensions = desktop.screenGeometry()
        splash_width = int((desktop_dimensions.width())/2)
        splash_height = int((desktop_dimensions.height()) * 0.3)
        SplashWindow.resize(splash_width, splash_height)
        #SplashWindow.setMinimumSize(QSize(1500, 720))
        self.centralwidget = QWidget(SplashWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(56, 58,89);\n"
"	color:rgb(220,220,220);\n"
"	border-radius: 20px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(56)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(240, 160, 240); background-color: rgba(0,0,0,0%)")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98,114,164);\n"
"	color:rgb(255, 255, 255);\n"
"	text-align:center;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 157, 235, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	border-radius: 10px\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 4)
        self.progressBar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.verticalLayout.addWidget(self.frame)

        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashWindow", u"<strong>DRIVe", None))
        self.label_2.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#6272a4;\">Drowsiness Rating and Intervention Verification System</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#c8c8c8;\">loading...</span></p></body></html>", None))
    # retranslateUi

