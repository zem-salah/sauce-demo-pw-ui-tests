from typing import Union, Type, Any
from robber import expect, BadExpectation
from playwright.sync_api import expect as pw_expect

from data.products import Product
from page_object.page_factory import PageFactory


class BaseAssertion:

    should_init = True

    @classmethod
    def set_context(cls, context):
        cls.context = context


class AssertThat:
    """
    Used to ease readability and access assertion methods
    """

    def __new__(cls, obj):
        return obj


class Cart(BaseAssertion):
    """
    Assertion class that contains checks related to the shopping cart
    """

    @classmethod
    def set_context(cls, context):
        super().set_context(context)
        cls.primary_header = PageFactory(context.page)('primary header')
        cls.cart_page = PageFactory(context.page)('shopping cart')

    @classmethod
    def contains_number_of_product(cls, expected_number_of_products):
        pw_expect(cls.primary_header.cart_badge).to_have_text(
            expected_number_of_products)

    @classmethod
    def contains_product(cls, product: Product):
        cls._current_product = product
        expect(product in cls.cart_page.get_products()).to.be.true()
        return cls

    @classmethod
    def with_quantity_of(cls, expected_quantity: int):
        """
        must be chained with contains_product. This is to ease readability.
        contains_product must set a _current_product in the class to be used
        by this method.

        :param expected_quantity: expected quantity to be in cart of
        _current_product
        :return: None
        """
        expect(cls.cart_page.get_quantity_of_product(cls._current_product))\
            .to.be.eq(expected_quantity)

    @classmethod
    def is_empty(cls):
        pw_expect(cls.primary_header.cart_badge).not_to_be_visible()


class Page(BaseAssertion):
    """
    Assertion class that contains checks related to a page (not the playwright
    Page object, but a page in web context)
    """

    def __init__(self, expected_page_pretty_name):
        self.expected_page_pretty_name = expected_page_pretty_name
        self.expected_page_object = PageFactory(self.context.page)(
            expected_page_pretty_name)
        self.actual_page = self.context.current_page

    def is_visible(self):
        try:
            expect(self.expected_page_object.is_visible()).to.be.true()
        except BadExpectation as e:
            e.message = f'Page {self.expected_page_pretty_name} is not ' \
                        f'visible'
            raise e

    def is_current_page(self):
        expect(isinstance(
            self.actual_page, type(self.expected_page_object)
        )).to.be.true()


class ProductTile(BaseAssertion):
    """
    Assertion class that contains checks related to a product cards displayed
    in the home page after logging in.
    """

    def __init__(self, product: Product):
        self.product_name = product.name
        self.product_page = PageFactory(self.context.page)('products')

    def remove_button_is_visible(self):
        pw_expect(self.product_page.remove(self.product_name)).to_be_visible()
