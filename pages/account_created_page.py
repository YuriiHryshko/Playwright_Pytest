from playwright.sync_api import Page

class AccountCreatedPage():
    def __init__(self, page: Page):
        self.page = page
        self.account_created_title = self.page.locator('h2[data-qa="account-created"]')
        self.continue_btn = self.page.locator('[data-qa="continue-button"]')

    def click_continue_btn(self):
        self.continue_btn.click()