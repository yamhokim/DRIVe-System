from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 1440)
        MainWindow.setStyleSheet(u"background-color: rgb(50, 50, 75)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: 2px solid rgb(0, 0, 0); background-color:rgb(194, 255, 82);border-radius: 10px")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color:rgb(237, 255, 0); border: 2px solid black; border-radius: 10px")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color:rgb(255, 208, 130); border: 2px solid black; border-radius: 10px")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color:rgb(247, 131, 97); border: 2px solid black; border-radius: 10px")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:rgb(196, 72, 35); border: 2px solid black; border-radius: 10px")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color:rgb(85, 170, 255); border:2px solid rgb(38, 41, 63); border-radius: 10px")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color:rgb(85, 170, 255); border:2px solid rgb(38, 41, 63); border-radius: 10px")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color:rgb(85, 170, 255); border:2px solid rgb(38, 41, 63); border-radius: 10px")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color:rgb(85, 170, 255); border:2px solid rgb(38, 41, 63); border-radius: 10px")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(8)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color:rgb(85, 170, 255); border:2px solid rgb(38, 41, 63); border-radius: 10px")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_9)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Drowsiness State Protocol", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Alert</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Slightly Drowsy</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Moderately Drowsy</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Very Drowsy</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Extremely Drowsy</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Appearance of alertness present; normal facial tone; normal</span></p><p><span style=\" color:#ffffff;\">fast eye blinks; short ordinary glances; occasional body movements/gestures</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Still sufficiently alert; less sharp / alert looks; longer</span></p><p align=\"center\"><span style=\" color:#ffffff;\">glances; slower eye blinks; first mannerisms as rubbing face/eyes, scratching, facial</span></p><p align=\"center\"><span style=\" color:#ffffff;\">contortions, moving restlessly in the seat</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Mannerisms; slower eye-lid closures; decreasing facial</span></p><p><span style=\" color:#ffffff;\">tone; glassy eyes; staring at fixed position</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Eyelid closures (2-3s); eyes rolling upward / sideways; no</span></p><p><span style=\" color:#ffffff;\">proper focused eyes; decreased facial tone; lack of apparent activity; large isolated or</span></p><p><span style=\" color:#ffffff;\">punctuating movements</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Eyelid closures (4s or more); falling asleep; longer</span></p><p><span style=\" font-weight:600; color:#ffffff;\">periods of lack of activity; movements when transition in and out of dozing</span></p></body></html>", None))
    # retranslateUi

