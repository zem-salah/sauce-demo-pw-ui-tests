from typing import Union, Type, Any
from robber import expect, BadExpectation
from playwright.sync_api import expect as pw_expect

from page_object.page_factory import PageFactory


class AssertThat:

    def __new__(cls, obj):
        return obj


class Cart:

    should_init = True

    @classmethod
    def set_context(cls, context):
        cls.context = context
        cls.primary_header = PageFactory(context.page)('primary header')

    @classmethod
    def contains_number_of_product(cls, expected_number_of_products):
        pw_expect(cls.primary_header.cart_badge).to_have_text(
            expected_number_of_products)


class Page:

    should_init = True

    @classmethod
    def set_context(cls, context):
        cls.context = context

    def __init__(self, expected_page_pretty_name):
        self.expected_page_pretty_name = expected_page_pretty_name
        self.expected_page_object = PageFactory(self.context)(
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
