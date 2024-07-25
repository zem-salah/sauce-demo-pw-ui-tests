from behave import when

from Actions.login_actions import Login
from data.user import User


@when('the user logs in as "{user_role}"')
def login_as_user(context, user_role):
    context.current_user = User(user_role)
    context.current_page = Login.login_as(context.current_user)
