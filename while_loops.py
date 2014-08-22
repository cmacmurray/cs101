"""
Write a program that asks the user to input 10 integers, and then prents the
largest odd number that was entered, if no odd numbers are entered it should
if none are entered it should indicate as such
"""
counter = 5
odd_numbers = []

while counter != 0:
    num = raw_input('enter an integer ')
    if int(num)%2 != 0:
        odd_numbers.append(num)
    counter = counter -1
    if counter == 0:
        break
if len(odd_numbers) > 0:
    print max(odd_numbers)
else:
    print " no odd numbers"


