from page_object.cart_page import CartPage
from page_object.checkout_complete import CheckoutComplete
from page_object.checkout_form import CheckoutForm
from page_object.checkout_overview import CheckoutOverview
from page_object.login_form import LoginFrom
from page_object.primary_header import PrimaryHeader
from page_object.products_page import ProductsPage


class PageFactory:

    def __init__(self, page):
        self._page = page

    def __call__(self, page_name):
        page_name_to_creation_function = {
            'checkout complete': self._create_checkout_complete_page,
            'checkout information': self._create_checkout_information_page,
            'checkout overview': self._create_checkout_overview_page,
            'login': self._create_login_page,
            'primary header': self._create_primary_header_object,
            'products': self._create_products_page,
            'shopping cart': self._create_shopping_cart_page,
        }
        page_method = page_name_to_creation_function.get(page_name)
        if page_method:
            return page_method()
        else:
            raise ValueError(f"Page {page_name} not found")

    def _create_checkout_complete_page(self):
        return CheckoutComplete(self._page)

    def _create_checkout_information_page(self):
        return CheckoutForm(self._page)

    def _create_checkout_overview_page(self):
        return CheckoutOverview(self._page)

    def _create_login_page(self):
        return LoginFrom(self._page)

    def _create_primary_header_object(self):
        return PrimaryHeader(self._page)

    def _create_products_page(self):
        return ProductsPage(self._page)

    def _create_shopping_cart_page(self):
        return CartPage(self._page)
