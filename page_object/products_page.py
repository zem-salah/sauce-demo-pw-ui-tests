from data.products import ProductsData
from page_object.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.add_product_to_cart_locator_prefix = 'add-to-cart-{:s}'

    def is_visible(self):
        return True

    def add_product_to_cart(self, product_pretty_name):
        self.page.get_by_test_id(
            self.add_product_to_cart_locator_prefix.format(
                ProductsData.get_product_locator_value(product_pretty_name)
            )
        ).click()
