from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from lib.pages.home_page import HomePage
import time

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.wait = WebDriverWait(context.browser, 10)
    context.home_page = HomePage(context)

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    context.url = "https://demo.guru99.com/test/newtours/index.php"


def before_scenario(context, scenario):
    context.browser.get(context.url)
    context.valid_email = "walterchp@gmail.com"
    context.valid_password = "Prueba.01"
    time.sleep(3)
