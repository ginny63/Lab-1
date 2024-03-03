inp = input()
sumup = 0
sumlow= 0
for i in inp:
     if i.isupper():
         sumup += 1
     elif i.islower():
         sumlow += 1
print("Uppercase letters: ",sumup)
print("Lowercase letters: ",sumlow)