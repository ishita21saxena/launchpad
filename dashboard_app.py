# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_app.ui'
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

import webbrowser
import subprocess

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(743, 584)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(300, 490, 151, 91))
        self.widget.setStyleSheet(_fromUtf8("background-image: url(:/icon/download (2).png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton1 = QtGui.QPushButton(self.widget)
        self.pushButton1.setGeometry(QtCore.QRect(10, 40, 25, 19))
        self.pushButton1.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton1.setIcon(icon1)
        self.pushButton1.setIconSize(QtCore.QSize(25, 25))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 40, 25, 19))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 40, 25, 19))
        self.pushButton_3.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 10, 16, 16))
        self.pushButton_4.setStyleSheet(_fromUtf8("image: url(:/icon/download (3).png);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 10, 451, 481))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-image: url(:/icon/download.jpg);\n"
""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_2.hide()
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 451, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 5, 141, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("font: 87 10pt \"Arial Black\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(40, 240, 31, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(200, 240, 91, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 440, 91, 31))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-image: url(:/icon/download (2).png);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 200, 16, 16))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 240, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(302, 240, 141, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(120, 80, 70, 17))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 110, 70, 17))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton2.setGeometry(QtCore.QRect(110, 140, 101, 19))
        self.pushButton2.setMaximumSize(QtCore.QSize(101, 19))
        self.pushButton2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon4)
        self.pushButton2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton_21 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_21.setGeometry(QtCore.QRect(110, 170, 101, 19))
        self.pushButton_21.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 240, 25, 19))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 280, 25, 19))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(40, 280, 31, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 280, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(200, 280, 91, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 280, 141, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 320, 25, 19))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(40, 320, 31, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 320, 113, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(200, 320, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(300, 320, 141, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(120, 140, 261, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox.hide()
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 20, 261, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 3, 141, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(70, 50, 31, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 120, 25, 19))
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 120, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.widget_2 = QtGui.QWidget(self.groupBox_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 350, 451, 51))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_2.hide()
        self.label_19 = QtGui.QLabel(self.widget_2)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 25, 19))
        self.label_19.setText(_fromUtf8(""))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.widget_2)
        self.label_20.setGeometry(QtCore.QRect(40, 10, 31, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit_10 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 10, 113, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_21 = QtGui.QLabel(self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(200, 10, 91, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_11 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(300, 10, 141, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))

        ########################################
        def pipelinebrowser():
            subprocess.call("C:\Users\ishita\PycharmProjects\core_tools\src\apps\browser\main.py")

        self.pushButton_3.clicked.connect(pipelinebrowser)

        def google():
            webbrowser.open("https://www.google.com/",new=2)

        def handbook():
            webbrowser.open("http://cmpahandbook.com/",new=2)
        
        def browser():
            self.url = self.lineEdit_5.text()
            url = self.lineEdit_5.text()
            print url
            print self.lineEdit_5.text()
            webbrowser.open_new(url)
                
        def book():
            self.url2 = self.lineEdit_7.text()
            url2 = self.lineEdit_7.text()
            print url2
            print self.lineEdit_7.text()
            webbrowser.open_new(url2)

        if (self.lineEdit_5.textChanged):
            #pushButton1 is the browser icon
            self.pushButton1.clicked.connect(browser)
        else:
            self.pushButton1.clicked.connect(google)

        if (self.lineEdit_7.textChanged):
            #pushButton_2 is the book icon
            self.pushButton_2.clicked.connect(book)
        else:
            self.pushButton_2.clicked.connect(handbook)
            
        def publish():
            self.groupBox_2.hide()
        #pushButton_6 is the Publish Button
        self.pushButton_6.clicked.connect(publish)



        def addicon():
            iconpath = QtGui.QFileDialog.getOpenFileName(caption='Open File', directory="/Desktop", filter="*.png *.xpm *.jpg")
            print iconpath
            self.link = str(iconpath)
            link = str(iconpath)
            self.label_18.setPixmap(QtGui.QPixmap(iconpath))
            self.label_18.setScaledContents(True)
            self.label_19.setPixmap(QtGui.QPixmap(link))
            self.label_19.setScaledContents(True)

        #pushButton_10 is the Add Icon button
        self.pushButton_10.clicked.connect(addicon)

        def OK():
            self.name1 = self.lineEdit_2.text()
            name1 = self.lineEdit_2.text()
            self.lineEdit_10.setText(name1)
            self.name2 = self.lineEdit_3.text()
            name2 = self.lineEdit_3.text()
            self.lineEdit_11.setText(name2)
            self.groupBox.hide()

        # pushButton_11 is the OK button
        self.pushButton_11.clicked.connect(OK)

        ##########################################
        
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox_2.show)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox.show)
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_2.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LaunchPad", None))
        self.pushButton_4.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "FSU LaunchPad", None))
        self.label_2.setText(_translate("Form", "FSU Launch Pad Settings", None))
        self.label_3.setText(_translate("Form", "Launcher Logo", None))
        self.label_4.setText(_translate("Form", "Pin To Taskbar", None))
        self.label_5.setText(_translate("Form", "Launch At Startup", None))
        self.label_6.setText(_translate("Form", "Primary Color", None))
        self.label_7.setText(_translate("Form", "Secondary Color", None))
        self.label_8.setText(_translate("Form", "Shortcuts", None))
        self.label_9.setText(_translate("Form", "Name:", None))
        self.label_10.setText(_translate("Form", "URL/Program Path", None))
        self.pushButton_6.setText(_translate("Form", "Publish Changes", None))
        self.pushButton_7.setText(_translate("Form", "+", None))
        self.label_11.setText(_translate("Form", "Name:", None))
        self.label_12.setText(_translate("Form", "URL/Program Path", None))
        self.label_13.setText(_translate("Form", "Name:", None))
        self.label_14.setText(_translate("Form", "URL/Program Path", None))
        self.label_15.setText(_translate("Form", "Add a Shortcut", None))
        self.label_16.setText(_translate("Form", "Name:", None))
        self.label_17.setText(_translate("Form", "URL/Program Path", None))
        self.pushButton_10.setText(_translate("Form", "Add Icon", None))
        self.pushButton_11.setText(_translate("Form", "OK", None))
        self.label_20.setText(_translate("Form", "Name:", None))
        self.label_21.setText(_translate("Form", "URL/Program Path", None))
        self.label_14.setText(_translate("Form", "URL/Program Path", None))
        self.label_13.setText(_translate("Form", "Name:", None))
        self.lineEdit_4.setText(_translate("Form", "Google", None))
        self.lineEdit_5.setText(_translate("Form", "https://www.google.com/", None))
        self.lineEdit_6.setText(_translate("Form", "Handbook", None))
        self.lineEdit_7.setText(_translate("Form", "http://cmpahandbook.com/", None))
        self.lineEdit_8.setText(_translate("Form", "Pipeline", None))
        self.lineEdit_9.setText(_translate("Form", "C:\Users\ishita\PycharmProjects\core_tools\src\apps\browser", None))


import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

