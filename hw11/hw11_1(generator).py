def Fib(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, f1+f2
        yield f1

gen = Fib(100)
for i in gen:
    print(i)
