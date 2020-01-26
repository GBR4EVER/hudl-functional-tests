from behave import then, when
from framework.webapp import webapp


@when('the user selects the remember password box')
def the_user_selects_the_remember_password_box(context):
    try:
        webapp.select_login()
    except:
        print("User cannot select the remember password box.")


@then('the user is successfully logged in as expected')
def the_user_is_successfully_logged_in_as_expected(context):
    webapp.verify_user_logged_in()


@then('the user is routed to the coach home page as expected')
def the_user_is_routed_to_the_coach_home_page_as_expected(context):
    webapp.verify_coach_page()
