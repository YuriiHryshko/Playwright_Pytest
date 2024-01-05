from playwright.sync_api import Page

class ContactUsPage():
    def __init__(self, page: Page):
        self.page = page
        self.contact_form_title = self.page.locator('.contact-form>h2.title')
        self.name_field = self.page.locator('input[data-qa="name"]')
        self.email_field = self.page.locator('input[data-qa="email"]')
        self.subject_field = self.page.locator('input[data-qa="subject"]')
        self.message_field = self.page.locator('#message')
        self.choose_file_input = self.page.locator('input[name="upload_file"]')
        self.submit_btn = self.page.locator('input[data-qa="submit-button"]')
        self.alert_success = self.page.locator('.status.alert.alert-success')

    def fill_contact_us_form(self, name, email, subject, message):
        self.name_field.fill(name)
        self.email_field.fill(email)
        self.subject_field.fill(subject)
        self.message_field.fill(message)

    def upload_file(self, file):
        self.choose_file_input.set_input_files(file)

    def click_submit_btn(self):
        self.submit_btn.click()

    def click_browser_ok(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

