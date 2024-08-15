from behave import when

from actions.navigation_actions import Navigate


@when('the user completes the checkout')
def navigate_to_checkout_complete(context):
    context.current_page = Navigate.to_checkout_complete()
