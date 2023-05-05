# MAIN WINDOW FOR FTINESS APPLICATION
# ------------------------------------

# LIBRARIES AND MODULES
# ---------------------
# Import the PyQt5 modules
import sys 
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as QW # UI elements functionality
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.uic import loadUi
from datetime import date
import kuntoilija
import timetools
import athleteFile # Home made module for processing data files


# TODO: Import some library able to plot trends and make it as widget in the UI

# Class for the main window
class MainWindow(QW.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor fo the main window
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)
    
        self.birthDE = self.birthDateEdit
        self.birthDE.dateChanged.connect(self.activateCalculatePB)
        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)

        # Set current date when the app starts
        self.currentDate = date.today()
        self.weighingDE = self.weighingDateEdit
        self.weighingDE.setDate(self.currentDate)

        # Measurement data
        self.heightSB = self.heightSpinBox
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.weightSpinBox
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB = self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipsSB = self.hipsSpinBox
        self.hipsSB.setEnabled(False)
        self.hipsSB.valueChanged.connect(self.activateCalculatePB)

        # Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.show()

    
        # self.calculatePB = self.calculatePushButton
        self.calcPB = self.findChild(QW.QPushButton, 'calcPushButton')
        self.calcPB.clicked.connect(self.calculateAll)
        self.calcPB.setEnabled(False)

        # self.savePB = self.savePushButton
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)
        
        # Read data from file and save it to a list
        self.dataList = []
        jsonFile = athleteFile.ProcessJsonFile()
        try:
            data = jsonFile.readData('athleteData.json')
            self.dataList = data[3]
        except Exception as e:
            data = (0, 'Error', str(e), self.dataList)
            
        

        # Read previous athlete_data from disk


    # Define slots in methods

    # Create a alerting method
    def alert(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Critical)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()
    
    def activateCalculatePB(self):
        self.calcPB.setEnabled(True)
        if self.nameLE.text() == '':
            self.calcPB.setEnabled(False)

        if self.birthDE.date() == QtCore.QDate(1900, 1, 1):
            self.calcPB.setEnabled(False)

        if self.genderCB.currentText() == '':
            self.calcPB.setEnabled(False)
        
        if self.heightSB.value() == 100:
            self.calcPB.setEnabled(False)

        if self.weightSB.value() == 20:
            self.calcPB.setEnabled(False)

        if self.neckSB.value() == 10:
            self.calcPB.setEnabled(False)

        if self.waistSB.value() == 30:
            self.calcPB.setEnabled(False)

        if self.genderCB.currentText() == 'Nainen':
            self.hipsSB.setEnabled(True)

            if self.hipsSB.value() == 50:  
                self.calcPB.setEnabled(False)
        else:
            self.hipsSB.setEnabled(False)


            
    
    
    # Calculates BMI, finnish and US fat percentages and updates corrensponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value() # Spinbox value as an integer 
        weight = self.weightSB.value()

        self.calcPB.setEnabled(False)
        self.savePB.setEnabled(True)
        
        # Convert birthday to ISO string using QtCore methods
        birthday = self.birthDE.date().toString(format=QtCore.Qt.ISODate)

        # Set Gender Value according to Combobox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1
        else:
            gender = 0

        # Convert Weighing data to ISO string
        dateOfWeighing = self.weighingDE.date().toString(format=QtCore.Qt.ISODate)

        # Calculate time difference using our home made tools
        age = timetools.datediff2(birthday, dateOfWeighing, 'year')

        neck = self.neckSB.value()
        if neck < 20:
            self.alert('Virheellinen kaulan ympärys', 'Kaulan ympäryksen tulee olla vähintään 20 cm')
        waist = self.waistSB.value()
        hips = self.hipsSB.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, neck, waist, hips, dateOfWeighing)
            
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))

        fiFatPercentage = athlete.fi_rasva
        usFatPercentage = athlete.usa_rasva
        
        # Set fat percentage labels
        self.fatFiLabel.setText(str(fiFatPercentage))
        self.fatUsLabel.setText(str(usFatPercentage))

        self.dataRow = self.constructData(athlete)
        print(self.dataRow)

    def constructData(self, athlete):
        # A dictionary for single weighing of an athlete
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino,
                'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva, 
                'bmi': athlete.bmi, 'rasvaprosenttiFi': athlete.fi_rasva, 'rasvaprosenttiUs': athlete.usa_rasva}
        return athlete_data_row        

    # Saves the data to a disk
    def saveData(self):

        # Add current values to a list
        self.dataList.append(self.dataRow)

        # Save the list to a json file
        jsonfile2 = athleteFile.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)

        # Show status message on status bar
        self.statusBar.showMessage(status[1], 4000)

        # TODO: Call error message box if error code is 0
        if status[0] != 0:
            self.alert(status[1], status[2])
        else:
            # Set all inputs to default values
            self.nameLE.clear()
            zeroDate = QtCore.QDate(1900, 1, 1)
            self.birthDE.setDate(zeroDate)
            self.heightSB.setValue(100)
            self.weightSB.setValue(20)
            self.neckSB.setValue(10)
            self.waistSB.setValue(30)
            self.hipsSB.setValue(50)
            # Piilottaa tallenna näppäimen operaation suorittamisen jälkeen
            self.savePB.setEnabled(False)



if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion') # Use Fusion style

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    
    # # Create dark style to all

    # # Define the palette to dark
    # dark_palette = QPalette()
    # dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.WindowText, Qt.white)
    # dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    # dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    # dark_palette.setColor(QPalette.Text, Qt.white)
    # dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.ButtonText, Qt.white)
    # dark_palette.setColor(QPalette.BrightText, Qt.red)
    # dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    # # Apply the palette
    # app.setPalette(dark_palette)
    # # Apply the dark stylesheet
    # app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    # Show the window
    appWindow.show()
    sys.exit(app.exec())

