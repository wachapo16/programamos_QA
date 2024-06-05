from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def register_mercury():
    try:
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/newtours/index.php")
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)

        button_register = driver.find_element(By.LINK_TEXT, "REGISTER").click()
        time.sleep(1)

        register_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='images/mast_register.gif']"))
        )

        if register_image:
            print("!Bienvenido a la página del registro¡")
            print("Por favor procede a llenar los campos")

        mail = driver.find_element(By.XPATH, "//input[contains(@id,'email')]").send_keys("walterchp@gmail.com")
        time.sleep(1)

        password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]").send_keys("Prueba.01")
        time.sleep(1)

        confirm_password = driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]").send_keys("Prueba.01")
        time.sleep(1)

        button = driver.find_element(By.XPATH, "//input[@src='images/submit.gif']") .click()
        time.sleep(2)

        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Note: Your user name is walterchp@gmail.com.')]"))
        )

        if confirmation_message:
            print("Mensaje de confirmación encontrado")
            print(confirmation_message.text)
    except Exception as e:
        print("Error al cargar la página de registro", e)
    finally:
        driver.quit()
register_mercury()


def login_mercury():
    try:
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/newtours/index.php")
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        
        email_login = driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("walterchp@gmail.com")
        password_login = driver.find_element(By.XPATH, "//input[contains(@type,'password')]").send_keys("Prueba.01")

        signin_button = driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
        time.sleep(2)

        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Login Successfully')]"))
        )

        if confirmation_message:
            print("Mensaje de confirmación encontrado")
            print(confirmation_message.text)
    except Exception as e:
        print("Error al cargar la página de inicio de sesión", e)
    finally:
        driver.quit()

login_mercury()
