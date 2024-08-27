from data.user import User
from page_object.base_page import BasePage


class LoginFrom(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_test_id('username')
        self.password = page.get_by_test_id('password')
        self.login = page.get_by_test_id('login-button')
        self.locked_out_user_error = page.get_by_test_id('error').filter(
            has_text='this user has been locked out')
        self.user_name_is_required_error = page.get_by_test_id('error').filter(
            has_text='username is required')

    def fill_user_password(self, user: User):
        self.password.fill(user.password)
