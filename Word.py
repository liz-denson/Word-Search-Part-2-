###############################################################################
# Word Search (Word class)
# Liz Denson & Caroline Holland
# Last modified on 2023-02-06
#
# A Word class for the programming assignment Word Search.
# Requires Debug.py.
###############################################################################

# Import Debug.py library to appropriately utilize the DEBUG variable
from Debug import DEBUG

# Word class
class Word:
    
    # Orientations stored in a list through a class variable called ORIENTATIONS
    ORIENTATIONS = ["HR", "HL", "VD", "VU", "DRD", "DRU", "DLD", "DLU"]
    
    # The constructor which takes a word, an orientation, and a location as parameters
    def __init__(self, word, orientation=None, location=None):
        self.word = word.upper()
        self.orientation = orientation
        self.location = location

    # Getters and setters for the instance variables _word, _orientation, and _location
    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, word):
        self._word = word.upper()
    @property
    def orientation(self):
        return self._orientation
    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        self._location = location
    
    # A __str__() method that returns a string representation of the Word in two formats
    def __str__(self):
        if DEBUG == False:
            return self.word.upper()
        else:
            return "{}/{}@{}".format(self.word, self.orientation, self.location)
