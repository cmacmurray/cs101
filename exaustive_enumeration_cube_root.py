"""
Use exhaustive enumeration to print the integers cube root, if the integer is 
not a perfect cube, print the a message to that effect.
"""

X = int(raw_input('enter an integer '))
ans = 0

while ans ** 3 < abs(X):
    ans = ans + 1
if ans ** 3 != abs(X):
    print X, 'is not a perfect cube'
else:
    if X > 0:
        ans = -ans
    print 'Cube root of ', X, 'is', ans

