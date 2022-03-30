from selenium import webdriver
import time

chrome_driver_path = "C:\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://wiki.hidirgungor.com")
time.sleep(7)
driver.close()

