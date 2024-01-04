from playwright.sync_api import Page

class LoginSignupPage():
    def __init__(self, page: Page):
        self.page = page
        self.signup_form_header = self.page.locator('.signup-form>h2')
        self.signup_name_field = self.page.locator('input[data-qa="signup-name"]')
        self.signup_email_field = self.page.locator('input[data-qa="signup-email"]')
        self.signup_btn = self.page.locator('button[data-qa="signup-button"]')
        self.signup_form_error = self.page.locator('form[action="/signup"]>p')
        self.login_form_header = self.page.locator('.login-form>h2')
        self.login_email_field = self.page.locator('input[data-qa="login-email"]')
        self.login_password_field = self.page.locator('input[data-qa="login-password"]')
        self.login_btn = self.page.locator('button[data-qa="login-button"]')
        self.login_form_error = self.page.locator('form[action="/login"]>p')

    def click_signup_btn(self):
        self.signup_btn.click()

    def click_login_btn(self):
        self.login_btn.click()

    def fill_signup_form(self, name, email):
        self.signup_name_field.fill(name)
        self.signup_email_field.fill(email)

    def fill_login_form(self, email, password):
        self.login_email_field.fill(email)
        self.login_password_field.fill(password)