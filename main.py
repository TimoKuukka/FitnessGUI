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
import ohje
import BGPictures # Compiled resources for background images


# FIXME: DONT WORK BECAUSE DIMENSIONFRAME ! !
# TODO: Make another resource file for the help window, build and import it
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

        # TODO: Change spin boxes to sliders
        # Measurement data
        self.heightVS = self.verticalSliderHeight
        self.heightVS.valueChanged.connect(self.activateCalculatePB)
        self.weightDial = self.weightDial
        self.weightDial.valueChanged.connect(self.activateCalculatePB)
        self.neckHS = self.horizontalSliderNeck
        self.neckHS.valueChanged.connect(self.activateCalculatePB)
        self.waistHS = self.horizontalSliderWaist
        self.waistHS.valueChanged.connect(self.activateCalculatePB)
        self.hipsHS = self.horizontalSliderHips
        self.hipsHS.setEnabled(False)
        self.hipsHS.valueChanged.connect(self.activateCalculatePB)

        # Background image for body dimensions is a QFrame with a background image by default a woman
        self.dimensionBox = self.dimensionFrame

        # Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.show()

    
        # self.calculatePB = self.calculatePushButton
        self.calcPB = self.findChild(QW.QPushButton, 'calcPushButton')
        self.calcPB.clicked.connect(self.calculateAll)
        self.calcPB.setEnabled(False)

        # Temporary push button for inserting test values into controls
        self.testPB = self.testUiPushButton
        self.testPB.clicked.connect(self.insertTestValues)

        # A push button to for saving user data
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
        
        # MENU ACTIONS
        self.actionPalauta_oletukset.triggered.connect(self.restoreDefaults)
        self.actionOhje.triggered.connect(self.openHelpDialog)
        
    # Define slots in methods

    # Create a alerting method
    def alert(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Critical)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    # Create a warning method
    def warn(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Warning)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    # Create a inform method
    def inform(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Information)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def showMessageBox(self, windowTitle, message, detailedMessage, icon='Information'):
        """Creates a message box for various types of messages

        Args:
            windowTitle (str): Header for the message windowsS
            message (str): Message to be shown
            detailedMessage (str): A message that can be shoen by pressing details button
            icon (str, optional): Allowed values: NoIcon, Information, Question, Warning and Critical
            Defaults to Information.
        """
        iconTypes = {'Information': QW.QMessageBox.Information, 'NoIcon': QW.QMessageBox.NoIcon,
         'Question': QW.QMessageBox.Question, 'Warning': QW.QMessageBox.Warning,
         'Critical': QW.QMessageBox.Critical}
        msgBox = QW.QMessageBox()
        msgBox.setIcon(iconTypes[icon])
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
        
        if self.heightVS.value() == 100:
            self.calcPB.setEnabled(False)

        if self.weightDial.value() == 20:
            self.calcPB.setEnabled(False)

        if self.neckHS.value() == 10:
            self.calcPB.setEnabled(False)

        if self.waistHS.value() == 30:
            self.calcPB.setEnabled(False)

        if self.genderCB.currentText() == 'Nainen' or self.genderCB.currentText() == '':
            self.hipsHS.show()
            self.dimensionBox.setStyleSheet("background-image : url(:/pictures/NaisSlice.png)") # Change the bg image

            if self.hipsHS.value() == 50:  
                self.calcPB.setEnabled(False)
        else:
            self.hipsHS.hide() # Hide Hips spinbox
            self.dimensionBox.setStyleSheet("background-image : url(:/pictures/MiesSlice.png)") # Change the bg image


            
    def insertTestValues(self):
        # Set test values to all controls
        self.nameLE.setText('Erkki Esimerkki')
        testBirhtday = QtCore.QDate(1987, 12, 31)
        self.birthDE.setDate(testBirhtday)
        self.genderCB.setCurrentText('Mies')
        self.heightVS.setValue(179)
        self.weightDial.setValue(105)
        self.neckHS.setValue(30)
        self.waistHS.setValue(105)

    
    # Calculates BMI, finnish and US fat percentages and updates corrensponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightVS.value() # Spinbox value as an integer 
        weight = self.weightDial.value()

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

        neck = self.neckHS.value()
        if neck < 21:
            #self.alert('Tarkista kaulan koko', 'kaulan ympärys liian pieni', 'Kaulan ympäryksen tulee olla vähintään 20 cm')
            self.showMessageBox('Tarkista kaulan koko', 'Kaulan ympärys virheellinen', 'Sallitut arvot 21 - 60 cm', 'Warning')
        waist = self.waistHS.value()
        hips = self.hipsHS.value()

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
            self.restoreDefaults()

    def restoreDefaults(self):
        self.nameLE.clear()
        zeroDate = QtCore.QDate(1900, 1, 1)
        self.birthDE.setDate(zeroDate)
        self.heightVS.setValue(100)
        self.weightDial.setValue(20)
        self.neckHS.setValue(10)
        self.waistHS.setValue(30)
        self.hipsHS.setValue(50)
        # Hides save push button after clicked
        self.savePB.setEnabled(False)

    def openHelpDialog(self):
        openHelp = ohje.OpenHelp()
        openHelp.exec()


if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion') # Use Fusion style

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    


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

