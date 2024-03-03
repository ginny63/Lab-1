import os
from string import ascii_uppercase
inp = r'C:\yinn.txt'
inpb = os.access(inp, os.F_OK)
if inpb == False:
     print('Path does not exist')
elif inpb == True:
    os.remove(inp)
    print("File has been removed")