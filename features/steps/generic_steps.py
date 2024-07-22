from behave import given, then

from Assertion.assertion import AssertThat
from data.user import User
from page_object.page_factory import PageFactory


@given('"{user_role}" is on the "{form_pretty_name}" form')
def navigate_to_form(context, user_role, form_pretty_name):
    context.current_user = User(user_role)
    PageFactory(context.page)(form_pretty_name).navigate()


@then('he should be on "{page_pretty_name}" page')
def assert_page_is_visible(context, page_pretty_name):
    AssertThat.Page(page_pretty_name).is_visible()
    AssertThat.Page(page_pretty_name).is_current_page()
