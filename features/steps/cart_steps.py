from behave import then, when

from Assertion.assertion import AssertThat, Cart
from Actions.navigation_actions import Navigate


@when('he goes to the shopping cart')
def navigate_to_cart(context):
    context.current_page = Navigate.to_shopping_cart()


@then('the shopping cart is empty')
def assert_cart_is_empty(context):
    AssertThat(Cart).is_empty()


@then('the cart should contain "{expected_number_of_products}" product')
def assert_cart_contain_product(context, expected_number_of_products):
    AssertThat(Cart).contains_number_of_product(expected_number_of_products)
