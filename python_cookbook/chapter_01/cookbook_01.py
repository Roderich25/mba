

# 1.1 Unpacking a sequence into separte variables

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2020, 12, 8)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(shares)
print(price)
print(year)
print(mon)
print(day)

# unpacking also works for iterable objects
s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

# ignoring certain values
x, _, y, (z, _, _) = data
print(x)
print(y)
print(z)
