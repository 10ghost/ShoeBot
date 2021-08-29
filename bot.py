from selenium import webdriver
from webdriver_manager.Firefox import FirefoxDriverManager
import time
#initiate the browser
browser = webdriver.Firefox(FirefoxDriverManager())
#Open the Website
browser.get('https://www.footlocker.com/')
print(browser)
search = driver.find_element_by_name("s")
search.send_keys("")
search.send_keys("")
search.send_keys(keys.RETURN)
