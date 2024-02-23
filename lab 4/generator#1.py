def sqgn(N):
    for i in range(1,N+1):
        yield i*i
for sq in sqgn(6):
    print(sq)