# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GradeTable.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GradeTable(object):
    def setupUi(self, GradeTable):
        GradeTable.setObjectName(_fromUtf8("GradeTable"))
        GradeTable.resize(1111, 859)
        self.centralWidget = QtGui.QWidget(GradeTable)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 110, 1051, 641))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalScrollBar = QtGui.QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.horizontalScrollBar = QtGui.QScrollBar(self.gridLayoutWidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.gridLayout.addWidget(self.horizontalScrollBar, 1, 0, 1, 1)
        self.tableView = QtGui.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 1051, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 1051, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(960, 760, 121, 40))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        GradeTable.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(GradeTable)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1111, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuEPET = QtGui.QMenu(self.menuBar)
        self.menuEPET.setObjectName(_fromUtf8("menuEPET"))
        GradeTable.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(GradeTable)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        GradeTable.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(GradeTable)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        GradeTable.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuEPET.menuAction())

        self.retranslateUi(GradeTable)
        QtCore.QMetaObject.connectSlotsByName(GradeTable)

    def retranslateUi(self, GradeTable):
        GradeTable.setWindowTitle(_translate("GradeTable", "查看成绩单", None))
        self.label_2.setText(_translate("GradeTable", "  实验：", None))
        self.label.setText(_translate("GradeTable", "直流电路的构建与测量", None))
        self.label_4.setText(_translate("GradeTable", "时间：", None))
        self.label_3.setText(_translate("GradeTable", "2018/3/24 下午", None))
        self.label_7.setText(_translate("GradeTable", "任课老师：", None))
        self.label_8.setText(_translate("GradeTable", "肖瑾", None))
        self.label_6.setText(_translate("GradeTable", "实验人数：", None))
        self.label_5.setText(_translate("GradeTable", "15", None))
        self.commandLinkButton.setText(_translate("GradeTable", "保存实验数据", None))
        self.menuEPET.setTitle(_translate("GradeTable", "EPET", None))

