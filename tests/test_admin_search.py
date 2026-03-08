"""Tests for admin search functionality."""
from pages.admin_page import AdminPage
from pages.login import Login


def test_goto_admin(logged_in_page):
    page = logged_in_page
    page.click("text=Admin")


def test_search_user(logged_in_page):
    page = logged_in_page
    admin_page = AdminPage(page)
    admin_page.goto_admin(page)
    admin_page.search_user(page, "Admin", "Admin")
    expect(page.locator(".oxd-table-card").first).to_be_visible()

    # assert page.locator(".oxd-table-card").is_visible()
