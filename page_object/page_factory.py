from page_object.login_form import LoginFrom
from page_object.products_page import ProductsPage


class PageFactory:

    def __init__(self, page):
        self._page = page

    def __call__(self, page_name):
        page_name_to_creation_function = {
            'login': self._create_login_page,
            'products': self._create_products_page,
        }
        page_method = page_name_to_creation_function.get(page_name)
        if page_method:
            return page_method()
        else:
            raise ValueError(f"Page {page_name} not found")

    def _create_login_page(self):
        return LoginFrom(self._page)

    def _create_products_page(self):
        return ProductsPage(self._page)
