import os
from string import ascii_uppercase
with open(r'C:\ginny.txt', 'r') as file:
     a = len(file.readlines())
     print("Number of lines:", a)