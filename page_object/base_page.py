import os
from urllib.parse import urljoin


class BasePage:

    def __init__(self, page):
        self.page = page

    @property
    def path(self):
        return '/'

    def navigate(self):
        # wait_until commit decreased execution time from 1.19s to 700ms
        self.page.goto(urljoin(os.getenv('BASE_URL'), self.path),
                       wait_until='commit')
