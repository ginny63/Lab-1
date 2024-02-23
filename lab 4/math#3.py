import math
nides=int(input("number of sides:"))
dlina=int(input("length of a side:"))
ar=(nides*dlina**2)/(4*math.tan(math.pi/nides))
print(int(ar))