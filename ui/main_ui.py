# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 620)
        MainWindow.setMinimumSize(QtCore.QSize(400, 620))
        MainWindow.setMaximumSize(QtCore.QSize(400, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 550, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_pushcase = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_pushcase.setObjectName("add_pushcase")
        self.horizontalLayout.addWidget(self.add_pushcase)
        self.del_purchase = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.del_purchase.setObjectName("del_purchase")
        self.horizontalLayout.addWidget(self.del_purchase)
        self.category = QtWidgets.QComboBox(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(80, 50, 221, 27))
        self.category.setObjectName("category")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 381, 461))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 27))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список покупок"))
        self.add_pushcase.setText(_translate("MainWindow", "Добавить покупку"))
        self.del_purchase.setText(_translate("MainWindow", "Удалить покупку"))
        self.label.setText(_translate("MainWindow", "Выберите категорию"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.action.setText(_translate("MainWindow", "Добавить категорию"))

