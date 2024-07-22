from page_object.base_page import BasePage


class LoginFrom(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_test_id('username')
        self.password = page.get_by_test_id('password')
        self.login = page.get_by_test_id('login-button')
