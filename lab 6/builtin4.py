import time
n=int(input())
ms=int(input())
s=ms/1000
time.sleep(s)
sq=n**0.5
inp='Square root of{fn} after{fs} is (fsq)'.format(fn=n,fs=ms,fsq=sq)
print(inp)
