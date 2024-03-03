import os
from string import ascii_uppercase
mesto1 = r'C:\ '
print([x for x in os.listdir(mesto1)]) 
print([x for x in os.listdir(mesto1) if os.path.isdir(os.path.join(mesto1, x))]) 
print([x for x in os.listdir(mesto1) if not os.path.isdir(os.path.join(mesto1, x))]) 
