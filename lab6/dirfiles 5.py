import os
from string import ascii_uppercase
cir = ['A', 'B', 'C', 'D']
with open(r'C:\ginny2.txt', 'w') as fil:
     for x in cir:
         fil.write(x + '\n')
fil.close()
