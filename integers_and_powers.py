"""
Write a program that asks the user to enter an integer and prints 2 integers,
*root* and *pwr* such that 0 < pwr < 6 and root**pwr is equal  to the integer
entered byu the user. If no such pair of integers exist, it should print a 
message to that effect
"""

#Take an integer from the user

num = int(raw_input('please input an integer '))
root = 0
pwr = 0

while root ** pwr != abs(num):
    root = root +1
    while root ** pwr != abs(num):
        pwr = pwr +1
        if pwr == 6 or root ** pwr == num:
            break

if root ** pwr != num:
    print 'No such integer pair exist'
