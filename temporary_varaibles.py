temp = 0 

X = 9
Y = 2
Z = 4

if X%2 != 0 and X > temp:
    temp = X
elif Y%2 != 0 and Y > temp:
    temp = Y
elif Z%2 != 0 and Z > temp:
    temp = Z

if temp > 0:
    print temp
else:
    print "shit is fucked"
