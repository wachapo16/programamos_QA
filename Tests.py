from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

name = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
name.send_keys("walter")
time.sleep(1)

mail = driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]") .send_keys("walterchp@gmail.com")
time.sleep(1)

current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']") .send_keys("colocando texto de prueba")
time.sleep(1)

permanent_address = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']") .send_keys("colocando texto two de prueba")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

button = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]") .click()
time.sleep(2)
driver.close()