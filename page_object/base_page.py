import os
from urllib.parse import urljoin


class BasePage:

    def __init__(self, page):
        self.page = page

    @property
    def path(self):
        return '/'

    def navigate(self):
        self.page.goto(urljoin(os.getenv('BASE_URL'), self.path))
