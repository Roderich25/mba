from selenium import webdriver
import os
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
browser = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)

browser.get('https://www.pluralsight.com')


browser.quit()
