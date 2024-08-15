from behave import given, then, when

from actions.form_actions import Form
from Assertion.assertion import AssertThat, Page
from page_object.page_factory import PageFactory


@given('sauce demo login form is visible')
def navigate_to_login_form(context):
    PageFactory(context.page)('login').navigate()


@when('he fills')
def user_fills_form(context):
    """
    Generic step to fill a form from a table composed of two columns
    '|field|value|'

    Each row in this table will be used to fill one field in the form.

    'field' column, must contain pretty names of the fields to fill.
    Exemple :
        |field      |value        |
        |user name  | new user    |
        |address    | foo         |
        |email      | bar@foo.com |
        ...
    """
    Form(context.current_page).fill_from_table(context.table)


@then('he should be on "{page_pretty_name}" page')
def assert_page_is_visible(context, page_pretty_name):
    AssertThat(Page(page_pretty_name)).is_visible()
    AssertThat(Page(page_pretty_name)).is_current_page()
