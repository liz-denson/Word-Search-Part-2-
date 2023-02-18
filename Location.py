###############################################################################
# Word Search (Location class)
# Liz Denson & Caroline Holland
# Last modified on 2023-02-06
#
# A Location class for the programming assignment Word Search.
###############################################################################

# Location class
class Location:
    
    # The constructor which takes a row and col as parameters
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        
    # Getters and setters for the instance variables _row and _col
    @property
    def row(self): 
        return self._row
    @row.setter
    def row(self, row):
        if row < 0:
            self._row = 0
        else:
            self._row = row
    @property
    def col(self):
        return self._col
    @col.setter
    def col(self, col):
        if col < 0:
            self._col = 0
        else:
            self._col = col

    # A __str__() method that returns a string representation of the Location in the format (row,col)
    def __str__(self):
        return ("({},{})".format(self.row, self.col))

