from selenium import webdriver
from selenium.webdriver.common.by import By

class HomeWebElements:
    url = "https://demo.guru99.com/test/newtours/index.php"
    
    # Elements register
    button_register = (By.LINK_TEXT, "REGISTER")
    register_image = (By.XPATH, "//img[@src='images/mast_register.gif']")
    email_register = (By.XPATH, "//input[contains(@id,'email')]")
    password_register = (By.XPATH, "//input[contains(@name,'password')]")
    confirm_password = (By.XPATH, "//input[contains(@name,'confirmPassword')]")
    button = (By.XPATH, "//input[@src='images/submit.gif']")
    confirmation_message = (By.XPATH, "//b[contains(.,'Note: Your user name is walterchp@gmail.com.')]")
    
    # Elements login
    email_login = (By.XPATH, "//input[contains(@type,'text')]")
    password_login = (By.XPATH, "//input[contains(@type,'password')]")
    sign_in_button = (By.XPATH, "//input[contains(@type,'submit')]")
    login_confirmation_message = (By.XPATH, "//h3[contains(.,'Login Successfully')]")

    
    
    
