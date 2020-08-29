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
    file = tree.xpath('//a[@aria-label="Descarga el archivo 2015 en formato csv"]/@href')
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
