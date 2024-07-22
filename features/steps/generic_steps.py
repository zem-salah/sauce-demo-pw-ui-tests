from behave import given, then

from data.user import User
from page_object.page_factory import PageFactory


@given('"{user_role}" is on the "{form_pretty_name}" form')
def navigate_to_form(context, user_role, form_pretty_name):
    context.current_user = User(user_role)
    PageFactory(context.page)(form_pretty_name).navigate()
