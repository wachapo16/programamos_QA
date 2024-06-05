from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

buttonLogin = driver.find_element(By.LINK_TEXT, "SIGN-ON") .click()

try:
    loginImag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='images/mast_signon.gif']"))
        )
      
    if loginImag:
        print("!Bienvenido al Sign in¡")
        print("Por favor procede a llenar las credenciales")

    mail = driver.find_element(By.XPATH, "//input[contains(@name,'userName')]") .send_keys("walterchp@gmail.com")
    password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]") .send_keys("Prueba.01")
    
    button = driver.find_element(By.XPATH, "//input[contains(@type,'submit')]") .click()
    time.sleep(2)
    
    confirmationMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Login Successfully')]"))
        )
    
    if confirmationMessage:
        print("Mensaje de confirmación encontrado")
        print(confirmationMessage.text)
except Exception as e:
    print("Error al cargar la pagina de resgister", e)

    