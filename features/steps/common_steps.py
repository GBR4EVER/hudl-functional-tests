from behave import given, when, then
from framework.webapp import WebApp


@given('I load the website')
def step_impl_load_website(context):
    WebApp.load_website()


@when('I go to "{page}" page')
def step_impl_goto_page(context, page):
  WebApp.goto_page(page)


@then('I see this "{component}" page')
def step_impl_verify_component(context, component):
  WebApp.verify_nav_button_exists(component)