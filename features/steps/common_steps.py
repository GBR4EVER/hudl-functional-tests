from behave import given, when
from framework.webapp import webapp


@given('the user loads the website')
def the_user_loads_the_website(context):
    try:
        webapp.load_website()
    except:
        print("Can't load website.")
        webapp.driver.quit()


@given('the user selects to login from the welcome page')
def the_user_selects_to_login_from_the_welcome_page(context):
    try:
        webapp.click_nav_login()
    except:
        print("Can't locate login button.")
        webapp.driver.quit()


@given('the user inputs an valid username and password')
def the_user_inputs_an_valid_username_and_password(context):
    webapp.input_credentials()


@when('the user selects the login button from the login page')
def the_user_selects_the_login_button_from_the_login_page(context):
    webapp.click_login()


