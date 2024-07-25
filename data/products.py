class Product:

    _translate = {
        "Sauce Labs Backpack": "sauce-labs-backpack"
    }

    def __init__(self, product_pretty_name):
        self.name = product_pretty_name

    @classmethod
    def get_locator_value(cls, product_name):
        try:
            return cls._translate[product_name]
        except KeyError:
            raise KeyError(
                f'Product {product_name} does not exist.'
            )
