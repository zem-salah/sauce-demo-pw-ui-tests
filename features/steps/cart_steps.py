from behave import then, when

from Assertion.assertion import AssertThat, Cart
from Actions.navigation_actions import Navigate
from data.products import Product


@when('he goes to the shopping cart')
def navigate_to_cart(context):
    context.current_page = Navigate.to_shopping_cart()


@when('the user proceed to checkout')
def navigate_to_checkout(context):
    context.current_page = Navigate.proceed_to_checkout()


@then('the shopping cart is empty')
def assert_cart_is_empty(context):
    AssertThat(Cart).is_empty()


@then('the cart should contain "{expected_number_of_products}" product')
def assert_cart_contain_product(context, expected_number_of_products):
    AssertThat(Cart).contains_number_of_product(expected_number_of_products)


@then('"{product_pretty_name}" product is in the cart and quantity '
      'is "{expected_quantity}"')
def assert_product_is_in_cart(context, product_pretty_name, expected_quantity):
    AssertThat(Cart).contains_product(Product(product_pretty_name))\
        .with_quantity_of(expected_quantity)
