from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(os.getcwd() + '/chromedriver', options=chromeOptions)
browser.get('https://www.python.org')

#ele = browser.find_element_by_partial_link_text('Learn M')
#ele.click()

ele = browser.find_element_by_id('id-search-field')
time.sleep(1)
ele.clear()
ele.send_keys("hash")
ele.send_keys(Keys.RETURN)


