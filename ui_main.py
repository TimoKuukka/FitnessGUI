# Form implementation generated from reading ui file 'c:\Users\TimoK\Documents\GitHub\FitnessGUI\main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 10, 49, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.wighingDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.wighingDateEdit.setGeometry(QtCore.QRect(10, 80, 110, 22))
        self.wighingDateEdit.setObjectName("wighingDateEdit")
        self.genderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.genderComboBox.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.heightSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(10, 130, 71, 22))
        self.heightSpinBox.setMaximum(250)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.weightSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.weightSpinBox.setGeometry(QtCore.QRect(90, 130, 71, 22))
        self.weightSpinBox.setMaximum(250)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.heightLabel.setObjectName("heightLabel")
        self.weightLabel = QtWidgets.QLabel(self.centralwidget)
        self.weightLabel.setGeometry(QtCore.QRect(90, 110, 61, 16))
        self.weightLabel.setObjectName("weightLabel")
        self.neckSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(170, 130, 71, 22))
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(250, 130, 71, 22))
        self.waistSpinBox.setMaximum(200)
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.waistLabel = QtWidgets.QLabel(self.centralwidget)
        self.waistLabel.setGeometry(QtCore.QRect(250, 110, 71, 16))
        self.waistLabel.setObjectName("waistLabel")
        self.neckLabel = QtWidgets.QLabel(self.centralwidget)
        self.neckLabel.setGeometry(QtCore.QRect(170, 110, 61, 16))
        self.neckLabel.setObjectName("neckLabel")
        self.calcPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcPushButton.setGeometry(QtCore.QRect(10, 170, 75, 24))
        self.calcPushButton.setObjectName("calcPushButton")
        self.savePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(100, 170, 75, 24))
        self.savePushButton.setObjectName("savePushButton")
        self.hipsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hipsSpinBox.setGeometry(QtCore.QRect(330, 130, 71, 22))
        self.hipsSpinBox.setMaximum(200)
        self.hipsSpinBox.setObjectName("hipsSpinBox")
        self.hipsLabel = QtWidgets.QLabel(self.centralwidget)
        self.hipsLabel.setGeometry(QtCore.QRect(330, 110, 71, 16))
        self.hipsLabel.setObjectName("hipsLabel")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(150, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 270, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.bmiLabel = QtWidgets.QLabel(self.centralwidget)
        self.bmiLabel.setGeometry(QtCore.QRect(10, 240, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bmiLabel.setFont(font)
        self.bmiLabel.setObjectName("bmiLabel")
        self.fatFiLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(10, 290, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(150, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 61, 16))
        self.label.setObjectName("label")
        self.ageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel.setGeometry(QtCore.QRect(230, 10, 49, 16))
        self.ageLabel.setObjectName("ageLabel")
        self.ageSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ageSpinBox.setGeometry(QtCore.QRect(230, 30, 42, 22))
        self.ageSpinBox.setObjectName("ageSpinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Syötä nimesi</span></p></body></html>"))
        self.nameLabel.setText(_translate("MainWindow", "Nimi"))
        self.genderComboBox.setItemText(0, _translate("MainWindow", "Valitse sukupuoli"))
        self.dateLabel.setText(_translate("MainWindow", "Mittauspäivä"))
        self.heightLabel.setText(_translate("MainWindow", "Pituus (cm)"))
        self.weightLabel.setText(_translate("MainWindow", "Paino (kg)"))
        self.waistLabel.setText(_translate("MainWindow", "Vyötärö (cm)"))
        self.neckLabel.setText(_translate("MainWindow", "Kaula (cm)"))
        self.calcPushButton.setText(_translate("MainWindow", "Laske"))
        self.savePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.hipsLabel.setText(_translate("MainWindow", "Lantio (cm)"))
        self.label_11.setText(_translate("MainWindow", "Painoindeksi"))
        self.label_12.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label_13.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.bmiLabel.setText(_translate("MainWindow", "Painoindeksi"))
        self.fatFiLabel.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.label_16.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label.setText(_translate("MainWindow", "Sukupuoli"))
        self.ageLabel.setText(_translate("MainWindow", "Ikä"))
