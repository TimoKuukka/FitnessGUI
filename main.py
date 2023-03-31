# MAIN WINDOW FOR FTINESS APPLICATION
# ------------------------------------

# LIBRARIES AND MODULES
# ---------------------
# Import the PyQt5 modules
import sys 
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi
from datetime import date
import kuntoilija

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    """MainWindow for the fitness app"""

    # Constructor fo the main window
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls in buttons and input fields
        self.calcPB = self.calcPushButton
        self.calcPB.clicked.connect(self.calculateAll)

        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

        # Measurement data
        self.nameLE = self.nameLineEdit
        self.genderCB = self.genderComboBox
        self.ageSB = self.ageSpinBox
        self.heightSB = self.heightSpinBox
        self.weightSB = self.weightSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.hipsSB = self.hipsSpinBox


        # Set current date when the app starts
        self.currentDate = date.today()
        self.wighingDE = self.wighingDateEdit
        self.wighingDE.setDate(self.currentDate)




    # Define slots in methods

    # Calculates BMI, finnish and US fat percentages and updates corrensponding labels
    def calculateAll(self):
        height = self.heightSB.value() 
        weight = self.weightSB.value()
        age = self.ageSB.value()
        gender = self.genderCB.value()
        dateOfWeighing = self.wighingDE()

        # Create an athlete from Kuntoilija class
        athlete = kuntoilija.Kuntoilija()
        bmi = athlete.bmi

        neck = self.neckSB.value()
        waist = self.waistSB.value()
        hips = self.hipsSB.value()

        self.bmiLabel.setText('100')

    # Saves the data to a disk
    def saveData(self):
        pass


if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window
    #  (and show it)
    appWindow = MainWindow()
    app.setStyle('Fusion')
    appWindow.show()
    sys.exit(app.exec())

