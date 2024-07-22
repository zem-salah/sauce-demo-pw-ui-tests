from behave import when

from Actions.login_actions import Login


@when('he logs in')
def user_logs_in(context):
    context.current_page = Login.login_as(context.current_user)
