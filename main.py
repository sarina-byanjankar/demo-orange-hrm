# from playwright.sync_api import sync_playwright

# from pages.admin_page import goto_admin, search_user
# from pages.login import login


# def main():
#     with sync_playwright() as p:
#         browser = p.firefox.launch(headless=False)
#         page = browser.new_page()

#         login(page, "Admin", "admin123")
#         goto_admin(page)
#         search_user(page, "achun", "Linda Anderson")


# if __name__ == "__main__":
#     main()
