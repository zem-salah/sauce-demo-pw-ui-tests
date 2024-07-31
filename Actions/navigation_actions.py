from page_object.page_factory import PageFactory
from page_object.cart_page import CartPage
from page_object.checkout_form import CheckoutForm


class Navigate:

    should_init = True
    page = None
    primary_header = None

    @classmethod
    def set_page(cls, page):
        cls.page = page
        cls.primary_header = PageFactory(cls.page)('primary header')
        cls.cart_page = PageFactory(cls.page)('shopping cart')

    @classmethod
    def to_shopping_cart(cls) -> CartPage:
        return cls.primary_header.access_cart()

    @classmethod
    def proceed_to_checkout(cls) -> CheckoutForm:
        """
        In cart page, we click on checkout button to go to the checkout
        information form
        :return: None
        """
        return cls.cart_page.checkout()
