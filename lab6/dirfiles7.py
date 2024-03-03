import os
from string import ascii_uppercase
with open('ginny.txt', 'r') as fil1, open('ginny3.txt', 'a') as fil2:
     for x in fil1:
         fil2.write(x)