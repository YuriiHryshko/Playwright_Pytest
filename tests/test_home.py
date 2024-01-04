import pytest

from pages.home_page import HomePage
from faker import Faker

fake = Faker()

email = fake.email()

class TestHomePage:
    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.home_page = HomePage(self.page)
        self.page.goto('https://automationexercise.com')
        assert self.page.title() == 'Automation Exercise'

    def test_verify_subscription_in_home_page(self, test_setup):
        assert self.home_page.subscription_title.inner_text() == 'SUBSCRIPTION'
        self.home_page.fill_subscription_field(email)

        assert self.home_page.success_subscribe_alert.is_visible()



