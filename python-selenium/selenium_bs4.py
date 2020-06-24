from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
import time

# Selenium part
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(os.getcwd() + '/chromedriver', options=chromeOptions)
browser.get('https://www.premierleague.com')
time.sleep(1)
players = browser.find_element_by_link_text("Players")
time.sleep(1)
players.click()
time.sleep(5)
search = browser.find_element_by_id("search-input")
search.send_keys("Raúl Jiménez")
search_go = browser.find_element_by_class_name("searchIconContainer.searchCommit")
search_go.click()
time.sleep(1)
raul_jimenez = browser.find_element_by_partial_link_text("Raúl Jiménez")
raul_jimenez.click()
page_source = browser.page_source

# BeautifulSoup part
soup = BeautifulSoup(page_source, 'lxml')
title_finder = soup.find_all("span", class_="title")
print(title_finder)

print('*' * 10)
for title in title_finder:
    print(title.string)
