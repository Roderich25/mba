import os
from zipfile import ZipFile
import requests

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

files = ['/contenidos/masiva/denue/2016_01/denue_01_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_02_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_03_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_04_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_05_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_06_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_07_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_08_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_09_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_10_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_11_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_12_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_13_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_14_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_15_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_16_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_17_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_18_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_19_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_20_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_21_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_22_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_23_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_24_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_25_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_26_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_27_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_28_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_29_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_30_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_31_0116_csv.zip',
         '/contenidos/masiva/denue/2016_01/denue_32_0116_csv.zip']

files = ['/contenidos/masiva/denue/2017_11/denue_01_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_02_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_03_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_04_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_05_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_06_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_07_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_08_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_09_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_10_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_11_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_12_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_13_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_14_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_15_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_16_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_17_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_18_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_19_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_20_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_21_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_22_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_23_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_24_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_25_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_26_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_27_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_28_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_29_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_30_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_31_1117_csv.zip', '/contenidos/masiva/denue/2017_11/denue_32_1117_csv.zip']

def denue_download(file_url):
    state = os.path.join('denue', file_url.split('/')[-1])
    resp = requests.get(file_url)
    with open(state, 'wb') as fp:
        fp.write(resp.content)
    print(file_url)
    try:
        with ZipFile(state) as zp:
            zp.extractall(path='denue/')
        os.remove(state)
    except Exception as e:
        print(e)


def main():
    for file in files:
        url = f'https://www.inegi.org.mx{file}'  # CHECK URL!!!
        print(url, url.split('/')[-1])
        denue_download(url)


if __name__ == '__main__':
    main()
