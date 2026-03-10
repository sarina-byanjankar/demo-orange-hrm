
from utils.config import TIMEOUT


class landingpage:
    def __init__(self, page):
        self.page = page
        self.brand_logo = self.page.locator(
            ".orangehrm-login-branding")
        self.brand_logo.wait_for(state="visible", timeout=TIMEOUT)
        self.page_title = self.page.locator(
            "h5.oxd-text")
        self.page_title.wait_for(state="visible", timeout=TIMEOUT)
        self.username_field = self.page.locator(
            "input[name='username']")

    def verify_brand_logo(self):
        return self.brand_logo.is_visible()

    def verify_page_title(self):
        return self.page_title.is_visible()

    def verify_field_username(self):

        self.username_field.wait_for(state="visible", timeout=TIMEOUT)
        return self.username_field.is_visible()

    def verify_field_password(self):
        self.password_field = self.page.locator(
            "input[name='password']")
        self.password_field.wait_for(state="visible", timeout=TIMEOUT)
        return self.password_field.is_visible()

    def verify_login_button(self):
        self.login_button = self.page.locator(
            "button[type='submit']")
        self.login_button.wait_for(state="visible", timeout=TIMEOUT)
        return self.login_button.is_visible()

    def verify_forgot_password_link(self):
        self.forgot_password_link = self.page.locator(
            ".orangehrm-login-forgot")
        self.forgot_password_link.wait_for(state="visible", timeout=TIMEOUT)
        return self.forgot_password_link.is_visible()
