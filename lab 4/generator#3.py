def gen(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
for x in gen(100):
    print(x)

    

