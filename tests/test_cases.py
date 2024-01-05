import pytest

from pages.home_page import HomePage
from utils.tools import take_screenshot

class TestCasesPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        assert self.page.title() == 'Automation Exercise'

        self.home_page.click_test_cases_btn()
        assert self.page.url == 'https://automationexercise.com/test_cases'

        take_screenshot(self.page, "Verify Test Cases Page")

