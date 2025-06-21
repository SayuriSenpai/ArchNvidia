# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bin import installer
import sys
import os 



class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form  # เก็บ reference ของหน้าต่าง/วิดเจ็ตที่กำลังเซ็ต UI ลงไป
        Form.setObjectName("Forms")
        Form.resize(546, 444)
        Form.setFixedSize(Form.size())
        self.backg = QtWidgets.QLabel(Form)
        self.backg.setGeometry(QtCore.QRect(-130, -20, 951, 461))
        self.backg.setAutoFillBackground(False)
        self.backg.setText("")
        self.backg.setPixmap(QtGui.QPixmap("Image/1255614-1920x1080-desktop-1080p-nvidia-background-image.jpg"))
        self.backg.setScaledContents(True)
        self.backg.setObjectName("backg")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(450, 10, 71, 61))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Image/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(130, 90, 391, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 361, 231))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 311, 51))
        self.label_2.setStyleSheet("font: 25px;")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(80, 50, 251, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.Text = QtWidgets.QLabel(Form)
        self.Text.setGeometry(QtCore.QRect(20, -30, 331, 121))
        self.Text.setMouseTracking(False)
        self.Text.setStyleSheet("color: lime; font: 25px;")
        self.Text.setObjectName("Text")
        self.Text_2 = QtWidgets.QLabel(Form)
        self.Text_2.setEnabled(True)
        self.Text_2.setGeometry(QtCore.QRect(20, 0, 201, 121))
        self.Text_2.setMouseTracking(False)
        self.Text_2.setStyleSheet("color: lime; font: 15px;")
        self.Text_2.setObjectName("Text_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-120, 130, 351, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Image/pngegg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Buttonbox = QtWidgets.QDialogButtonBox(Form)
        self.Buttonbox.setGeometry(QtCore.QRect(320, 370, 201, 51))
        self.Buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.Buttonbox.setCenterButtons(True)
        self.Buttonbox.setObjectName("Buttonbox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nvidia Installer v1.0 by Sayuri Senpai"))
        self.label_2.setText(_translate("Form", "Nvidia Installer v1.0"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Sans Semi-Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Easy Install and setup on Arch Linux </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Nvidia legacy Driver .. GT series GTX series </span>Package <span style=\" font-weight:600; font-style:italic;\">340xx 390xx 470xx 525xx 535xx</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Recommend 340xx 390xx </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arch Linux XFCE</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Cadit : </span><span style=\" font-style:italic;\">Sayuri Senpai</span></p></body></html>"))
        self.Text.setText(_translate("Form", "NVIDIA Graphics Driver"))
        self.Text_2.setText(_translate("Form", "Version Arch Linux"))

        self.Buttonbox.accepted.connect(self.on_yes_clicked)   # Yes จะส่ง accepted
        self.Buttonbox.rejected.connect(self.on_no_clicked) 
    
    

    def on_yes_clicked(self):
        os.system("clear")
        print("Next page ...")
        self.Form.close()   # ปิดหน้าต่างปัจจุบัน
        # สร้างหน้าต่างใหม่จาก gui2
        self.new_window = QtWidgets.QWidget()
        self.ui2 = installer.Ui_Form2()
        self.ui2.setupUi(self.new_window)
        self.new_window.show()
        print("page2 Running ")
            

    def on_no_clicked(self):
        print("ออกจากโปรแกรม , Exit to Program")
        self.Form.close() 
        self.new_window = QtWidgets.QWidget
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
