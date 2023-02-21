###############################################################################
# Word Search (Grid class)
# Liz Denson & Caroline Holland
# Last modified on 2023-02-20
#
# A Grid class for the programming assignment Word Search (part 2).
# Requires Location.py and Word.py.
###############################################################################

# import libraries
from Location import Location
from Word import Word
from random import randint

# the Grid class
# a Grid has a size (the same for both width and height), a grid of letters, and Word instances that are within the Grid
class Grid:
    # class variables
    # the character representing a "blank" letter in the grid
    BLANK = "."
    # the max number of tries to position a word
    MAX_TRIES = 1000
    # the constructor
    def __init__(self, size = 25):
        # set the _size instance variable
        self._size = size
        # initialize the grid
        self._grid = []
        # add the rows
        for row in range(self._size):
            # create a new blank row
            cur_row = []
            # fill it with spaces
            for col in range(self._size):
                cur_row.append(Grid.BLANK)
            # add the new row to grid
            self._grid.append(cur_row)
        # initialize the words
        self._words = []
        
    # getters
    @property 
    def size(self): 
        return self._size
    @property 
    def grid(self): 
        return self._grid
    @property
    def words(self):
        return self._words
    
    # setters
    @size.setter
    def size(self, size):
        if size < 1:
            self._size = 25
        else:
            self._size = size
            
    # tries to position a word at the specified orientation in the grid
    def position(self, word, orientation):
        # set the default min and max row and col
        min_row = 0
        max_row = self._size - 1
        min_col = 0
        max_col = self._size - 1
         # the max_col value (based on the HR, DRD, & DRU orientations)
        if orientation in [ "HR", "DRU", "DRD" ]:
            max_col = self._size - len(word)
        # modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)
        if orientation in [ "HL", "DLU", "DLD" ]:
            min_col = len(word) - 1
        if orientation in [ "VU", "DRU", "DLU" ]:
            min_row = len(word) - 1
        if orientation in [ "VD", "DRD", "DLD" ]:
            max_row = self._size - len(word)
        
        # create the Word instance
        word = Word(word, orientation)
        # select a random location based on the min and max values
        loc = Location(randint(min_row, max_row), randint(min_col, max_col))
        # check if this location works up to the specified maximum number of tries
        tries = 0
        while (not self._check(word, loc)):
            # stop trying if we've reached the specified maximum number of tries
            if (tries == Grid.MAX_TRIES):
                return
            # select a new random location
            loc = Location(randint(min_row, max_row), randint(min_col, max_col))
            # note the attempt
            tries += 1
        # update the word's location
        word.location = loc
        # position the word in the grid at the location
        self._position(word)
        # and add it to the list of words
        self._words.append(word)
        
    # checks if a word can be positioned as specified
    def _check(self, word, loc):
        # the starting row and col for the word
        row = loc.row
        col = loc.col
        # check if the word fits for the specified orientation
        for letter in word.word:
            # abort if we don't encounter a space or the appropriate letter
            if (not self._grid[row][col] in [ Grid.BLANK, letter ]):
                return False
           # the col (based on the HR, DRD, & DRU orientations)
            if word.orientation in [ "HR", "DRD", "DRU" ]:
                col += 1
            # modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)
            if word.orientation in [ "HL", "DLD", "DLU" ]:
                col -= 1
            if word.orientation in [ "VU", "DRU", "DLU" ]:
                row -= 1
            if word.orientation in [ "VD", "DLD", "DRD" ]:
                row += 1
        # otherwise, all the letters fit!
        return True
    
    # positions a word as specified
    def _position(self, word):
        # the starting row and col for the word
        row = word.location.row
        col = word.location.col
        # position the word
        for letter in word.word:
            # place the current letter
            self._grid[row][col] = letter
            # the col (based on the HR, DRD, & DRU orientations)
            if word.orientation in [ "HR", "DRD", "DRU" ]:
                col += 1
            # modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)
            if word.orientation in [ "HL", "DLD", "DLU" ]:
                col -= 1
            if word.orientation in [ "VU", "DRU", "DLU" ]:
                row -= 1
            if word.orientation in [ "VD", "DLD", "DRD" ]:
                row += 1
    
    # prints the words
    def print_words(self):
        # add sorting the words first
        sorted_words = sorted(self._words, key=lambda w: w.word) # Source (sorting/lambda): https://blogboard.io/blog/knowledge/python-sorted-lambda/
        for word in self._words:
            print(word)
    
    # prints the solution
    def print_solution(self):
        print(self.__str__(False))
    
    # return a string representation of the grid
    def __str__(self, fill=True):
        grid = "\n"
        for row in range(self._size):
            for col in range(self._size):
                # if no letter exists at row,col
                if (self._grid[row][col] == Grid.BLANK and fill):
                    # add a random one
                    grid += "{:2}".format(chr(randint(65, 90)))
                else:
                    grid += "{:2}".format(self._grid[row][col])
            grid += "\n"
        # remove the trailing newline
        grid = grid.rstrip("\n")
        return grid