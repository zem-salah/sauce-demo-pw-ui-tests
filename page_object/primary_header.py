from page_object.base_page import BasePage


class PrimaryHeader(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_badge = page.get_by_test_id('shopping-cart-badge')
