class FMR:

    def __init__(self, lista):
        self.lista = lista

    def filter(self, fun):
        self.lista = list(filter(fun, self.lista))
        return self

    def map(self, fun):
        self.lista = list(map(fun, self.lista))
        return self

    def reduce(self, fun, start=None):
        pass

    def __repr__(self):
        return str(self.lista)


abc = FMR([1, 2, 3, 4])
print(abc.map(lambda x: x*x).map(lambda x: x*x))
