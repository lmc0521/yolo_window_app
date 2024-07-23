# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 675)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblPath = QLabel(self.frame_3)
        self.lblPath.setObjectName(u"lblPath")
        self.lblPath.setFrameShape(QFrame.Panel)
        self.lblPath.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.lblPath)

        self.btnPath = QPushButton(self.frame_3)
        self.btnPath.setObjectName(u"btnPath")
        self.btnPath.setMinimumSize(QSize(50, 0))
        self.btnPath.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.btnPath)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.lblImg = QLabel(self.frame)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setFrameShape(QFrame.Panel)
        self.lblImg.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.lblImg)


        self.verticalLayout.addWidget(self.frame)

        self.lblStatus = QLabel(self.centralwidget)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setMinimumSize(QSize(0, 30))
        self.lblStatus.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(20)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblStatus)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblPath.setText("")
        self.btnPath.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u9304", None))
        self.lblImg.setText("")
        self.lblStatus.setText("")
    # retranslateUi

