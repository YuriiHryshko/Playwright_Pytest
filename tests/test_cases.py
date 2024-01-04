import pytest

from pages.home_page import HomePage

class TestCasesPage:
    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.home_page = HomePage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        self.page.goto('https://automationexercise.com')
        assert self.page.title() == 'Automation Exercise'

        self.home_page.click_test_cases_btn()
        assert self.page.url == 'https://automationexercise.com/test_cases'


