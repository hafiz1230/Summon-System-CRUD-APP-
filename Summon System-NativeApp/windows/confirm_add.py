# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_window(object):
    def setupUi(self, add_window):
        add_window.setObjectName("add_window")
        add_window.resize(342, 130)
        self.label = QtWidgets.QLabel(add_window)
        self.label.setGeometry(QtCore.QRect(0, -10, 331, 101))
        self.label.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_add = QtWidgets.QDialogButtonBox(add_window)
        self.button_add.setGeometry(QtCore.QRect(90, 90, 156, 23))
        self.button_add.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_add.setObjectName("button_add")

        self.retranslateUi(add_window)
        QtCore.QMetaObject.connectSlotsByName(add_window)

    def retranslateUi(self, add_window):
        _translate = QtCore.QCoreApplication.translate
        add_window.setWindowTitle(_translate("add_window", "Add data"))
        self.label.setText(_translate("add_window", "<html><head/><body><p>Are you sure to add</p><p>the data?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_window = QtWidgets.QDialog()
    ui = Ui_add_window()
    ui.setupUi(add_window)
    add_window.show()
    sys.exit(app.exec_())

