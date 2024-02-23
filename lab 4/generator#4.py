def squares(a,b):
 for i in range(a,b+1):
  yield i*i
for x in squares(1,7):
 print(x)  
