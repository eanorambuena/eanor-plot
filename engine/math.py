import math

def Constant1(x):
    return 1

def x(y):
    return y

class Function():
    def __init__(self, f):
        self.f = f
        self.name = f.__name__.capitalize()
    def __call__(self, x):
        return self.f(x)
    def __add__(self, other):
        if type(other) in [int, float]:
            return self + Function(Constant1) * other
        def new_f(x):
            return self.f(x) + other.f(x)
        return Function(new_f)
    def __sub__(self, other):
        if type(other) in [int, float]:
            return self - Function(Constant1) * other
        def new_f(x):
            return self.f(x) - other.f(x)
        return Function(new_f)
    def __mul__(self, other):
        if type(other) in [int, float]:
            def ConstantOther(x):
                return other
            return self * Function(ConstantOther)
        def new_f(x):
            return self.f(x) * other.f(x)
        new_function = Function(new_f)
        new_function.name = self.name + " * " + str(other)
        return new_function
    def __pow__(self, other):
        if type(other) in [int, float]:
            def ConstantOther(x):
                return other
            return self ** Function(ConstantOther)
        def new_f(x):
            return self.f(x) ** other.f(x)
        new_function = Function(new_f)
        new_function.name = self.name + " ** " + str(other)
        return new_function
    def __truediv__(self, number):
        def new_f(x):
            return self.f(x) / number
        return Function(new_f)
    def __str__(self):
        return self.name
    def __getitem__(self, other): #compose
        def new_f(x):
            return self.f(other.f(x))
        return Function(new_f)

X = Function(x)
Sin = Function(math.sin)
Cos = Function(math.cos)
Tan = Function(math.tan)
