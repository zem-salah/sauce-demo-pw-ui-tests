from actions.login_actions import Login
import pytest


@pytest.fixture(scope='session')
def playwright(playwright):
    playwright.selectors.set_test_id_attribute('data-test')
    yield playwright
    playwright.stop()


@pytest.fixture
def login_actions(page):
    Login.set_page(page)
    yield Login
    page.close()
