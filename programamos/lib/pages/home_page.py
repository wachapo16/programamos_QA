from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lib.pages.web_elements.home_web_elements import HomeWebElements
from lib.pages.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, context):
        self.browser = context.browser
        self.wait = context.wait
        self.elements = HomeWebElements

    def navigate(self, url):
        self.browser.get(url)
        
    def click_register_button(self):
        self.browser.find_element(*self.elements.button_register).click()

    def find_register_image(self):
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.elements.register_image)
            )
        except TimeoutException:
            return None

    def enter_email(self, email):
        email_element = self.wait.until(
            EC.presence_of_element_located(self.elements.email_register)
        )
        email_element.send_keys(email)

    def enter_password(self, password):
        self.browser.find_element(*self.elements.password_register).send_keys(password)

    def enter_confirm_password(self, password):
        self.browser.find_element(*self.elements.confirm_password).send_keys(password)

    def click_submit_button(self):
        self.browser.find_element(*self.elements.button).click()

    def is_on_registration_page(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.elements.confirmation_message)
            )
        except TimeoutException:
            return True 

    def enter_login_email(self, email):
        self.browser.find_element(*self.elements.email_login).send_keys(email)

    def enter_login_password(self, password):
        self.browser.find_element(*self.elements.password_login).send_keys(password)

    def click_sign_in_button(self):
        self.browser.find_element(*self.elements.sign_in_button).click()
