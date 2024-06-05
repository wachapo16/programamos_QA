from behave import when

@when('the user clicks on the register button')
def step_impl(context):
    context.home_page.click_register_button()
    
@when('the user enters valid registration details')
def step_impl(context):
    context.home_page.enter_email(context.valid_email)
    context.home_page.enter_password(context.valid_password)
    context.home_page.enter_confirm_password(context.valid_password)

@when('the user submits the registration form')
def step_impl(context):
    context.home_page.click_submit_button()

@when('the user enters valid login credentials')
def step_impl(context):
    context.home_page.enter_login_email(context.valid_email)
    context.home_page.enter_login_password(context.valid_password)

@when('the user submits the login form')
def step_impl(context):
    context.home_page.click_sign_in_button()
