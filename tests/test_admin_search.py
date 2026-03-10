import pytest

"""Tests for admin search functionality."""
from conftest import page
from pages.admin_page import AdminPage
from pages.login import Login


# @pytest.mark.adminpage
# def test_goto_admin(logged_in_page):
#     admin_page = AdminPage(logged_in_page)
#     admin_page.goto_admin()

#     assert "/web/index.php/admin/viewSystemUsers" in logged_in_page.url


@pytest.mark.adminpage2
def test_search_user(logged_in_page):
    admin_page = AdminPage(logged_in_page)
    admin_page.goto_admin()

    admin_page.search_user("Michael Tomlinson user")
    assert admin_page.results_table.count() > 0
