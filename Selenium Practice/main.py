from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title 
elem = driver.find_element(By.NAME,"q")
elem.clear
elem.send_keys("dfgftg")
elem.send_keys(Keys.RETURN)
assert "No result Found." not in driver.page_source
time.sleep(6)
driver.close()