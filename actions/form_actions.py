class Form:

    should_init = True
    page = None

    def __init__(self, page_object_instance):
        self.page_object_instance = page_object_instance

    @classmethod
    def set_page(cls, page):
        cls.page = page

    def fill_from_table(self, table):
        for row in table:
            self.page_object_instance.get_field_locator_by_pretty_name(
                row['field']).fill(row['value'])
