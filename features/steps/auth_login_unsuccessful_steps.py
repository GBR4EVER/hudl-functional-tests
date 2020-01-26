from behave import given, then
from framework.webapp import webapp


@given('the user inputs an invalid username and or password')
def the_user_inputs_an_invalid_username_and_or_password(context):
    webapp.input_invalid_credentials()


@then('the user is prompted with a login error as expected')
def the_user_is_prompted_with_a_login_error_as_expected(context):
    webapp.verify_login_error()