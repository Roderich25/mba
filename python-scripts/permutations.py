#!/usr/bin/env python3
letters = ['a', 'b', 'c', 'd', 'e']


def permutations(letters, cadena=""):
    if not letters:
        print(cadena)
    else:
        for i in letters:
            available = letters.copy()
            available.remove(i)
            permutations(available, cadena+str(i))


permutations(letters)
