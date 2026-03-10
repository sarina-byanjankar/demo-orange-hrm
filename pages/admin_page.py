from playwright.sync_api import expect


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = page.locator(
            ".oxd-main-menu-item-wrapper:has-text('Admin')")
        # self.username_input = page.locator(".data-v-957b4417=")
        self.employee_name_input = page.locator(
            "input[placeholder='Type for hints...']"
        )
        self.search_button = page.locator("button:has-text('Search')")
        self.results_table = page.locator(".oxd-table-card")
        # self.add_button = page.locator("button:has-text('Add')")  # for future

    def goto_admin(self):
        self.admin_menu.click()
        expect(self.page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    def search_user(self, employee_name):
        # self.username_input.fill(username)
        self.employee_name_input.fill(employee_name)
        self.search_button.click()

        # Wait for results to load
        first_row = self.results_table.first
        first_row.wait_for(state="visible", timeout=5000)
