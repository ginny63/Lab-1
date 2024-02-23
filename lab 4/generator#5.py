def decr(n):
    while n>=0:
        yield n
        n-=1
for i in decr(7):
 print(i)