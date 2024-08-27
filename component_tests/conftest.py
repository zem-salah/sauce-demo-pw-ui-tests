from actions.login_actions import Login

import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def pw_browser():
    with sync_playwright() as pw:
        pw.selectors.set_test_id_attribute('data-test')
        browser = pw.chromium.launch(headless=False)
        yield browser


@pytest.fixture
def login_actions(pw_browser):
    page = pw_browser.new_page()
    Login.set_page(page)
    yield Login
