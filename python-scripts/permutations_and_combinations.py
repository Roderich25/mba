#!/usr/bin/env python3
letters = ["a", "b", "c", "d", "e"]


def permutations(letters, string=""):
    if not letters:
        print(string)
    else:
        for l in letters:
            available = letters.copy()
            available.remove(l)
            permutations(available, string + str(l))


print("\nPermutations:")
permutations(letters)


def combinations(n, m, letters, string=""):
    for l in range(0, len(letters)):
        if n == 1:
            print(string + letters[l])
        else:
            if l <= m - n:
                combinations(n - 1, m, letters[l + 1 : m + 1], string + letters[l])


print("\nCombinations:")
combinations(4, 5, letters)
