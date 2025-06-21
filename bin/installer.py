# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import os




class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.window = Form
        Form.resize(546, 440)
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
        self.frame.setGeometry(QtCore.QRect(90, 100, 391, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 371, 231))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 31, 21))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Image/Symbol.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(130, 40, 161, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 80, 161, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 31, 21))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Image/Symbol.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(130, 120, 161, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 31, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Image/Symbol.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(130, 160, 161, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 160, 31, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Image/Symbol.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(130, 200, 161, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 200, 31, 21))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Image/Symbol.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
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
        self.Buttonbox = QtWidgets.QDialogButtonBox(Form)
        self.Buttonbox.setGeometry(QtCore.QRect(320, 370, 201, 51))
        self.Buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.Buttonbox.setCenterButtons(True)
        self.Buttonbox.setObjectName("Buttonbox")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 81, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Image/Linux.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-90, 190, 251, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Image/13.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome to My Program"))
        self.checkBox.setText(_translate("Form", "Driver version 340xx"))
        self.checkBox_2.setText(_translate("Form", "Driver version 390xx"))
        self.checkBox_3.setText(_translate("Form", "Driver version 470xx"))
        self.checkBox_4.setText(_translate("Form", "Driver version 525xx"))
        self.checkBox_5.setText(_translate("Form", "Driver version 535xx"))
        self.Text.setText(_translate("Form", "NVIDIA Graphics Driver"))
        self.Text_2.setText(_translate("Form", "Install Driver "))

        self.Buttonbox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.apply_selection)
        self.Buttonbox.accepted.connect(self.apply_selection)

        self.arr = []
    def apply_selection(self):
        selected_versions = []

        selected_count = sum([
            self.checkBox.isChecked(),
            self.checkBox_2.isChecked(),
            self.checkBox_3.isChecked(),
            self.checkBox_4.isChecked(),
            self.checkBox_5.isChecked()
        ])

        if selected_count != 1:
            QMessageBox.warning(None, "คำเตือน", "กรุณาเลือกเพียง 1 เวอร์ชันเท่านั้น")
            return

        if self.checkBox.isChecked():
            selected_versions.append("340xx")
            self.arr = (
            f"yay -S --noconfirm --removemake --answerdiff=None --answerclean=None "
            f"nvidia-{selected_versions[0]}-dkms "
            f"nvidia-{selected_versions[0]}-utils lib32-nvidia-{selected_versions[0]}-utils nvidia-settings"
            )
            os.system("clear && figlet Boot && echo 'Loading setup program please wait...' ")
            self.window.close()
            os.system(self.arr)
            os.system("echo Thank you")
           

        elif self.checkBox_2.isChecked():
            selected_versions.append("390xx")
            self.arr = (
            f"yay -S --noconfirm --removemake --answerdiff=None --answerclean=None "
            f"nvidia-{selected_versions[0]}-dkms "
            f"nvidia-{selected_versions[0]}-utils lib32-nvidia-{selected_versions[0]}-utils nvidia-settings"
            )
            self.window.close()
            os.system("clear && figlet Boot && echo 'Loading setup program please wait...' ")
            os.system(self.arr)
            

        elif self.checkBox_3.isChecked():
             selected_versions.append("470xx")
             self.arr = (
             f"yay -S --noconfirm --removemake --answerdiff=None --answerclean=None "
             f"nvidia-{selected_versions[0]}-dkms "
             f"nvidia-{selected_versions[0]}-utils lib32-nvidia-{selected_versions[0]}-utils nvidia-settings"
             )
             self.window.close()
             os.system("clear && figlet Boot && echo 'Loading setup program please wait...' ")
             os.system(self.arr)
            
             
             

        elif self.checkBox_4.isChecked():
            selected_versions.append("525xx")
            self.arr = (
            f"yay -S --noconfirm --removemake --answerdiff=None --answerclean=None "
            f"nvidia-{selected_versions[0]}-dkms "
            f"nvidia-{selected_versions[0]}-utils lib32-nvidia-{selected_versions[0]}-utils nvidia-settings"
            )
            self.window.close()
            os.system("clear && figlet Boot && echo 'Loading setup program please wait...' ")
            os.system(self.arr)
            

        elif self.checkBox_5.isChecked():
            selected_versions.append("535xx")
            self.arr = (
            f"yay -S --noconfirm --removemake --answerdiff=None --answerclean=None "
            f"nvidia-{selected_versions[0]}-dkms "
            f"nvidia-{selected_versions[0]}-utils lib32-nvidia-{selected_versions[0]}-utils nvidia-settings"
            )
            self.window.close()
            os.system("clear && figlet Boot && echo 'Loading setup program please wait...' ")
            os.system(self.arr)
            

        QMessageBox.information(None, "เลือกเวอร์ชัน", f"คุณเลือกติดตั้งเวอร์ชัน: {selected_versions[0]}")
                                
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
