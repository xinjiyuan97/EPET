# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
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

class Ui_Score(object):
    def setupUi(self, Score):
        Score.setObjectName(_fromUtf8("Score"))
        Score.resize(1298, 820)
        self.centralwidget = QtGui.QWidget(Score)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 781, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(281, 50, 781, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1080, 720, 51, 29))
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1130, 720, 158, 20))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(810, 130, 481, 571))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableView = QtGui.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalScrollBar = QtGui.QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.horizontalScrollBar = QtGui.QScrollBar(self.gridLayoutWidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.gridLayout.addWidget(self.horizontalScrollBar, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1210, 750, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(280, 90, 781, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_14 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.label_14)
        self.label_13 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 130, 791, 571))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 720, 131, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Score.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Score)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEPET = QtGui.QMenu(self.menubar)
        self.menuEPET.setObjectName(_fromUtf8("menuEPET"))
        Score.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Score)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Score.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEPET.menuAction())

        self.retranslateUi(Score)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Score)

    def retranslateUi(self, Score):
        Score.setWindowTitle(_translate("Score", "打分页面", None))
        self.label_9.setText(_translate("Score", "实验：", None))
        self.label_10.setText(_translate("Score", "直流电路的构建与测量", None))
        self.label_8.setText(_translate("Score", "评分队列", None))
        self.label_2.setText(_translate("Score", "待评分：", None))
        self.label_3.setText(_translate("Score", "5人", None))
        self.label_5.setText(_translate("Score", "待评测实验项目编号：", None))
        self.label_4.setText(_translate("Score", "03", None))
        self.label_6.setText(_translate("Score", "学生座位号：", None))
        self.label_7.setText(_translate("Score", "11", None))
        self.label.setText(_translate("Score", "<html><head/><body><p><span style=\" font-size:11pt;\">评分：</span></p></body></html>", None))
        self.comboBox.addItem(_translate("Score", "通过", None))
        self.comboBox.addItem(_translate("Score", "不通过", None))
        self.pushButton.setText(_translate("Score", "提交评分", None))
        self.label_14.setText(_translate("Score", "姓名：", None))
        self.label_13.setText(_translate("Score", "蔡逸熙", None))
        self.label_12.setText(_translate("Score", "    学号：", None))
        self.label_11.setText(_translate("Score", "16031154", None))
        self.pushButton_2.setText(_translate("Score", "结束实验", None))
        self.menuEPET.setTitle(_translate("Score", "EPET", None))

