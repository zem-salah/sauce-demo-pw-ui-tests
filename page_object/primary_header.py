from page_object.base_page import BasePage


class PrimaryHeader(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_badge = page.get_by_test_id('shopping-cart-badge')
        self.cart_link = page.get_by_test_id('shopping-cart-link')

    def access_cart(self):
        from page_object.page_factory import PageFactory
        self.cart_link.click()
        return PageFactory(self.page)('shopping cart')
