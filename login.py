# from playwright.sync_api import sync_playwright


def login(page, username, password):
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    # Add any additional steps or checks after login if necessary
    # print(input("Press Enter to close the browser..."))
