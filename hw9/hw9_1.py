class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    @property
    def lens(self):
        return self._a, self._b, self._c

    def CheckTriangle(self):
        if (self._a + self._b > self._c) and (self._a + self._c > self._b) and (self._b + self._c > self._a):
            print("Correct triangle")
        else:
            print("There is no such triangle")

figure = Triangle(3, 4, 5)
figure.CheckTriangle()
print(figure.lens)
figure = Triangle(3, 4, 1)
figure.CheckTriangle()
print(figure.lens)
