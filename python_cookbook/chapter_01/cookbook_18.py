

# 1.18 Mapping names to sequence elements

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='jones@example.com', joined='10-12-2020')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# another example | tuple v.s. namedtuple

def compute_cost1(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares*s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75 # immutable attribute `AttributeError`
# use `_replace` method that returns a new namedtuple
s = s._replace(shares=75)
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    '''
        Convert a Dictionary to a Stock
    '''
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
s = dict_to_stock(a)
print(s)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/10/2020'}
s = dict_to_stock(b)
print(s)
