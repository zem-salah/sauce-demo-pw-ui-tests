from data.products import Product
from page_object.page_factory import PageFactory


class Products:

    should_init = True
    page = None
    product_page = None

    @classmethod
    def set_page(cls, page):
        cls.page = page
        cls.product_page = PageFactory(cls.page)('products')

    @classmethod
    def add_to_cart(cls, product: Product):
        cls.product_page.add_product_to_cart(product.name)
