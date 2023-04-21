# ROUTINES TO CREATE, WRITE AND READ ATHLETE DATA FILE
# ----------------------------------------------------

# LIBRARIES AND MODULES
# ---------------------
import json

# CLASS DEFINITIONS

class ProcessJsonFile():
    def __init__(self):
        # super.__init__ <- ei tarvita kun ei peritä mitään toisesta luokasta
        pass

    

    def saveData(self, file, data):
        """Saves all athlete data to disk

        Args:
            file (str): Name of the file
            data (dict): List of dictionaries

        Returns:
            tuple: Error code, Error message, detailed error message
        """

        with open(file, 'w') as fileToWrite:
            json.dump(data, fileToWrite, indent=4)
        status = (0, 'Tallennus onnistui', 'All data saved successfully')
        return status

    def readData(self, file):
        """Read athlete data from file

        Args:
            file (str): Name of the file

        Returns:
            tuple: Error code, Error message, detailed error message,  data
        """

        # Read previous athlete_data from disk
        with open(file, 'r') as fileToRead:
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage  = 'Data read successfully from disk'
            data = (0, message, detailedMessage, athlete_data)
        return data

    def appendData(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): Name of the file
            data (_type_): Python dictionary containing data

        Returns:
            tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistui', 'Data saved successfully')
        return status


# PRELIMINARY TEST

if __name__ == "__main__":
    pass