from behave import when

from Actions.navigation_actions import Navigate


@when('he access checkout overview page')
def navigate_to_checkout_overview(context):
    context.current_page = Navigate.to_checkout_overview()
