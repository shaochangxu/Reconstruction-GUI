# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DenseCommandInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DenseCmdDialog(object):
    def setupUi(self, DenseCmdDialog):
        DenseCmdDialog.setObjectName("DenseCmdDialog")
        DenseCmdDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DenseCmdDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(DenseCmdDialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(DenseCmdDialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(DenseCmdDialog)
        QtCore.QMetaObject.connectSlotsByName(DenseCmdDialog)

    def retranslateUi(self, DenseCmdDialog):
        _translate = QtCore.QCoreApplication.translate
        DenseCmdDialog.setWindowTitle(_translate("DenseCmdDialog", "Dialog"))
        self.pushButton.setText(_translate("DenseCmdDialog", "PushButton"))