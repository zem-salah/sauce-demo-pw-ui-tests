from playwright.sync_api import expect

from page_object.base_page import BasePage


class CheckoutComplete(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.back_to_product_btn = page.get_by_test_id('back-to-products')

    def is_visible(self):
        expect(self.back_to_product_btn).to_be_visible()
        return True
