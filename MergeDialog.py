# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Merge.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MergeDialog(object):
    def setupUi(self, MergeDialog):
        MergeDialog.setObjectName("MergeDialog")
        MergeDialog.resize(411, 182)
        self.verticalLayout = QtWidgets.QVBoxLayout(MergeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_6 = QtWidgets.QWidget(MergeDialog)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.archive_input = QtWidgets.QComboBox(self.widget_6)
        self.archive_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.archive_input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.archive_input.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.archive_input.setEditable(True)
        self.archive_input.setObjectName("archive_input")
        self.archive_input.addItem("")
        self.archive_input.addItem("")
        self.archive_input.addItem("")
        self.horizontalLayout_3.addWidget(self.archive_input)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout.addWidget(self.widget_6)
        self.StartBtn = QtWidgets.QPushButton(MergeDialog)
        self.StartBtn.setObjectName("StartBtn")
        self.verticalLayout.addWidget(self.StartBtn)

        self.retranslateUi(MergeDialog)
        QtCore.QMetaObject.connectSlotsByName(MergeDialog)

    def retranslateUi(self, MergeDialog):
        _translate = QtCore.QCoreApplication.translate
        MergeDialog.setWindowTitle(_translate("MergeDialog", "Dialog"))
        self.label_10.setText(_translate("MergeDialog", "压缩格式"))
        self.archive_input.setItemText(0, _translate("MergeDialog", "Text"))
        self.archive_input.setItemText(1, _translate("MergeDialog", "Binary"))
        self.archive_input.setItemText(2, _translate("MergeDialog", "CompressedBinary"))
        self.StartBtn.setText(_translate("MergeDialog", "StartMerge"))
