

# 1.11 Naming a slice

record = '                    100                 513.23     '

# without naming the slices
print(int(record[20:32]))
print(float(record[40:48]))

cost = int(record[20:32]) * float(record[40:48])
print(cost)

# naming the slices
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES])*float(record[PRICE])
print(cost)

# another example
items = [0, 1, 2, 3, 4, 5, 6]

a = slice(2, 4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
print(items)

# slice attributes
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# another example |
s = 'HelloWorld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])
