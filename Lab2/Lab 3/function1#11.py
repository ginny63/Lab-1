 def isPalin():
     word = input()
     if word == word[::-1]:
         return True
     else:
         return False

 print(isPalin())