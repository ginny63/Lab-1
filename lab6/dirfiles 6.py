import os
from string import ascii_uppercase
for i in ascii_uppercase:
     file = open(r'C:\grin\{fchar}.txt'.format(fi = i), 'x')
     file.close()