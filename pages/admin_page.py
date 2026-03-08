class AdminPage:
    def __init__(self, page):
        self.page = page

    def goto_admin(self, page):
        page.click(".oxd-main-menu-item-wrapper:has-text('Admin')")

    def search_user(self, page, username, employee_name):
        page.fill(".oxd-input.oxd-input--active", username)
        page.type(
            ".oxd-autocomplete-text-input.oxd-autocomplete-text-input--active", employee_name)
        page.click("button:has-text('Search')")

        # input("Press Enter to close the browser...")

    # def add_user(self, page):
    #     page.click("button:has-text('Add')")

    # def check_records(self, page):
    #     # Implement logic to check records in the admin page
    #     pass
