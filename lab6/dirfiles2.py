import os
from string import ascii_uppercase
print('path exists:', os.access(r'C:\ ', os.F_OK))
print('path readable:', os.access(r'C:\ ', os.R_OK))
print('path writable:', os.access(r'C:\ ', os.W_OK))
print('path executable:', os.access(r'C:\ ', os.X_OK))
