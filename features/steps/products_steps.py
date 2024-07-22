from behave import when

from Actions.products_actions import Products
from data.products import Product


@when('he adds "{product_pretty_name}" product to cart')
def add_product_in_cart(context, product_pretty_name):
    Products.add_to_cart(Product(product_pretty_name))
