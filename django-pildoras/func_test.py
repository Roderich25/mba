from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000/op")

assert browser.page_source.find("85223")

browser.close()
