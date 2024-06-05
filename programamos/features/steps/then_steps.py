from behave import then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.pages.web_elements.home_web_elements import HomeWebElements

@then('the user should be on the registration page')
def step_impl(context):
    assert context.home_page.is_on_registration_page(), "User is not on the registration page"

@then('the registration confirmation message is displayed')
def step_impl(context):
    confirmation_message = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(HomeWebElements.confirmation_message)
    )
    assert confirmation_message is not None

@then('the login confirmation message is displayed')
def step_impl(context):
    confirmation_message = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(HomeWebElements.login_confirmation_message)
    )
    assert confirmation_message is not None
