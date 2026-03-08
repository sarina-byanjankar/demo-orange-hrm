
from pages.login import Login


def test_valid_login(page):
    login = Login(page)
    login.login("admin", "admin123")

    # page = logged_in_page(page)
    assert "dashboard" in page.url


def test_invalid_login(page):
    login = Login(page)
    login.login("invalid_user", "invalid_pass")

    assert "dashboard" not in page.url


def test_empty_string(page):
    login = Login(page)
    login.login("", "")

    assert "dashboard" not in page.url
