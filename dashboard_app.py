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
import sys
import yaml

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(743, 584)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/fsu.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox_launchpad_window = QtGui.QGroupBox(Form)
        self.groupBox_launchpad_window.setGeometry(QtCore.QRect(300, 490, 151, 91))
        self.groupBox_launchpad_window.setStyleSheet(_fromUtf8("background-image: url(:/icon/download (2).png);"))
        self.groupBox_launchpad_window.setObjectName(_fromUtf8("groupBox_launchpad_window"))
        self.pushButton_First_Shortcut = QtGui.QPushButton(self.groupBox_launchpad_window)
        self.pushButton_First_Shortcut.setGeometry(QtCore.QRect(0, 40, 25, 19))
        self.pushButton_First_Shortcut.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_First_Shortcut.setIcon(icon1)
        self.pushButton_First_Shortcut.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_First_Shortcut.setObjectName(_fromUtf8("pushButton_First_Shortcut"))
        self.pushButton_Second_Shortcut = QtGui.QPushButton(self.groupBox_launchpad_window)
        self.pushButton_Second_Shortcut.setGeometry(QtCore.QRect(40, 40, 25, 19))
        self.pushButton_Second_Shortcut.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Second_Shortcut.setIcon(icon2)
        self.pushButton_Second_Shortcut.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Second_Shortcut.setObjectName(_fromUtf8("pushButton_Second_Shortcut"))
        self.pushButton_Third_Shortcut = QtGui.QPushButton(self.groupBox_launchpad_window)
        self.pushButton_Third_Shortcut.setGeometry(QtCore.QRect(80, 40, 25, 19))
        self.pushButton_Third_Shortcut.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Third_Shortcut.setIcon(icon3)
        self.pushButton_Third_Shortcut.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Third_Shortcut.setObjectName(_fromUtf8("pushButton_Third_Shortcut"))
        self.pushButton_Settings_Button = QtGui.QPushButton(self.groupBox_launchpad_window)
        self.pushButton_Settings_Button.setGeometry(QtCore.QRect(130, 10, 16, 16))
        self.pushButton_Settings_Button.setStyleSheet(_fromUtf8("image: url(:/icon/download (3).png);"))
        self.pushButton_Settings_Button.setObjectName(_fromUtf8("pushButton_Settings_Button"))
        self.label_FSU_LaunchPad = QtGui.QLabel(self.groupBox_launchpad_window)
        self.label_FSU_LaunchPad.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FSU_LaunchPad.setFont(font)
        self.label_FSU_LaunchPad.setObjectName(_fromUtf8("label_FSU_LaunchPad"))
        self.groupBox_Settings = QtGui.QGroupBox(Form)
        self.groupBox_Settings.setGeometry(QtCore.QRect(160, 70, 451, 481))
        self.groupBox_Settings.setStyleSheet(_fromUtf8("background-image: url(:/icon/download.jpg);\n"
""))
        self.groupBox_Settings.setObjectName(_fromUtf8("groupBox_Settings"))
        self.groupBox_Settings.hide()
        self.line_2 = QtGui.QFrame(self.groupBox_Settings)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 451, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_FSU_Settings = QtGui.QLabel(self.groupBox_Settings)
        self.label_FSU_Settings.setGeometry(QtCore.QRect(10, 5, 141, 21))
        self.label_FSU_Settings.setObjectName(_fromUtf8("label_FSU_Settings"))
        self.label_Launcher_logo = QtGui.QLabel(self.groupBox_Settings)
        self.label_Launcher_logo.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_Launcher_logo.setObjectName(_fromUtf8("label_Launcher_logo"))
        self.label_Pin__To_Taskbar = QtGui.QLabel(self.groupBox_Settings)
        self.label_Pin__To_Taskbar.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_Pin__To_Taskbar.setObjectName(_fromUtf8("label_Pin__To_Taskbar"))
        self.label_Launch_At_Startup = QtGui.QLabel(self.groupBox_Settings)
        self.label_Launch_At_Startup.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_Launch_At_Startup.setObjectName(_fromUtf8("label_Launch_At_Startup"))
        self.label_Primary_Color = QtGui.QLabel(self.groupBox_Settings)
        self.label_Primary_Color.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_Primary_Color.setObjectName(_fromUtf8("label_Primary_Color"))
        self.label_Secondary_Color = QtGui.QLabel(self.groupBox_Settings)
        self.label_Secondary_Color.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_Secondary_Color.setObjectName(_fromUtf8("label_Secondary_Color"))
        self.label_Shortcuts = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcuts.setGeometry(QtCore.QRect(20, 200, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_Shortcuts.setFont(font)
        self.label_Shortcuts.setStyleSheet(_fromUtf8("font: 87 10pt \"Arial Black\";"))
        self.label_Shortcuts.setObjectName(_fromUtf8("label_Shortcuts"))
        self.label_Shortcut1_Name = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut1_Name.setGeometry(QtCore.QRect(40, 240, 31, 16))
        self.label_Shortcut1_Name.setObjectName(_fromUtf8("label_Shortcut1_Name"))
        self.label_Shortcut1_URL = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut1_URL.setGeometry(QtCore.QRect(200, 240, 91, 16))
        self.label_Shortcut1_URL.setObjectName(_fromUtf8("label_Shortcut1_URL"))
        self.pushButton_Publish_Changes = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Publish_Changes.setGeometry(QtCore.QRect(350, 440, 91, 31))
        self.pushButton_Publish_Changes.setAutoFillBackground(False)
        self.pushButton_Publish_Changes.setStyleSheet(_fromUtf8("background-image: url(:/icon/download (2).png);"))
        self.pushButton_Publish_Changes.setObjectName(_fromUtf8("pushButton_Publish_Changes"))
        self.pushButton_Close = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Close.setGeometry(QtCore.QRect(230, 440, 91, 31))
        self.pushButton_Close.setAutoFillBackground(False)
        self.pushButton_Close.setStyleSheet(_fromUtf8("background-image: url(:/icon/download (2).png);"))
        self.pushButton_Close.setObjectName(_fromUtf8("pushButton_Close"))
        self.pushButton_Plus_Sign = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Plus_Sign.setGeometry(QtCore.QRect(100, 200, 16, 16))
        self.pushButton_Plus_Sign.setObjectName(_fromUtf8("pushButton_Plus_Sign"))
        self.lineEdit_Launcher_Logo = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Launcher_Logo.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_Launcher_Logo.setObjectName(_fromUtf8("lineEdit_Launcher_Logo"))
        self.lineEdit_Shortcut1_Name = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut1_Name.setGeometry(QtCore.QRect(80, 240, 113, 20))
        self.lineEdit_Shortcut1_Name.setObjectName(_fromUtf8("lineEdit_Shortcut1_Name"))
        self.lineEdit_Shortcut1_URL = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut1_URL.setGeometry(QtCore.QRect(302, 240, 141, 20))
        self.lineEdit_Shortcut1_URL.setObjectName(_fromUtf8("lineEdit_Shortcut1_URL"))
        self.checkBox_Pin_Taskbar = QtGui.QCheckBox(self.groupBox_Settings)
        self.checkBox_Pin_Taskbar.setGeometry(QtCore.QRect(120, 80, 70, 17))
        self.checkBox_Pin_Taskbar.setText(_fromUtf8(""))
        self.checkBox_Pin_Taskbar.setObjectName(_fromUtf8("checkBox_Pin_Taskbar"))
        self.checkBox_Launch_startup = QtGui.QCheckBox(self.groupBox_Settings)
        self.checkBox_Launch_startup.setGeometry(QtCore.QRect(120, 110, 70, 17))
        self.checkBox_Launch_startup.setText(_fromUtf8(""))
        self.checkBox_Launch_startup.setObjectName(_fromUtf8("checkBox_Launch_startup"))
        self.pushButton_Launcher_logo = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Launcher_logo.setGeometry(QtCore.QRect(230, 50, 25, 19))
        self.pushButton_Launcher_logo.setText(_fromUtf8(""))
        self.pushButton_Launcher_logo.setIcon(icon)
        self.pushButton_Launcher_logo.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Launcher_logo.setObjectName(_fromUtf8("pushButton_Launcher_logo"))
        self.pushButton_Primary_Color = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Primary_Color.setGeometry(QtCore.QRect(110, 140, 101, 19))
        self.pushButton_Primary_Color.setMaximumSize(QtCore.QSize(101, 19))
        self.pushButton_Primary_Color.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/download (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Primary_Color.setIcon(icon4)
        self.pushButton_Primary_Color.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_Primary_Color.setObjectName(_fromUtf8("pushButton_Primary_Color"))
        self.pushButton_Secondary_Color = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Secondary_Color.setGeometry(QtCore.QRect(110, 170, 101, 19))
        self.pushButton_Secondary_Color.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Secondary_Color.setIcon(icon5)
        self.pushButton_Secondary_Color.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_Secondary_Color.setObjectName(_fromUtf8("pushButton_Secondary_Color"))
        self.pushButton_Shortcut1_icon = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Shortcut1_icon.setGeometry(QtCore.QRect(10, 240, 25, 19))
        self.pushButton_Shortcut1_icon.setText(_fromUtf8(""))
        self.pushButton_Shortcut1_icon.setIcon(icon1)
        self.pushButton_Shortcut1_icon.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Shortcut1_icon.setObjectName(_fromUtf8("pushButton_Shortcut1_icon"))
        self.pushButton_Shortcut2_icon = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Shortcut2_icon.setGeometry(QtCore.QRect(10, 280, 25, 19))
        self.pushButton_Shortcut2_icon.setText(_fromUtf8(""))
        self.pushButton_Shortcut2_icon.setIcon(icon2)
        self.pushButton_Shortcut2_icon.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Shortcut2_icon.setObjectName(_fromUtf8("pushButton_Shortcut2_icon"))
        self.label_Shortcut2_Name = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut2_Name.setGeometry(QtCore.QRect(40, 280, 31, 16))
        self.label_Shortcut2_Name.setObjectName(_fromUtf8("label_Shortcut2_Name"))
        self.lineEdit_Shortcut2_Name = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut2_Name.setGeometry(QtCore.QRect(80, 280, 113, 20))
        self.lineEdit_Shortcut2_Name.setObjectName(_fromUtf8("lineEdit_Shortcut2_Name"))
        self.label_Shortcut2_URL = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut2_URL.setGeometry(QtCore.QRect(200, 280, 91, 16))
        self.label_Shortcut2_URL.setObjectName(_fromUtf8("label_Shortcut2_URL"))
        self.lineEdit_Shortcut2_URL = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut2_URL.setGeometry(QtCore.QRect(300, 280, 141, 20))
        self.lineEdit_Shortcut2_URL.setObjectName(_fromUtf8("lineEdit_Shortcut2_URL"))
        self.pushButton_Shortcut3_icon = QtGui.QPushButton(self.groupBox_Settings)
        self.pushButton_Shortcut3_icon.setGeometry(QtCore.QRect(10, 320, 25, 19))
        self.pushButton_Shortcut3_icon.setText(_fromUtf8(""))
        self.pushButton_Shortcut3_icon.setIcon(icon3)
        self.pushButton_Shortcut3_icon.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Shortcut3_icon.setObjectName(_fromUtf8("pushButton_Shortcut3_icon"))
        self.label_Shortcut3_Name = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut3_Name.setGeometry(QtCore.QRect(40, 320, 31, 16))
        self.label_Shortcut3_Name.setObjectName(_fromUtf8("label_Shortcut3_Name"))
        self.lineEdit_Shortcut3_Name = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut3_Name.setGeometry(QtCore.QRect(80, 320, 113, 20))
        self.lineEdit_Shortcut3_Name.setObjectName(_fromUtf8("lineEdit_Shortcut3_Name"))
        self.label_Shortcut3_URL = QtGui.QLabel(self.groupBox_Settings)
        self.label_Shortcut3_URL.setGeometry(QtCore.QRect(200, 320, 91, 16))
        self.label_Shortcut3_URL.setObjectName(_fromUtf8("label_Shortcut3_URL"))
        self.lineEdit_Shortcut3_URL = QtGui.QLineEdit(self.groupBox_Settings)
        self.lineEdit_Shortcut3_URL.setGeometry(QtCore.QRect(300, 320, 141, 20))
        self.lineEdit_Shortcut3_URL.setObjectName(_fromUtf8("lineEdit_Shortcut3_URL"))
        self.groupBox_Add_shortcut = QtGui.QGroupBox(self.groupBox_Settings)
        self.groupBox_Add_shortcut.setGeometry(QtCore.QRect(120, 140, 261, 161))
        self.groupBox_Add_shortcut.setObjectName(_fromUtf8("groupBox_Add_shortcut"))
        self.groupBox_Add_shortcut.hide()
        self.line_3 = QtGui.QFrame(self.groupBox_Add_shortcut)
        self.line_3.setGeometry(QtCore.QRect(0, 20, 261, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_Add_a_Shortcut = QtGui.QLabel(self.groupBox_Add_shortcut)
        self.label_Add_a_Shortcut.setGeometry(QtCore.QRect(10, 3, 141, 20))
        self.label_Add_a_Shortcut.setObjectName(_fromUtf8("label_Add_a_Shortcut"))
        self.label_New_shortcut_Name = QtGui.QLabel(self.groupBox_Add_shortcut)
        self.label_New_shortcut_Name.setGeometry(QtCore.QRect(70, 50, 31, 16))
        self.label_New_shortcut_Name.setObjectName(_fromUtf8("label_New_shortcut_Name"))
        self.label_New_shortcut_URL = QtGui.QLabel(self.groupBox_Add_shortcut)
        self.label_New_shortcut_URL.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_New_shortcut_URL.setObjectName(_fromUtf8("label_New_shortcut_URL"))
        self.label_New_icon = QtGui.QLabel(self.groupBox_Add_shortcut)
        self.label_New_icon.setGeometry(QtCore.QRect(20, 120, 25, 19))
        self.label_New_icon.setText(_fromUtf8(""))
        self.label_New_icon.setObjectName(_fromUtf8("label_New_icon"))
        self.pushButton_Add_Icon = QtGui.QPushButton(self.groupBox_Add_shortcut)
        self.pushButton_Add_Icon.setGeometry(QtCore.QRect(70, 120, 75, 23))
        self.pushButton_Add_Icon.setObjectName(_fromUtf8("pushButton_Add_Icon"))
        self.pushButton_OK = QtGui.QPushButton(self.groupBox_Add_shortcut)
        self.pushButton_OK.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.pushButton_OK.setObjectName(_fromUtf8("pushButton_OK"))
        self.lineEdit_Name_Add_shortcut = QtGui.QLineEdit(self.groupBox_Add_shortcut)
        self.lineEdit_Name_Add_shortcut.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit_Name_Add_shortcut.setObjectName(_fromUtf8("lineEdit_Name_Add_shortcut"))
        self.lineEdit_URL_Add_shortcut = QtGui.QLineEdit(self.groupBox_Add_shortcut)
        self.lineEdit_URL_Add_shortcut.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_URL_Add_shortcut.setObjectName(_fromUtf8("lineEdit_URL_Add_shortcut"))
        self.widget_New_shortcut_row = QtGui.QWidget(self.groupBox_Settings)
        self.widget_New_shortcut_row.setGeometry(QtCore.QRect(0, 350, 451, 51))
        self.widget_New_shortcut_row.setObjectName(_fromUtf8("widget_New_shortcut_row"))
        self.widget_New_shortcut_row.hide()
        self.label_Shortcut4_New_Icon = QtGui.QLabel(self.widget_New_shortcut_row)
        self.label_Shortcut4_New_Icon.setGeometry(QtCore.QRect(10, 10, 25, 19))
        self.label_Shortcut4_New_Icon.setText(_fromUtf8(""))
        self.label_Shortcut4_New_Icon.setObjectName(_fromUtf8("label_Shortcut4_New_Icon"))
        self.label_New_Shortcut_Name = QtGui.QLabel(self.widget_New_shortcut_row)
        self.label_New_Shortcut_Name.setGeometry(QtCore.QRect(40, 10, 31, 16))
        self.label_New_Shortcut_Name.setObjectName(_fromUtf8("label_New_Shortcut_Name"))
        self.lineEdit_New_Shortcut_Name = QtGui.QLineEdit(self.widget_New_shortcut_row)
        self.lineEdit_New_Shortcut_Name.setGeometry(QtCore.QRect(80, 10, 113, 20))
        self.lineEdit_New_Shortcut_Name.setObjectName(_fromUtf8("lineEdit_New_Shortcut_Name"))
        self.label_New_Shortcut_URL = QtGui.QLabel(self.widget_New_shortcut_row)
        self.label_New_Shortcut_URL.setGeometry(QtCore.QRect(200, 10, 91, 16))
        self.label_New_Shortcut_URL.setObjectName(_fromUtf8("label_New_Shortcut_URL"))
        self.lineEdit_New_Shortcut_URL = QtGui.QLineEdit(self.widget_New_shortcut_row)
        self.lineEdit_New_Shortcut_URL.setGeometry(QtCore.QRect(300, 10, 141, 20))
        self.lineEdit_New_Shortcut_URL.setObjectName(_fromUtf8("lineEdit_New_Shortcut_URL"))
        self.pushButton_new_launchpad_icon = QtGui.QPushButton(self.groupBox_launchpad_window)
        self.pushButton_new_launchpad_icon.setGeometry(QtCore.QRect(120, 40, 25, 19))
        self.pushButton_new_launchpad_icon.setText(_fromUtf8(""))
        self.pushButton_new_launchpad_icon.setObjectName(_fromUtf8("pushButton_new_launchpad_icon"))
        self.pushButton_new_launchpad_icon.hide()

        ########################################
        def pipelinebrowser():
            subprocess.call("C:\Users\ishita\PycharmProjects\core_tools\src\apps\browser\main.py")

        self.pushButton_Third_Shortcut.clicked.connect(pipelinebrowser)

        def browser():
            self.url = self.lineEdit_Shortcut1_URL.text()
            url = self.lineEdit_Shortcut1_URL.text()
            print url
            print self.lineEdit_Shortcut1_URL.text()
            webbrowser.open_new(url)
                
        def book():
            self.url2 = self.lineEdit_Shortcut2_URL.text()
            url2 = self.lineEdit_Shortcut2_URL.text()
            print url2
            print self.lineEdit_Shortcut2_URL.text()
            webbrowser.open_new(url2)


        #pushButton1 is the browser icon
        self.pushButton_First_Shortcut.clicked.connect(browser)


        #pushButton_2 is the book icon
        self.pushButton_Second_Shortcut.clicked.connect(book)


            
        def publish():
            config_file = r"C:\Users\ishita\PycharmProjects\launchpad\config.yaml"

            def load_yaml(path):
                with open(path, 'r') as stream:
                    try:
                        result = yaml.load(stream)
                        if result:
                            return result
                        else:
                            return {}
                    except yaml.YAMLError as exc:
                        print(exc)
                        sys.exit(99)

            def write_yaml(outfile, d):
                with open(outfile, 'w') as outfile:
                    yaml.dump(d, outfile, default_flow_style=False)

            self.name1 = self.lineEdit_Shortcut1_Name.text()
            name1 = self.lineEdit_Shortcut1_Name.text()
            self.url1 = self.lineEdit_Shortcut1_URL.text()
            url1 = self.lineEdit_Shortcut1_URL.text()

            self.name2 = self.lineEdit_Shortcut2_Name.text()
            name2 = self.lineEdit_Shortcut2_Name.text()
            self.url2 = self.lineEdit_Shortcut2_URL.text()
            url2 = self.lineEdit_Shortcut2_URL.text()

            self.name3 = self.lineEdit_Shortcut3_Name.text()
            name3 = self.lineEdit_Shortcut3_Name.text()
            self.url3 = self.lineEdit_Shortcut3_URL.text()
            url3 = self.lineEdit_Shortcut3_URL.text()

            self.name4 = self.lineEdit_New_Shortcut_Name.text()
            name4 = self.lineEdit_New_Shortcut_Name.text()
            self.url4 = self.lineEdit_New_Shortcut_URL.text()
            url4 = self.lineEdit_New_Shortcut_URL.text()

            dict = load_yaml(config_file)
            dict['shortcuts'][str(name1)] = str(url1)
            dict['shortcuts'][str(name2)] = str(url2)
            dict['shortcuts'][str(name3)] = str(url3)
            dict['shortcuts'][str(name4)] = str(url4)

            write_yaml(config_file, dict)

            self.groupBox_Settings.hide()



        #pushButton_6 is the Publish Button
        self.pushButton_Publish_Changes.clicked.connect(publish)


        def addicon():
            iconpath = QtGui.QFileDialog.getOpenFileName(caption='Open File', directory="/Desktop", filter="*.png *.xpm *.jpg")
            print iconpath
            self.link = str(iconpath)
            link = str(iconpath)
            self.label_New_icon.setPixmap(QtGui.QPixmap(iconpath))
            self.label_New_icon.setScaledContents(True)
            self.label_Shortcut4_New_Icon.setPixmap(QtGui.QPixmap(link))
            self.label_Shortcut4_New_Icon.setScaledContents(True)
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap(_fromUtf8(link)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_new_launchpad_icon.setIcon(icon6)
            self.pushButton_new_launchpad_icon.setIconSize(QtCore.QSize(25, 25))

        #pushButton_10 is the Add Icon button
        self.pushButton_Add_Icon.clicked.connect(addicon)

        def OK():
            self.name1 = self.lineEdit_Name_Add_shortcut.text()
            name1 = self.lineEdit_Name_Add_shortcut.text()
            self.lineEdit_New_Shortcut_Name.setText(name1)
            self.name2 = self.lineEdit_URL_Add_shortcut.text()
            name2 = self.lineEdit_URL_Add_shortcut.text()
            self.lineEdit_New_Shortcut_URL.setText(name2)
            self.groupBox_Add_shortcut.hide()
            self.pushButton_new_launchpad_icon.show()

        # pushButton_11 is the OK button
        self.pushButton_OK.clicked.connect(OK)

        def newicon():
            self.url4 = self.lineEdit_New_Shortcut_URL.text()
            url4 = self.lineEdit_New_Shortcut_URL.text()
            print url4
            print self.lineEdit_New_Shortcut_URL.text()
            webbrowser.open_new(url4)

        self.pushButton_new_launchpad_icon.clicked.connect(newicon)

        def closedialog():
            self.groupBox_Settings.hide()

        self.pushButton_Close.clicked.connect(closedialog)





        ##########################################
        
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_Settings_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox_Settings.show)
        QtCore.QObject.connect(self.pushButton_Plus_Sign, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox_Add_shortcut.show)
        QtCore.QObject.connect(self.pushButton_OK, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_New_shortcut_row.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LaunchPad", None))
        self.label_FSU_LaunchPad.setText(_translate("Form", "FSU LaunchPad", None))
        self.label_FSU_Settings.setText(_translate("Form", "FSU Launch Pad Settings", None))
        self.label_Launcher_logo.setText(_translate("Form", "Launcher Logo", None))
        self.label_Pin__To_Taskbar.setText(_translate("Form", "Pin To Taskbar", None))
        self.label_Launch_At_Startup.setText(_translate("Form", "Launch At Startup", None))
        self.label_Primary_Color.setText(_translate("Form", "Primary Color", None))
        self.label_Secondary_Color.setText(_translate("Form", "Secondary Color", None))
        self.label_Shortcuts.setText(_translate("Form", "Shortcuts", None))
        self.label_Shortcut1_Name.setText(_translate("Form", "Name:", None))
        self.label_Shortcut1_URL.setText(_translate("Form", "URL/Program Path", None))
        self.pushButton_Publish_Changes.setText(_translate("Form", "Publish Changes", None))
        self.pushButton_Close.setText(_translate("Form", "Close", None))
        self.pushButton_Plus_Sign.setText(_translate("Form", "+", None))
        self.label_Shortcut2_Name.setText(_translate("Form", "Name:", None))
        self.label_Shortcut2_URL.setText(_translate("Form", "URL/Program Path", None))
        self.label_Shortcut3_Name.setText(_translate("Form", "Name:", None))
        self.label_Shortcut3_URL.setText(_translate("Form", "URL/Program Path", None))
        self.label_Add_a_Shortcut.setText(_translate("Form", "Add a Shortcut", None))
        self.label_New_shortcut_Name.setText(_translate("Form", "Name:", None))
        self.label_New_shortcut_URL.setText(_translate("Form", "URL/Program Path", None))
        self.pushButton_Add_Icon.setText(_translate("Form", "Add Icon", None))
        self.pushButton_OK.setText(_translate("Form", "OK", None))
        self.label_New_Shortcut_Name.setText(_translate("Form", "Name:", None))
        self.label_New_Shortcut_URL.setText(_translate("Form", "URL/Program Path", None))
        self.lineEdit_Shortcut1_Name.setText(_translate("Form", "Google", None))
        self.lineEdit_Shortcut1_URL.setText(_translate("Form", "https://www.google.com/", None))
        self.lineEdit_Shortcut2_Name.setText(_translate("Form", "Handbook", None))
        self.lineEdit_Shortcut2_URL.setText(_translate("Form", "http://cmpahandbook.com/", None))
        self.lineEdit_Shortcut3_Name.setText(_translate("Form", "Pipeline", None))
        self.lineEdit_Shortcut3_URL.setText(_translate("Form", "C:\Users\ishita\PycharmProjects\core_tools\src\apps\browser", None))


import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.setWindowIcon(QtGui.QIcon(":/icon/fsu.jpg"))
    w = QtGui.QWidget()
    trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(":/icon/fsu.jpg"), w)
    trayIcon.show()
    sys.exit(app.exec_())

