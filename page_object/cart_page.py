from playwright.sync_api import expect

from page_object.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def is_visible(self):
        expect(self.page.get_by_test_id('title')).to_have_text('Your Cart')
        expect(self.page.get_by_test_id('continue-shopping')).to_be_visible()
        expect(self.page.get_by_test_id('checkout')).to_be_visible()
        return True
