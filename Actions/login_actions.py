from data.user import User
from page_object.login_form import LoginFrom
from page_object.page_factory import PageFactory
from page_object.products_page import ProductsPage


class Login:

    should_init = True
    page = None
    login_form = None

    @classmethod
    def set_page(cls, page):
        cls.page = page
        cls.login_form = LoginFrom(page)

    @classmethod
    def login_as(cls, user: User) -> ProductsPage:
        cls.login_form.username.fill(user.name)
        cls.login_form.password.fill(user.password)
        cls.login_form.login.click()
        return PageFactory(cls.page)('products')
