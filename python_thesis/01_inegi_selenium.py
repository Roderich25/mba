from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from lxml import html

chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(os.getcwd() + '/chromedriver', options=chromeOptions)
browser.get('https://www.inegi.org.mx/app/descarga/default.html')

states = browser.find_elements_by_xpath('//ul[@id="ulAG"]//li[@class="undefined"]//a')

files = []
print(states)
for state in states:
    state.click()
    sleep(10)
    tree = html.fromstring(browser.page_source)
    file = tree.xpath('//a[@aria-label="Descarga el archivo 2020/11 en formato csv"]/@href')
    print(file)
    files.extend(file)
browser.quit()
print(files)

output = ['/contenidos/masiva/denue/denue_01_25022015_csv.zip',
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

out2018 = ['/contenidos/masiva/denue/2018_11/denue_01_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_02_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_03_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_04_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_05_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_06_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_07_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_08_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_09_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_10_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_11_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_12_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_13_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_14_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_16_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_17_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_18_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_19_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_20_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_21_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_22_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_23_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_24_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_25_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_26_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_27_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_28_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_29_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_30_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_31_1118_csv.zip',
           '/contenidos/masiva/denue/2018_11/denue_32_1118_csv.zip']

out2019 = ['/contenidos/masiva/denue/2019_11/denue_01_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_02_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_03_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_04_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_05_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_06_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_07_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_08_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_09_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_10_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_11_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_12_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_13_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_14_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_15_1_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_15_2_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_16_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_17_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_18_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_19_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_20_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_21_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_22_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_23_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_24_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_25_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_26_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_27_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_28_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_29_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_30_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_31_1119_csv.zip',
           '/contenidos/masiva/denue/2019_11/denue_32_1119_csv.zip']

out2020 = ['/contenidos/masiva/denue/denue_01_csv.zip',
           '/contenidos/masiva/denue/denue_02_csv.zip',
           '/contenidos/masiva/denue/denue_03_csv.zip',
           '/contenidos/masiva/denue/denue_04_csv.zip',
           '/contenidos/masiva/denue/denue_05_csv.zip',
           '/contenidos/masiva/denue/denue_06_csv.zip',
           '/contenidos/masiva/denue/denue_07_csv.zip',
           '/contenidos/masiva/denue/denue_08_csv.zip',
           '/contenidos/masiva/denue/denue_09_csv.zip',
           '/contenidos/masiva/denue/denue_10_csv.zip',
           '/contenidos/masiva/denue/denue_11_csv.zip',
           '/contenidos/masiva/denue/denue_12_csv.zip',
           '/contenidos/masiva/denue/denue_13_csv.zip',
           '/contenidos/masiva/denue/denue_14_csv.zip',
           '/contenidos/masiva/denue/denue_15_1_csv.zip',
           '/contenidos/masiva/denue/denue_15_2_csv.zip',
           '/contenidos/masiva/denue/denue_16_csv.zip',
           '/contenidos/masiva/denue/denue_17_csv.zip',
           '/contenidos/masiva/denue/denue_18_csv.zip',
           '/contenidos/masiva/denue/denue_19_csv.zip',
           '/contenidos/masiva/denue/denue_20_csv.zip',
           '/contenidos/masiva/denue/denue_21_csv.zip',
           '/contenidos/masiva/denue/denue_22_csv.zip',
           '/contenidos/masiva/denue/denue_23_csv.zip',
           '/contenidos/masiva/denue/denue_24_csv.zip',
           '/contenidos/masiva/denue/denue_25_csv.zip',
           '/contenidos/masiva/denue/denue_26_csv.zip',
           '/contenidos/masiva/denue/denue_27_csv.zip',
           '/contenidos/masiva/denue/denue_28_csv.zip',
           '/contenidos/masiva/denue/denue_29_csv.zip',
           '/contenidos/masiva/denue/denue_30_csv.zip',
           '/contenidos/masiva/denue/denue_31_csv.zip',
           '/contenidos/masiva/denue/denue_32_csv.zip']
