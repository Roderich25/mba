from calculator import FileAverageCalculator
from calculator import MemoryAverageCalculator

fac = FileAverageCalculator(open('data.txt'))
print(fac.average())

mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(mac.average())
