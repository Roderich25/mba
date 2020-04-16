#!/usr/bin/env python3
from array import array
from functools import reduce
from operator import xor
import math
import numbers
import reprlib


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return f"Vector({components})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True
        # return len(self)==len(other) and all(a==b for a,b in zip(self,other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return reduce(xor, hashes, 0)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError(f"{cls.__name__} indices must be integers")

    shortcut_names = "xyzt"

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = f"{cls.__name__} object has no attribute {name}"
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = f"readonly attribute {name}"
            elif name.islower():
                error = f"can't set attributes 'a' to 'z' in {cls.__name__}"
            else:
                error = ""
            if error:
                raise AttributeError(error)
        super().__setattr__(name, value)

    def __format__(self, fmt=""):
        comp = (str(format(c, fmt)) for c in self)
        return f"({', '.join(comp)} )"

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


v = Vector(range(0, 10))

print(str(v))
print(repr(v))

print(len(v))
print(repr(v[1:4]))
print(v[1])
print(type(v[-1:]))

print(v.x, v.y, v.z)

print(format(v, "5.2f"))
