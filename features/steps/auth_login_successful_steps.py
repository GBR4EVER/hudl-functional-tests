from behave import then
from framework.webapp import webapp


@then('the user is successfully logged in as expected')
def step_impl_verify_user_logged_in(context):
    webapp.verify_user_logged_in()


@then('the user is routed to the coach home page as expected')
def step_impl_verify_coach_page(context):
    webapp.verify_coach_page()