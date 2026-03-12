import pytest
from utils.data_reader import get_login_data
from conftest import logger

from pages.login import Login
# from utils.config import TIMEOUT


@pytest.mark.parametrize("username,password", get_login_data())
def test_login_with_csv(page, username, password):
    login = Login(page)
    logger.info(
        f"Testing login with username: {username} and password: {password}")
    login.login(username, password)

    if username == "admin" and password == "admin123":
        assert "dashboard" in page.url
    else:
        assert "dashboard" not in page.url

# def test_valid_login(page):
#     login = Login(page)

#     logger.info("Testing valid login with correct credentials")
#     login.login("admin", "admin123")
#     assert "dashboard" in page.url


# def test_invalid_login(page):
#     login = Login(page)
#     logger.info("Testing invalid login with incorrect credentials")
#     login.login("invalid_user", "invalid_pass")

#     assert "dashboard" not in page.url


# def test_empty_string(page):
#     login = Login(page)
#     logger.info("Testing login with empty username and password")
#     login.login("", "")
# # sample comment
#     assert "dashboard" not in page.url
