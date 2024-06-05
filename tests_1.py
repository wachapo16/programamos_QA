import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
time.sleep(3)

name = driver.find_element(By.ID, "userName")
name.send_keys("Walter")
time.sleep(2)

email = driver.find_element(By.ID, "userEmail").send_keys("prueba@selenium.com")
time.sleep(1)