from playwright.sync_api import sync_playwright


class Login:
    def __init__(self, page):
        self.page = page
        # 'self.username_input = page.locator("input[name=\'username\']")'

    def login(self, username, password):
        # self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.fill("input[name='username']", username)
        s
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        # Add any additional steps or checks after login if necessary
        # print(input("Press Enter to close the browser..."))
