from page_object.base_page import BasePage


class CheckoutOverview(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.finish_btn = page.get_by_test_id('finish')

    def is_visible(self):
        return True

    def access_checkout_complete(self):
        from page_object.page_factory import PageFactory
        self.finish_btn.click()
        return PageFactory(self.page)('checkout complete')
