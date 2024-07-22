from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from Actions import init_actions_module
from Assertion import init_assertions_module


def before_all(context):
    # load key-value pairs from .env file and set them as env variables
    load_dotenv()
    context.pw = sync_playwright().start()
    context.pw.selectors.set_test_id_attribute('data-test')


def before_scenario(context, scenario):
    context.browser = context.pw.chromium.launch(
        headless=False, channel="chrome")
    context.page = context.browser.new_page()
    init_actions_module(context)
    init_assertions_module(context)


def after_scenario(context, scenario):
    context.browser.close()
