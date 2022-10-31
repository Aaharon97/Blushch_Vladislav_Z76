class Fib:
    def __iter__(self):
        return self

    def __init__(self, n: int, f1 = 0, f2 = 1):
        self.n = n
        self.f1 = 0
        self.f2 = 1

    def __next__(self):
        for i in range(self.n):
            self.f1, self.f2 = self.f2, self.f1 + self.f2
            return self.f1

#TODO почему оно не ограничивается количеством элементов которе я ввел?
iterator = iter(Fib(10))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))