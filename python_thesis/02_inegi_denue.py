import os
from zipfile import ZipFile
import requests

files = ['/contenidos/masiva/denue/denue_01_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_02_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_03_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_04_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_05_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_06_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_07_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_08_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_09_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_10_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_11_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_12_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_13_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_14_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_15_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_16_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_17_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_18_04062015_csv.zip',
         '/contenidos/masiva/denue/denue_19_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_20_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_21_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_22_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_23_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_24_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_25_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_26_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_27_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_28_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_29_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_30_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_31_25022015_csv.zip',
         '/contenidos/masiva/denue/denue_32_25022015_csv.zip']


def denue_download(file_url):
    state = os.path.join('denue', file_url.split('/')[-1])
    resp = requests.get(file_url)
    with open(state, 'wb') as fp:
        fp.write(resp.content)
    print(url)
    try:
        with ZipFile(state) as zp:
            zp.extractall(path='denue/')
        os.remove(state)
    except Exception as e:
        print(e)


for file in files:
    url = f'https://www.inegi.org.mx{file}'
    print(url, url.split('/')[-1])
    denue_download(url)
