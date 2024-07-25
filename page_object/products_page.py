from playwright.sync_api import Locator

from data.products import Product
from page_object.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.add_product_to_cart_locator_prefix = 'add-to-cart-{:s}'
        self.remove_product_from_cart_locator_prefix = 'remove-{:s}'

    def is_visible(self):
        return True

    def add_to_cart(self, product_name) -> Locator:
        return self.page.get_by_test_id(
            self.add_product_to_cart_locator_prefix.format(
                Product.get_locator_value(product_name)
            )
        )

    def add_product_to_cart(self, product_name) -> None:
        self.add_to_cart(product_name).click()

    def remove(self, product_name) -> Locator:
        return self.page.get_by_test_id(
            self.remove_product_from_cart_locator_prefix.format(
                Product.get_locator_value(product_name)
            )
        )
