from behave import given, when
from framework.webapp import webapp


@given('the user loads the website')
def step_impl_load_website(context):
    try:
        webapp.load_website()
    except:
        print("Can't load website")
        webapp.driver.quit()


@given('the user selects to login from the welcome page')
def step_impl_click_login(context):
    try:
        webapp.click_nav_login()
    except:
        print("Can't locate login button")
        webapp.driver.quit()


@given('the user inputs an valid username and password')
def step_impl_input_credentials(context):
    webapp.input_credentials()


@when('the user selects the login button from the login page')
def step_impl_goto_page(context):
    webapp.click_login()


