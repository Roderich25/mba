class FMR:

    def __init__(self, lista):
        self.lista = lista

    def filter(self, fun):
        self.lista = list(filter(fun, self.lista))
        return self

    def map(self, fun):
        self.lista = list(map(fun, self.lista))
        return self

    def reduce(self, fun, value=0):
        if not self.lista:
            return value
        else:
            for el in self.lista:
                value = fun(value, el)
                self.lista.remove(el)
                return self.reduce(fun, value)

    def __repr__(self):
        return str(self.lista)


abc = FMR([1, 2, 3, 4])
print(abc.map(lambda x: x*x).reduce(lambda x, y: x+y))
