from playwright.sync_api import expect

from data.products import Product
from page_object.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def is_visible(self):
        expect(self.page.get_by_test_id('title')).to_have_text('Your Cart')
        expect(self.page.get_by_test_id('continue-shopping')).to_be_visible()
        expect(self.page.get_by_test_id('checkout')).to_be_visible()
        return True

    def get_products(self) -> list[Product]:
        cart_items = self.page.get_by_test_id('cart-list') \
            .get_by_test_id('inventory-item-name').all_inner_texts()
        return [Product(cart_item) for cart_item in cart_items]

    def get_quantity_of_product(self, product: Product) -> int:
        return self.page.get_by_test_id('inventory-item').filter(
            has_text=product.name).get_by_test_id('item-quantity').inner_text()
