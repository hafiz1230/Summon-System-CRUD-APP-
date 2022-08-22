# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirm_window(object):
    def setupUi(self, confirm_window):
        confirm_window.setObjectName("confirm_window")
        confirm_window.resize(354, 136)
        self.label = QtWidgets.QLabel(confirm_window)
        self.label.setGeometry(QtCore.QRect(10, 0, 331, 101))
        self.label.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_update = QtWidgets.QDialogButtonBox(confirm_window)
        self.button_update.setGeometry(QtCore.QRect(100, 90, 156, 23))
        self.button_update.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_update.setObjectName("button_update")

        self.retranslateUi(confirm_window)
        QtCore.QMetaObject.connectSlotsByName(confirm_window)

    def retranslateUi(self, confirm_window):
        _translate = QtCore.QCoreApplication.translate
        confirm_window.setWindowTitle(_translate("confirm_window", "Confirm updates?"))
        self.label.setText(_translate("confirm_window", "<html><head/><body><p>Are you sure to update </p><p>the changes?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirm_window = QtWidgets.QDialog()
    ui = Ui_confirm_window()
    ui.setupUi(confirm_window)
    confirm_window.show()
    sys.exit(app.exec_())
