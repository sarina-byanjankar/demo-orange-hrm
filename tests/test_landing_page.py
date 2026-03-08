import pytest

from pages.landing_page import landingpage


@pytest.mark.landing
def test_page_title(page):
    landing_page = landingpage(page)
    expected_title = "Login"
    assert landing_page.verify_page_title(
    ) == expected_title, f"Expected page title to be '{expected_title}'"


@pytest.mark.landing
def test_brand_logo_visibility(page):
    landing_page = landingpage(page)
    assert landing_page.verify_brand_logo(), "Brand logo is not visible"


@pytest.mark.landing
def test_username_field_visibility(page):
    landing_page = landingpage(page)
    assert landing_page.verify_field_username(), "Username field is not visible"


@pytest.mark.landing
def test_password_field_visibility(page):
    landing_page = landingpage(page)
    assert landing_page.verify_field_password(), "Password field is not visible"


@pytest.mark.landing
def test_login_button_visibility(page):
    landing_page = landingpage(page)
    assert landing_page.verify_login_button(), "Login button is not visible"


# @pytest.mark.landing
def test_forgot_password_link_visibility(page):
    landing_page = landingpage(page)
    assert landing_page.verify_forgot_password_link(
    ), "Forgot password link is not visible"
