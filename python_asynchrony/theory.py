from random import randint
import asyncio
import time


def odds(start, stop):
    for odd in range(start, stop+1, 2):
        yield odd


async def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)
    #
    start = time.perf_counter()
    r = await die()
    elapsed = time.perf_counter() - start
    print(f'r: {r}, time: {elapsed:.2f}')
    #
    start = time.perf_counter()
    r = await asyncio.gather(*(die() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f'r: {r}, time: {elapsed:.2f}')
    #
    async for so in square_odds(11, 21):
        print('so:', so)


async def die():
    await asyncio.sleep(2)
    return randint(1, 6)


async def square_odds(start, stop):
    for odd in odds(start, stop):
        await asyncio.sleep(2)
        yield odd**2


if __name__ == '__main__':
    asyncio.run(main())
