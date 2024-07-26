from page_object.page_factory import PageFactory
from page_object.cart_page import CartPage


class Navigate:

    should_init = True
    page = None
    primary_header = None

    @classmethod
    def set_page(cls, page):
        cls.page = page
        cls.primary_header = PageFactory(cls.page)('primary header')

    @classmethod
    def to_shopping_cart(cls) -> CartPage:
        return cls.primary_header.access_cart()
