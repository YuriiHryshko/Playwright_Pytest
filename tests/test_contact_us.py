import pytest
import os

from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from faker import Faker
from utils.tools import take_screenshot

test_file = "../data/test_file.png"
scriptPath = os.path.abspath(__file__)
filePath = os.path.join(os.path.dirname(scriptPath), '..', 'data', 'test_file.png')

fake = Faker()
name = fake.name()
email = fake.email()
subject = fake.sentence(nb_words=4)
message = fake.text()

class TestContactUsPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_us_page = ContactUsPage(self.page)

    def test_contact_us_form(self, test_setup):
        assert self.page.title() == 'Automation Exercise'

        self.home_page.click_contact_us_btn()
        assert self.contact_us_page.contact_form_title.is_visible()

        self.contact_us_page.fill_contact_us_form(name, email, subject, message)
        self.contact_us_page.upload_file(filePath)
        self.contact_us_page.click_submit_btn()
        self.contact_us_page.click_browser_ok()
        #assert self.contact_us_page.alert_success.is_visible()

        self.home_page.click_home_btn()
        assert self.page.url == 'https://automationexercise.com/'

        take_screenshot(self.page, "Contact Us Form")
