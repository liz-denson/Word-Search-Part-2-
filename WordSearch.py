###############################################################################
# Word Search
# Caroline Holland & Liz Denson
# Last modified on 2023-02-18
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
NUM_WORDS = 5               # how many words to randomly select
GRID_SIZE = 10              # the height/width of the grid
DISPLAY_SOLUTION = True     # display the solution?

######
# MAIN
######
# read the words from stdin
    # remove the trailing newline and convert to uppercase

# manually open the input file
with open ("animals.txt", "r") as f:
    # read the words from the input file
    lines = f.read().splitlines()

# remove the trailing newline and convert to uppercase
words = [line.strip().upper() for line in lines]

# grab a sampling of the specified number of words
selected_words = sample(words, NUM_WORDS)

# initialize the grid
grid = Grid(GRID_SIZE)

# process the words
count = 0
for word in selected_words:
    # randomly select an orientation for the current word
    orientation = choice(Word.ORIENTATIONS)
    # position the current word at the chosen orientation in the grid
    grid.position(word, orientation)
    
    count += 1

# display stats (i.e., "Successfully placed X of Y words.")
print("Successfully placed {} of {} words.\n".format(count, NUM_WORDS))

# display the grid
print(grid, "\n")

# display the words
grid.print_words()

# if specified, display the solution
if DISPLAY_SOLUTION:
    grid.print_solution()

