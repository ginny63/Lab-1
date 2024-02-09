import math
 class Name:
     def __init__(self):
         self.name = ""
        
     def getString(self):
         self.name = input()
        
     def printString(self):
         print(self.name.upper())
        
 word = Name()
 word.getString()
 word.printString()