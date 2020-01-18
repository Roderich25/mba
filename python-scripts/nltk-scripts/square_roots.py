#!/usr/bin/env python3


def square_root(a):
    x = a//2
    while True:
        print(int(x)*"*", x)
        y = (x + a/x)/2
        print
        if abs(y-x) < 0.00001:
            return y
        x = y


print(square_root(125))
