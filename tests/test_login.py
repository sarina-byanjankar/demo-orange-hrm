
from conftest import logger

from pages.login import Login
from utils.config import TIMEOUT


def test_valid_login(page):
    login = Login(page)

    logger.info("Testing valid login with correct credentials")
    login.login("admin", "admin123")

    # page = logged_in_page(page)
    assert "dashboard" in page.url


def test_invalid_login(page):
    login = Login(page)
    logger.info("Testing invalid login with incorrect credentials")
    login.login("invalid_user", "invalid_pass")

    assert "dashboard" not in page.url


def test_empty_string(page):
    login = Login(page)
    logger.info("Testing login with empty username and password")
    login.login("", "")

    assert "dashboard" not in page.url
