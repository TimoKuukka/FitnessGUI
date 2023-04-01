# MAIN WINDOW FOR FTINESS APPLICATION
# ------------------------------------

# LIBRARIES AND MODULES
# ---------------------
# Import the PyQt5 modules
import sys 
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.uic import loadUi
from datetime import date
import kuntoilija
import timetools


# TODO: Import some library able to plot trends and make it as widget in the UI
# TODO: REMOVE EVERYTHING 'ageSpinBox'
# TODO: ADD birthDateE = self.birthDateEdit

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor fo the main window
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.nameLineEdit
        self.birthDE = self.birthDateEdit
        self.genderCB = self.genderComboBox

        # Set current date when the app starts
        # TODO: FIX date format to shorter code
        self.currentDate = date.today()
        self.weighingDE = self.weighingDateEdit
        self.weighingDE.setDate(self.currentDate)

        # Measurement data
        self.heightSB = self.heightSpinBox
        self.weightSB = self.weightSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.hipsSB = self.hipsSpinBox

        # TODO: Disable Calculate button until values have been edited
        self.calcPB = self.calcPushButton
        self.calcPB.clicked.connect(self.calculateAll)

        # TODO: Disable Calculate button until values have been edited
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)



    # Define slots in methods

    # Calculates BMI, finnish and US fat percentages and updates corrensponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value() # Spinbox value as an integer 
        weight = self.weightSB.value()
        
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

        # Create an athlete from Kuntoilija class
        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, dateOfWeighing)
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))

    # TODO: Make this method to save results to a disk drive
    # Saves the data to a disk
    def saveData(self):
        pass


if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    
    # Create dark style to all
    # Force the style to be the same on all OSs:
    app.setStyle('Fusion')
    # Define the palette to dark
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    # Apply the palette
    app.setPalette(dark_palette)
    # Apply the dark stylesheet
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    # Show the window
    appWindow.show()
    sys.exit(app.exec())

