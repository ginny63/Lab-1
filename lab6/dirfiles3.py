import os
from string import ascii_uppercase
inp = input('Input: \n')
inpb = os.access(inp, os.F_OK)
if inpb == False:
     print("Path does not exist")
elif inpb == True:
     print("Directories:", ', '.join([x for x in os.listdir(inp) if os.path.isdir(os.path.join(inp, x))]))
     print("Files:", ', '.join([x for x in os.listdir(inp) if not os.path.isdir(os.path.join(inp, x))]))
    