

# Combining multiple mappings into a single mapping
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

# operations tha mutate mappings always affect the first mapping
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y'] # KeyError: "Key not found in the first mapping: 'y'"
