from random import randint
import time
import asyncio


def odds(start, stop):
    for odd in range(start, stop+1, 2):
        yield odd


def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)


def die():
    time.sleep(2)
    return randint(1, 6)


if __name__ == '__main__':
    # main()
    pass
