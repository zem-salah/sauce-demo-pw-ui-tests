from page_object.base_page import BasePage


class CheckoutOverview(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def is_visible(self):
        return True
