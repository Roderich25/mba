#!/usr/bin/env python3
def hanoi(n_disc, start, helper, target):
    if n_disc == 0:
        return
    else:
        hanoi(n_disc - 1, start, target, helper)
        move(start, target)
        hanoi(n_disc - 1, helper, start, target)


def move(start, target):
    print(f"Move disc from {start} to {target}.")


hanoi(4, "A", "B", "C")
