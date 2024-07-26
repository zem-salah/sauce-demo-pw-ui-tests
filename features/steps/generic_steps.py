from behave import given, then

from Assertion.assertion import AssertThat, Page
from page_object.page_factory import PageFactory


@given('sauce demo login form is visible')
def navigate_to_login_form(context):
    PageFactory(context.page)('login').navigate()


@then('he should be on "{page_pretty_name}" page')
def assert_page_is_visible(context, page_pretty_name):
    AssertThat(Page(page_pretty_name)).is_visible()
    AssertThat(Page(page_pretty_name)).is_current_page()
