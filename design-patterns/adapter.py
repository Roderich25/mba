from random import randint
from calculator import GeneratorAdapter, FileAverageCalculator
g = (randint(0, 100) for i in range(1_000_000))

fac = FileAverageCalculator(GeneratorAdapter(g))
print(fac.average())
