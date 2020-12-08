

# 1.2 Unpacking elements from iterables of arbitrary length

def avg(grades):
    return sum(grades)/len(grades)


def drop_first_last(grades):
    '''
        Remove first and last element
        and return the average of the rest
    '''
    first, *middle, last = grades
    return avg(middle)


print(drop_first_last([5, 6, 7, 8, 9, 10]))


# another example
record = ('David', 'david@example.com', '55-66-77-88-99', '99-88-77-66-55')
name, email, *phones = record
print(name)
print(email)
print(phones)  # return a list

# another example
sales_record = [123, 234, 345, 456, 567, 678, 890, 901]
*trailing_qtrs,  current_qtr = sales_record
print(trailing_qtrs)
print(current_qtr)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# another example
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# another example
line = 'nobody:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# another example
record = ['ACME', 50, 123.45, (8, 12, 2020)]
name, *_, (*_, year) = record
print(name)
print(year)

# another example
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


def sum_items(items):
    head, *tail = items
    return head + sum_items(tail) if tail else head  # recursion


print(sum_items(items))
print(sum_items([100]))
