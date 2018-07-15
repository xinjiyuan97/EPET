#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import GradeTable
import score
import Login
import CourseForm
import ServerConnection
import time

global CourseName,ClassRoom

def LabId(ClassRoom):
    LabList=ServerConnection.LabList()
    for i in range(len(LabList)):
        if LabList[i]['labNum']==ClassRoom:
            return(LabList[i]['id'])
    return None

def LoginCheck():
    username=lg.edit_user_name.text()
    passwd=lg.edit_password.text()
    Status=ServerConnection.login(username,passwd)
    if Status:
        cf.show()
        lg.close()
    else:
        QMessageBox.information(lg, u"登录失败", u"用户名或密码错误")

def ConfirmCheck():
    global CourseName,ClassRoom
    CourseName=cf.comboBox_2.currentText()
    ClassRoom=cf.comboBox.currentText()
    Id=LabId(ClassRoom)
    if Id!=None:
        ServerConnection.LabUpdate(Id,ClassRoom,'OPEN')
    cf.close()
    sc.label_10.setText(CourseName)
    sc.show()

def SetTime():
    TimeStr=time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    #sc.label_3.setText(TimeStr)

def CourseListInit(w):
    CourseData=ServerConnection.CourseList()
    for i in range(len(CourseData)):
        w.comboBox_2.addItem(CourseData[i]['Title'])

class GT(QMainWindow,GradeTable.Ui_GradeTable):
    def __init__(self,parent=None):
        super(GT,self).__init__(parent)
        self.setupUi(self)

class SC(QMainWindow,score.Ui_Score):
    def __init__(self,parent=None):
        super(SC,self).__init__(parent)
        self.setupUi(self)
        self.label_3.setText( "0人")
        #self.label_8.setText(_translate("GradeTable", "肖瑾", None))
        #self.label_5.setText(_translate("GradeTable", "15", None))
        #self.timer.timeout.connect(SetTime)
        #self.timer.start()

class LG(QMainWindow,Login.Ui_LoginForm):

    def __init__(self,parent=None):
        super(LG,self).__init__(parent)
        self.setupUi(self)
        login_button=self.Login
        user_name=self.edit_user_name
        login_button.clicked.connect(LoginCheck)


class CF(QDialog,CourseForm.Ui_CourseForm):
    def __init__(self,parent=None):
        super(CF,self).__init__(parent)
        self.setupUi(self)
        confirm_button=self.ok
        confirm_button.clicked.connect(ConfirmCheck)
        CourseListInit(self)


app=QApplication(sys.argv)
mw=GT()
sc=SC()
lg=LG()
cf=CF()
#mw.show()
#sc.show()
lg.show()
#cf.show()
app.exec_()
