from playwright.sync_api import sync_playwright

from admin_page import goto_admin
from login import login


def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        login(page, "Admin", "admin123")
        goto_admin(page)


if __name__ == "__main__":
    main()
