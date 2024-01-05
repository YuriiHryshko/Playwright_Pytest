import pytest
import random

from pages.home_page import HomePage
from pages.login_signup_page import LoginSignupPage
from pages.registration_page import RegistrationPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from data.data import Data
from utils.tools import take_screenshot

name = Data.user["name"]
email = Data.user["email"]
gender = random.randint(1, 2)
password = Data.user["password"]
birthday = Data.user["birthday"]
birth_month = Data.user["birth_month"]
birth_year = Data.user["birth_year"]
firstname = Data.user["first_name"]
last_name = Data.user["last_name"]
company = Data.user["company"]
address = Data.user["address1"]
address2 = Data.user["address2"]
country = Data.user["country"]
state = Data.user["state"]
city = Data.user["city"]
zipcode = Data.user["zipcode"]
mobile = Data.user["mobile_number"]

registered_email = Data.registered_user["email"]
registered_password = Data.registered_user["password"]
registered_name = Data.registered_user["name"]



class TestLoginSignupPage:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.login_signup_page = LoginSignupPage(self.page)
        self.registration_page = RegistrationPage(self.page)
        self.account_created_page = AccountCreatedPage(self.page)
        self.account_deleted_page = DeleteAccountPage(self.page)
        assert self.page.title() == 'Automation Exercise'

    def test_register_user(self, test_setup):
        self.home_page.click_login_btn()
        assert self.login_signup_page.signup_form_header.is_visible()

        self.login_signup_page.fill_signup_form(name, email)
        self.login_signup_page.click_signup_btn()
        assert self.registration_page.form_headers.first.is_visible()

        self.registration_page.fill_account_info_form(gender, password, birthday, birth_month, birth_year)
        self.registration_page.select_newsletter_checkbox()
        self.registration_page.select_offers_checkbox()
        self.registration_page.fill_address_info_form(firstname, last_name, company, address, address2, country, state, city, zipcode, mobile)
        self.registration_page.click_create_account_btn()
        assert self.account_created_page.account_created_title.is_visible()

        self.account_created_page.click_continue_btn()
        assert self.home_page.logged_in_username.is_visible()
        assert name in self.home_page.logged_in_username.inner_text()

        self.home_page.click_delete_account_btn()
        assert self.account_deleted_page.account_deleted_title.is_visible()

        self.account_deleted_page.click_continue_btn()

        take_screenshot(self.page, "Register User")
    def test_login_user_with_correct_email_and_password(self, test_setup):
        self.home_page.click_login_btn()
        assert self.login_signup_page.login_form_header.is_visible()

        self.login_signup_page.fill_login_form(registered_email, registered_password)
        self.login_signup_page.click_login_btn()
        assert self.home_page.logged_in_username.is_visible()
        assert registered_name in self.home_page.logged_in_username.inner_text()

        #self.home_page.click_delete_account_btn()
        #assert self.account_deleted_page.account_deleted_title.is_visible()

        take_screenshot(self.page, "Login User with correct email and password")
    def test_login_user_with_incorrect_email_and_password(self, test_setup):
        self.home_page.click_login_btn()
        assert self.login_signup_page.login_form_header.is_visible()

        self.login_signup_page.fill_login_form(email, password)
        self.login_signup_page.click_login_btn()
        assert self.login_signup_page.login_form_error.is_visible()

        take_screenshot(self.page, "Login User with incorrect email and password")

    def test_logout_user(self, test_setup):
        self.home_page.click_login_btn()
        assert self.login_signup_page.login_form_header.is_visible()

        self.login_signup_page.fill_login_form(registered_email, registered_password)
        self.login_signup_page.click_login_btn()
        assert self.home_page.logged_in_username.is_visible()
        assert registered_name in self.home_page.logged_in_username.inner_text()

        self.home_page.click_logout_btn()
        assert self.page.url == 'https://automationexercise.com/login'

        take_screenshot(self.page, "Logout User")

    def test_register_user_with_existing_email(self, test_setup):
        self.home_page.click_login_btn()
        assert self.login_signup_page.signup_form_header.is_visible()

        self.login_signup_page.fill_signup_form(name, registered_email)
        self.login_signup_page.click_signup_btn()
        assert self.login_signup_page.signup_form_error.is_visible()

        take_screenshot(self.page, "Register User with existing email")



