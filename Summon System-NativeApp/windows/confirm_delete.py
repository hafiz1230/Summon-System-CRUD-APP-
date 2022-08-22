# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_window(object):
    def setupUi(self, delete_window):
        delete_window.setObjectName("delete_window")
        delete_window.resize(327, 134)
        self.button_delete = QtWidgets.QDialogButtonBox(delete_window)
        self.button_delete.setGeometry(QtCore.QRect(90, 90, 156, 23))
        self.button_delete.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_delete.setObjectName("button_delete")
        self.label = QtWidgets.QLabel(delete_window)
        self.label.setGeometry(QtCore.QRect(0, -10, 331, 101))
        self.label.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(delete_window)
        QtCore.QMetaObject.connectSlotsByName(delete_window)

    def retranslateUi(self, delete_window):
        _translate = QtCore.QCoreApplication.translate
        delete_window.setWindowTitle(_translate("delete_window", "Delete"))
        self.label.setText(_translate("delete_window", "<html><head/><body><p>Are you sure to delete</p><p>the data?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_window = QtWidgets.QDialog()
    ui = Ui_delete_window()
    ui.setupUi(delete_window)
    delete_window.show()
    sys.exit(app.exec_())

