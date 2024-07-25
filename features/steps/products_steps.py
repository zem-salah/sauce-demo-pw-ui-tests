from behave import then, when

from Actions.products_actions import Products
from Assertion.assertion import AssertThat, ProductTile
from data.products import Product


@when('he adds "{product_pretty_name}" product to cart')
def add_product_in_cart(context, product_pretty_name):
    Products.add_to_cart(Product(product_pretty_name))


@then('the add to cart button for product "{product_pretty_name}" turns into remove button')
def assert_add_to_cart_become_remove(context, product_pretty_name):
    AssertThat(ProductTile(Product(product_pretty_name)))\
        .remove_button_is_visible()
