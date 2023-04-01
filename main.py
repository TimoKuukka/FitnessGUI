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
        self.wighingDE = self.wighingDateEdit
        self.wighingDE.setDate(self.currentDate)

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
        dateOfWeighing = self.wighingDE.date().toString(format=QtCore.Qt.ISODate)

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
    app.setStyle('Fusion')
    appWindow.show()
    sys.exit(app.exec())

