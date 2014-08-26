"""
Write a program that asks the user to enter an integer and prints 2 integers,
*ROOT* and *PWR* such that 0 < pwr < 6 and root**pwr is equal  to the integer
entered byu the user. If no such pair of integers exist, it should print a
message to that effect
"""

NUM = int(raw_input('Feed me the numbar --> '))
ROOT = 0
PWR = 0

while ROOT ** PWR < abs(NUM) and PWR < 6:
    PWR = PWR +1
    while ROOT ** PWR < abs(NUM) and ROOT < NUM:
        ROOT = ROOT + 1
if ROOT ** PWR == NUM:
    print ROOT, PWR
else:
    print "I hate these snakes on a plane(no integer set)"
