"""
On the entrance the program will receive coefficients a, b and c - your goal is to
print 2 roots of the quadratic equation (each with a new line).
The roots must be reduced to an integer form before being displayed.
All of coefficients will be the coefficients that eventually yield 2 integer
roots of the quadratic equation.
"""

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b**2-4*a*c
x1 = 0
x2 = 0
if d > 0:
    x1 = int((-b + (b**2 - 4*a*c)**0.5)/2 * a)
    x2 = int((-b - (b**2 - 4*a*c)**0.5)/2 * a)
elif d == 0:
    x1 = x2 = int(-b/2*a)
else:
    pass

print('x1: ', x1)
print('x2: ', x2)
