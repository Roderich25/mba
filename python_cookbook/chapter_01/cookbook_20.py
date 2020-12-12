

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


# another example
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)


# another example
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merged = dict(b)
print(merged)
merged.update(a)
print(merged)

a['x'] = 123  # dictionary `a` is updated
print(merged['x'])  # but merged one doesn't


# another example
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 123  # ChainMap is updated
print(merged['x'])
