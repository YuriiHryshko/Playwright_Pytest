from playwright.sync_api import Page

class TestCasesPage():
    def __init__(self, page: Page):
        self.page = page
        self.contact_form_title = self.page.locator('.contact-form>h2.title')

