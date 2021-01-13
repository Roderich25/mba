

# 2.15 Interpolating variables in strings
import string
import sys

s = '{name} has {n} messages'
print(s.format(name='Guido', n=37))

name = 'Pablo'
n = 123
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Rodrigo', 33)
print(s.format_map(vars(a)))

# s.format(name='Guido') # KeyError: 'n'
# format & format_map do not deal with missing values


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


del n  # make sure `n` is undefined
print(s.format_map(safesub(vars())))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# another example
name = 'Rodrigo'
n = 123
print('%(name)s has %(n)s messages.' % vars())

s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
