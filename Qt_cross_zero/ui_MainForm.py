# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFormzKDpUX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(338, 244)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 317, 202))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_8 = QFrame(self.layoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 3, 2, 1, 1)

        self.btnStart = QPushButton(self.layoutWidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(95, 0))
        self.btnStart.setBaseSize(QSize(95, 0))

        self.gridLayout.addWidget(self.btnStart, 0, 4, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(95, 0))
        self.label.setBaseSize(QSize(95, 0))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 6, 3, 1, 1)

        self.line_9 = QFrame(self.layoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 3, 4, 1, 1)

        self.b00 = QPushButton(self.layoutWidget)
        self.b00.setObjectName(u"b00")
        self.b00.setBaseSize(QSize(300, 300))
        self.b00.setAutoRepeatInterval(300)
        self.b00.setFlat(True)

        self.gridLayout.addWidget(self.b00, 2, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(95, 0))
        self.label_2.setBaseSize(QSize(95, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.b12 = QPushButton(self.layoutWidget)
        self.b12.setObjectName(u"b12")
        self.b12.setFlat(True)

        self.gridLayout.addWidget(self.b12, 4, 4, 1, 1)

        self.b11 = QPushButton(self.layoutWidget)
        self.b11.setObjectName(u"b11")
        self.b11.setFlat(True)

        self.gridLayout.addWidget(self.b11, 4, 2, 1, 1)

        self.b22 = QPushButton(self.layoutWidget)
        self.b22.setObjectName(u"b22")
        self.b22.setFlat(True)

        self.gridLayout.addWidget(self.b22, 6, 4, 1, 1)

        self.b10 = QPushButton(self.layoutWidget)
        self.b10.setObjectName(u"b10")
        self.b10.setFlat(True)

        self.gridLayout.addWidget(self.b10, 4, 0, 1, 1)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 2, 3, 1, 1)

        self.b20 = QPushButton(self.layoutWidget)
        self.b20.setObjectName(u"b20")
        self.b20.setFlat(True)

        self.gridLayout.addWidget(self.b20, 6, 0, 1, 1)

        self.btnQuit = QPushButton(self.layoutWidget)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setMinimumSize(QSize(95, 0))
        self.btnQuit.setBaseSize(QSize(95, 0))

        self.gridLayout.addWidget(self.btnQuit, 1, 4, 1, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)

        self.b21 = QPushButton(self.layoutWidget)
        self.b21.setObjectName(u"b21")
        self.b21.setFlat(True)

        self.gridLayout.addWidget(self.b21, 6, 2, 1, 1)

        self.cntGamer1 = QLCDNumber(self.layoutWidget)
        self.cntGamer1.setObjectName(u"cntGamer1")
        self.cntGamer1.setMinimumSize(QSize(95, 0))
        self.cntGamer1.setBaseSize(QSize(95, 0))
        self.cntGamer1.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.cntGamer1, 0, 2, 1, 1)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 6, 1, 1, 1)

        self.cntGamer2 = QLCDNumber(self.layoutWidget)
        self.cntGamer2.setObjectName(u"cntGamer2")
        self.cntGamer2.setMinimumSize(QSize(95, 0))
        self.cntGamer2.setBaseSize(QSize(95, 0))
        self.cntGamer2.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.cntGamer2, 1, 2, 1, 1)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 3, 0, 1, 1)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 1, 1, 1)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 4, 3, 1, 1)

        self.b02 = QPushButton(self.layoutWidget)
        self.b02.setObjectName(u"b02")
        self.b02.setFlat(True)

        self.gridLayout.addWidget(self.b02, 2, 4, 1, 1)

        self.b01 = QPushButton(self.layoutWidget)
        self.b01.setObjectName(u"b01")
        self.b01.setFlat(True)

        self.gridLayout.addWidget(self.b01, 2, 2, 1, 1)

        self.line_10 = QFrame(self.layoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_10, 5, 0, 1, 1)

        self.line_11 = QFrame(self.layoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_11, 5, 2, 1, 1)

        self.line_12 = QFrame(self.layoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_12, 5, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u043e\u043a 1", None))
        self.b00.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u043e\u043a 2", None))
        self.b12.setText("")
        self.b11.setText("")
        self.b22.setText("")
        self.b10.setText("")
        self.b20.setText("")
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.b21.setText("")
        self.b02.setText("")
        self.b01.setText("")
    # retranslateUi

