class Product:

    def __init__(self, product_pretty_name):
        self.name = product_pretty_name

    _translate = {
        "Sauce Labs Backpack": "sauce-labs-backpack"
    }

    def get_product_locator_value(self):
        try:
            return self._translate[self.name]
        except KeyError:
            raise KeyError(
                f'Product {self.name} does not exist.'
            )
