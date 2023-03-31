# MAIN WINDOW FOR FTINESS APPLICATION
# ------------------------------------

# LIBRARIES AND MODULES
# ---------------------
# Import the PyQt5 modules
import sys 
from PyQt6 import QtCore # Core functionality of Qt
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi

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

# Define slots in methods
    def calculateAll(self):
        self.bmiLabel.setText('100')


if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window
    #  (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

