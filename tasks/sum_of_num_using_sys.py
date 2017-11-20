"""
The file should be run with a command-line argument - a string, consisting of numbers.
The sys.argv list will contain the command-line arguments:
- sys.argv [0] is the name of the running file,
- sys.argv [1] is a string consisting of numbers.
Task: calculate sum of numbers in string
"""

import sys

digit_str = sys.argv[1]
digit_sum = 0
if not digit_str.isdigit():
    print('В строке должны быть только числа')
else:
    for num in digit_str:
        digit_sum += int(num)
    print(digit_sum)

