from page_object.base_page import BasePage
from page_object.checkout_overview import CheckoutOverview


class CheckoutForm(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.continue_btn = page.get_by_test_id('continue')
        self.first_name = page.get_by_test_id('firstName')
        self.last_name = page.get_by_test_id('lastName')
        self.postal_code = page.get_by_test_id('postalCode')
        self.page_elements_pretty_name_to_locator = {
            'first name': self.first_name,
            'last name': self.last_name,
            'postal code': self.postal_code,
            'continue': self.continue_btn,
        }

    def access_checkout_overview(self) -> CheckoutOverview:
        from page_object.page_factory import PageFactory
        self.continue_btn.click()
        return PageFactory(self.page)('checkout overview')

    def is_visible(self):
        return True
