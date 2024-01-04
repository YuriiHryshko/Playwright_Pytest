from playwright.sync_api import Page

class RegistrationPage():
    def __init__(self, page: Page):
        self.page = page
        self.form_headers = self.page.locator('h2.title')
        self.mr_radio_btn = self.page.locator('#id_gender1')
        self.mrs_radio_btn = self.page.locator('#id_gender2')
        self.password_field = self.page.locator('#password')
        self.day_select = self.page.locator('#days')
        self.month_select = self.page.locator('#months')
        self.year_select = self.page.locator('#years')
        self.news_checkbox = self.page.locator('#newsletter')
        self.offers_checkbox = self.page.locator('#optin')
        self.first_name_field = self.page.locator('#first_name')
        self.last_name_field = self.page.locator('#last_name')
        self.company_field = self.page.locator('#company')
        self.address1_field = self.page.locator('#address1')
        self.address2_field = self.page.locator('#address2')
        self.country_select = self.page.locator('#country')
        self.state_field = self.page.locator('#state')
        self.city_field = self.page.locator('#city')
        self.zipcode_field = self.page.locator('#zipcode')
        self.mobile_number_field = self.page.locator('#mobile_number')
        self.create_account_btn = self.page.locator('button[data-qa="create-account"]')

    def fill_account_info_form(self, gender, password, day, month, year):
        if gender == 1:
            self.mr_radio_btn.check()
        else:
            self.mrs_radio_btn.check()
        self.password_field.fill(password)
        self.day_select.select_option(day)
        self.month_select.select_option(month)
        self.year_select.select_option(year)

    def fill_address_info_form(self, firstname, lastname, company, address, address2, country, state, city, zipcode, mobile):
        self.first_name_field.fill(firstname)
        self.last_name_field.fill(lastname)
        self.company_field.fill(company)
        self.address1_field.fill(address)
        self.address2_field.fill(address2)
        self.country_select.select_option(country)
        self.state_field.fill(state)
        self.city_field.fill(city)
        self.zipcode_field.fill(zipcode)
        self.mobile_number_field.fill(mobile)

    def select_newsletter_checkbox(self):
        self.news_checkbox.check()

    def select_offers_checkbox(self):
        self.offers_checkbox.check()

    def click_create_account_btn(self):
        self.create_account_btn.click()