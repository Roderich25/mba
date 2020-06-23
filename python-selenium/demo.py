from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--headless')
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(os.getcwd() + '/chromedriver', options=chromeOptions)
browser.get('https://www.pluralsight.com')
time.sleep(5)
icon = browser.find_element_by_xpath("//li[@class='ps-nav--search']//a[@class='ps-nav--primary']")
print(icon)
icon.click()
# icons = browser.find_elements_by_xpath("//a[@class='ps-nav--primary']")
# icons[4].click()
time.sleep(4)
ele = browser.find_element_by_name("q")
time.sleep(3)
ele.clear()
ele.send_keys("Padman")
ele.send_keys(Keys.RETURN)

# browser.quit()
browser