from playwright.sync_api import Page

class DeleteAccountPage():
    def __init__(self, page: Page):
        self.page = page
        self.continue_btn = self.page.locator('a[data-qa="continue-button"]')
        self.account_deleted_title = self.page.locator('h2[data-qa="account-deleted"]')

    def click_continue_btn(self):
        self.continue_btn.click()