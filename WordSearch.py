###############################################################################
# Word Search
# Liz Denson & Caroline Holland
# Last modified on 2023-02-20
#
# The main program for the programming assignment Word Search (part 2).
# Requires Word.py and Grid.py.
###############################################################################

# import libraries
from Word import Word
from Grid import Grid
from sys import stdin
from random import sample, choice

# define constants
NUM_WORDS = 15              # how many words to randomly select
GRID_SIZE = 25              # the height/width of the grid
DISPLAY_SOLUTION = True     # display the solution?

######
# MAIN
######
    
# manually open the input file
with open ("animals.txt", "r") as f:
    # read the words from the input file,convert to uppercase, and remove the trailing newline  
    words = f.read().upper().splitlines()

# grab a sampling of the specified number of words
words = sample(words, NUM_WORDS)

# initialize the grid
grid = Grid(GRID_SIZE)

# process the words
for word in words:
    # randomly select an orientation for the current word from ORIENTATIONS list in Word.py
    orientation = choice(Word.ORIENTATIONS)
    # position the current word at the chosen orientation in the grid
    grid.position(word, orientation)

# display stats (i.e., "Successfully placed X of Y words.")
print("Successfully placed {} of {} words.\n".format(len(grid._words), len(words)))
# display the grid
print(grid, "\n")

# display the words
grid.print_words()

# if specified, display the solution
if DISPLAY_SOLUTION:
    grid.print_solution()