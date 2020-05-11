import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """
            Add items from an iterable
        """

    @abc.abstractmethod
    def pick(self):
        """
            Remove item at random, returning it
            Should raise `LookupError` when the instance is empty
        """

    def loaded(self):
        """
            Return `True` if there's at leat 1 item left, `False` otherwise.
        """
        return bool(self.inspect())

    def inspect(self):
        """
            Return a sorted tuple with the items currently inside.
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from empty BingoCage")
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


b = BingoCage([1, 2, 3])
l = LotteryBlower([1, 2, 3])
t = TomboList([1, 2, 3])

for i in range(3):
    print("\n#", i, sep="")
    for o in [b, l, t]:
        print(type(o).__name__, o.pick(), sep="\t")

print("\nTombolist MRO:\t", TomboList.__mro__)
print(Tombola.__subclasses__())
print(abc._get_dump(Tombola))
