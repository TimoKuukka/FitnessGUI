# HELP DIALOG WINDOW
# ------------------

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets as QW # UI elements functionally
from PyQt5.uic import loadUi # Reads the UI file

# CLASS DEFINITION
class OpenHelp(QW.QDialog):

    # The constructor
    def __init__(self):
        super().__init__()

        loadUi('ohje.ui', self)
        self.setWindowTitle('Kuntoilusovelluksen ohje')
        self.closePB = self.closePushButton
        self.closePB.clicked.connect(self.closeHelp)

    # Methods ie. slots
    def closeHelp(self):
        self.close()