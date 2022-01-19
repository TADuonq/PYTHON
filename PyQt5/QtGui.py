# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Duong\Python\PyQt5\QtGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 573)
        MainWindow.setStyleSheet("\n"
                                "\n"
                                "\n"
                                " ")
        self.Button_start = QtWidgets.QPushButton(MainWindow)
        self.Button_start.setGeometry(QtCore.QRect(80, 350, 75, 23))
        self.Button_start.setObjectName("Button_start")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 80, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Button_stop = QtWidgets.QPushButton(MainWindow)
        self.Button_stop.setGeometry(QtCore.QRect(360, 350, 75, 23))
        self.Button_stop.setObjectName("Button_stop")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.Button_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Text Label"))
        self.Button_stop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
