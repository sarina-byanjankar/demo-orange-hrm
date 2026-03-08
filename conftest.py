import pytest
from playwright.sync_api import sync_playwright
from pages.login import Login
from utils.config import BASE_URL, USERNAME, PASSWORD


# making the follwoing function a fixture so that it can be used in the test functions, it will be automatically called
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        # page.goto(
        #     "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="networkidle")
        page.goto
        yield page  # This will where setup ends and test begins
        browser.close()


@pytest.fixture  # this will be used to avoid repeating login in every test
def logged_in_page(page):
    login = Login(page)
    login.login(USERNAME, PASSWORD)
    return page
