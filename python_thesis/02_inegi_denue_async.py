import os
from zipfile import ZipFile
import asyncio
import aiohttp
import aiofiles

FOLDER = 'inegi'

files = ['denue_01_25022015_csv.zip',
         'denue_02_25022015_csv.zip',
         'denue_03_25022015_csv.zip',
         'denue_04_25022015_csv.zip',
         'denue_05_25022015_csv.zip',
         'denue_06_25022015_csv.zip',
         'denue_07_25022015_csv.zip',
         'denue_08_25022015_csv.zip',
         'denue_09_25022015_csv.zip',
         'denue_10_25022015_csv.zip',
         'denue_11_25022015_csv.zip',
         'denue_12_25022015_csv.zip',
         'denue_13_25022015_csv.zip',
         'denue_14_25022015_csv.zip',
         'denue_15_25022015_csv.zip',
         'denue_16_25022015_csv.zip',
         'denue_17_25022015_csv.zip',
         'denue_18_04062015_csv.zip',
         'denue_19_25022015_csv.zip',
         'denue_20_25022015_csv.zip',
         'denue_21_25022015_csv.zip',
         'denue_22_25022015_csv.zip',
         'denue_23_25022015_csv.zip',
         'denue_24_25022015_csv.zip',
         'denue_25_25022015_csv.zip',
         'denue_26_25022015_csv.zip',
         'denue_27_25022015_csv.zip',
         'denue_28_25022015_csv.zip',
         'denue_29_25022015_csv.zip',
         'denue_30_25022015_csv.zip',
         'denue_31_25022015_csv.zip',
         'denue_32_25022015_csv.zip']

files = list(map(lambda s: f'https://www.inegi.org.mx/contenidos/masiva/denue/{s}', files))


async def denue_download(file_url, session, folder=FOLDER):
    state = os.path.join(folder, file_url.split('/')[-1])
    print(file_url)
    async with session.request(method='GET', url=file_url) as resp:
        if resp.status == 200:
            f = await aiofiles.open(state, mode='wb')
            await f.write(await resp.read())
            await f.close()
            try:
                with ZipFile(state) as zp:
                    zp.extractall(path=folder)
                os.remove(state)
            except Exception as e:
                print(e)


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(denue_download(f, session) for f in files))


if __name__ == '__main__':
    asyncio.run(main())