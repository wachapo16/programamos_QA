from behave import given

@given('I navigate to the Mercury main page')
def step_navigate_to_main_page(context):
    context.browser.get(context.url)


