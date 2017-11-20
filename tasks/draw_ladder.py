"""
At the entrance the program will receive the number of stairs.
The goal is to print the ladder using the space characters " " and the "#" grids.
"""

import sys
stairs_digit = int(sys.argv[1])
whitespace = ' '
grid = '#'
number_of_grid = 1
for stair in range(stairs_digit):
    line = whitespace*(stairs_digit-1) + grid * number_of_grid
    print(''.join(line))
    stairs_digit -= 1
    number_of_grid += 1

