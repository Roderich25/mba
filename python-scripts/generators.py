from inspect import getgeneratorstate


def save_in_list():
    numbers = []
    while True:
        number = yield
        if number is None:
            print("Finalizar")
            break
        numbers.append(number)
    return numbers


g = save_in_list()


print(getgeneratorstate(g))
#  Priming coroutine
next(g)
print(getgeneratorstate(g))
g.send(1000)
g.send(2222)
g.send(1902)

try:
    g.send(None)
except StopIteration as e:
    error = e.value

print(error)
print(getgeneratorstate(g))
