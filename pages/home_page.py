from playwright.sync_api import Page

class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.login_nav_btn = self.page.locator('a[href="/login"]')
        self.delete_account_nav_btn = self.page.locator('a[href="/delete_account"]')
        self.logged_in_username = self.page.locator('li>a>b')
        self.logout_nav_btn = self.page.locator('a[href="/logout"]')
        self.contact_us_nav_btn = self.page.locator('a[href="/contact_us"]')
        self.home_nav_btn = self.page.locator('ul>li>a[href="/"]')
        self.test_cases_nav_btn = self.page.locator('ul>li>a[href="/test_cases"]')
        self.products_nav_btn = self.page.locator('ul>li>a[href="/products"]')
        self.subscription_title = self.page.locator('.single-widget>h2')
        self.subscription_field = self.page.locator('#susbscribe_email')
        self.subscription_btn = self.page.locator('#subscribe')
        self.success_subscribe_alert = self.page.locator('#success-subscribe>.alert-success')


    def click_login_btn(self):
        self.login_nav_btn.click()

    def click_delete_account_btn(self):
        self.delete_account_nav_btn.click()

    def click_logout_btn(self):
        self.logout_nav_btn.click()

    def click_contact_us_btn(self):
        self.contact_us_nav_btn.click()

    def click_home_btn(self):
        self.home_nav_btn.click()

    def click_test_cases_btn(self):
        self.test_cases_nav_btn.click()

    def click_products_btn(self):
        self.products_nav_btn.click()

    def fill_subscription_field(self, email):
        self.subscription_field.fill(email)
        self.subscription_btn.click()