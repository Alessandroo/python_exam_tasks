class LinearFuncton(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, x):
        return self.a * x + self.b

    def __add__(self, f2):
        return LinearFuncton(self.a + f2.a, self.b + f2.b)

    def __mul__(self, c):
        if isinstance(c, (int, float)):
            return LinearFuncton(self.a * c, self.b * c)

    def __pow__(self, f2):
        if not isinstance(f2, LinearFuncton):
            raise TypeError()
        return LinearFuncton(self.a * f2.a, self.a * f2.b + self.b)

    def __str__(self):
        return '{}x + {}'.format(self.a, self.b)
