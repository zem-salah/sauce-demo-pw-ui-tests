from behave import then

from Assertion.assertion import AssertThat, Cart


@then('the shopping cart is empty')
def assert_cart_is_empty(context):
    AssertThat(Cart).is_empty()


@then('the cart should contain "{expected_number_of_products}" product')
def assert_cart_contain_product(context, expected_number_of_products):
    AssertThat(Cart).contains_number_of_product(expected_number_of_products)
