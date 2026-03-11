import pytest
import logging

from playwright.sync_api import Page, sync_playwright
from pages.login import Login
from utils.config import BASE_URL, USERNAME, PASSWORD

# making the follwoing function a fixture so that it can be used in the test functions, it will be automatically called


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        # page.goto("www.example.com", wait_until="networkidle")
        page.goto(BASE_URL, wait_until="networkidle")
        yield page  # This will where setup ends and test begins

        # teardown code will be executed after the test is done, it will close the browser
        browser.close()


@pytest.fixture  # this will be used to avoid repeating login in every test
def logged_in_page(page):
    login = Login(page)
    login.login(USERNAME, PASSWORD)
    return page


# Loggin the activities
logging.basicConfig(
    filename='test_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Taking the screenshot on failure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        page = item.funcargs['page']
        screenshot_path = f"screenshots/{item.name}.png"
        page.screenshot(path=screenshot_path)
        logger.info(f"Screenshot taken for failed test: {item.name}")
