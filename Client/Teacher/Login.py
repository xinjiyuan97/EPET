# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
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

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName(_fromUtf8("LoginForm"))
        LoginForm.resize(450, 350)
        LoginForm.setStyleSheet(_fromUtf8("QGridLayout\n"
"{\n"
"    background:rgb(85, 170, 255)\n"
"}"))
        self.centralWidget = QtGui.QWidget(LoginForm)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.title = QtGui.QLabel(self.horizontalLayoutWidget)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout.addWidget(self.title)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 220, 441, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.Login = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.Login.setObjectName(_fromUtf8("Login"))
        self.horizontalLayout_2.addWidget(self.Login)
        #login_button=self.Login
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.register_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.register_2.setObjectName(_fromUtf8("register_2"))
        self.horizontalLayout_2.addWidget(self.register_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 60, 441, 161))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.password = QtGui.QLabel(self.gridLayoutWidget)
        self.password.setIndent(8)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.user_name = QtGui.QLabel(self.gridLayoutWidget)
        self.user_name.setTextFormat(QtCore.Qt.AutoText)
        self.user_name.setScaledContents(False)
        self.user_name.setWordWrap(False)
        self.user_name.setIndent(6)
        self.user_name.setObjectName(_fromUtf8("user_name"))
        self.gridLayout.addWidget(self.user_name, 0, 1, 1, 1)
        self.edit_user_name = QtGui.QLineEdit(self.gridLayoutWidget)
        self.edit_user_name.setObjectName(_fromUtf8("edit_user_name"))
        self.gridLayout.addWidget(self.edit_user_name, 0, 2, 1, 1)
        #user_name=self.edit_user_name
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        self.edit_password = QtGui.QLineEdit(self.gridLayoutWidget)
        self.edit_password.setObjectName(_fromUtf8("edit_password"))
        self.edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout.addWidget(self.edit_password, 1, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 3, 1, 1)
        LoginForm.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(LoginForm)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        LoginForm.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(LoginForm)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        LoginForm.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(LoginForm)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        LoginForm.setStatusBar(self.statusBar)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        #login_button.clicked.connect(showMsg)


    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(_translate("LoginForm", "用户登录", None))
        self.title.setText(_translate("LoginForm", "电气实践智能化平台", None))
        self.Login.setText(_translate("LoginForm", "登陆", None))
        self.register_2.setText(_translate("LoginForm", "注册", None))
        self.password.setText(_translate("LoginForm", "密 码", None))
        self.user_name.setText(_translate("LoginForm", "用户名", None))

