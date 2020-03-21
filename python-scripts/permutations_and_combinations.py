#!/usr/bin/env python3
letters = ["a", "b", "c", "d"]


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
        elif l <= m - n:
            combinations(n - 1, 5, letters[l + 1 : m + 1], string + letters[l])


print("\nCombinations:")
combinations(3, 4, letters)
