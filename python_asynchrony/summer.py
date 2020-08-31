import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f'worker-{name}')
    url = f'https://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16'
    response = await session.request(method='GET', url=url)
    value = await response.text()
    value = json.loads(value)
    return value['data']


async def main():
    async with aiohttp.ClientSession() as session:
        response = await worker('bob', 3, session)
        print('response:', response, type(response))


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()-start
    print(f'time: {elapsed:.4f}')
