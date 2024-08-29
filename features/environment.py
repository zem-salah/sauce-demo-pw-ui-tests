import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from actions import init_actions_module
from Assertion import init_assertions_module


def after_step(context, step):
    if step.status == 'failed':
        context.page.screenshot(path="screenshot.png", full_page=True)


def before_all(context):
    # load key-value pairs from .env file and set them as env variables
    load_dotenv()
    assert os.getenv('BASE_URL'), "BASE_URL env variable not set"
    context.pw = sync_playwright().start()
    context.pw.selectors.set_test_id_attribute('data-test')


def before_scenario(context, scenario):
    context.browser = context.pw.chromium.launch(
        headless=False, channel="chrome")
    context.page = context.browser.new_context(base_url=os.getenv('BASE_URL'))\
        .new_page()
    init_actions_module(context.page)
    init_assertions_module(context)


def after_scenario(context, scenario):
    context.browser.close()
