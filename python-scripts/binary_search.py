#!/usr/bin/env python3
import math
target = 1_000_000
epsilon = 0.000_000_1
years = 5


def f_X(x):
    output = 100_000
    for _ in range(0, years*12):
        output *= x
    return output


def binary_search():
    left = 0
    right = target
    mid = 0
    counter = 0
    while abs(target-f_X(mid)) > epsilon:
        mid = (left + right)/2
        counter += 1
        if (target-f_X(mid)) > 0:
            left = mid
        else:
            right = mid
    print(mid, f'#{counter}')
    return mid


aprox = binary_search()
print(100_000 * aprox**(years*12))
