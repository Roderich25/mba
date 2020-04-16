#!/usr/bin/env python3
class Vector:
    __slots__ = ("__x", "__y")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        # self.__z = x + y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        cname = type(self).__name__
        return "{}({!r}, {!r})".format(cname, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __format__(self, fmt=""):
        comp = (format(c, fmt) for c in self)
        return "({},{})".format(*comp)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v = Vector(3.1, 4.2)

print(repr(v))
print(str(v))
print(format(v, "5.2f"))

print(hash(v))
print(hash(Vector(4.2, 3.1)))

print(v == Vector(3.1, 4.2))
print(v == Vector(4.2, 3.1))

print(set([v]))

# v._Vector__x = 3
# print(v.__dict__)
print(v._Vector__x)

x, y = v
print((x, y))
