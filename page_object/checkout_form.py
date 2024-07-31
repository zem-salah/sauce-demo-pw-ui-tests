from page_object.base_page import BasePage


class CheckoutForm(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page_elements_pretty_name_to_locator = {
            'first name': page.get_by_test_id('firstName'),
            'last name': page.get_by_test_id('lastName'),
            'postal code': page.get_by_test_id('postalCode'),
            'continue': page.get_by_test_id('continue'),
        }

    def is_visible(self):
        return True
