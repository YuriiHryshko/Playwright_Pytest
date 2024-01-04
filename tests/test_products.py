import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from data.data import Data

product_name = Data.product["name"]

class TestProductsPage:
    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.product_details_page = ProductDetailsPage(self.page)
        self.page.goto('https://automationexercise.com')
        assert self.page.title() == 'Automation Exercise'

        self.home_page.click_products_btn()
        assert self.page.url == 'https://automationexercise.com/products'

    def test_verify_all_products_and_product_detail_page(self, test_setup):
        assert self.products_page.products_list.is_visible()

        self.products_page.click_first_product_view_btn()
        assert self.page.url == 'https://automationexercise.com/product_details/1'

        assert self.product_details_page.product_name.is_visible()
        assert self.product_details_page.product_category.is_visible()
        assert self.product_details_page.product_price.is_visible()
        assert self.product_details_page.product_availability.is_visible()
        assert self.product_details_page.product_condition.is_visible()
        assert self.product_details_page.product_brand.is_visible()

    def test_search_product(self, test_setup):
        self.products_page.search_by_product_name(product_name)
        assert self.products_page.searched_products_title.is_visible()

        self.products_page.check_searched_results_by_name(product_name)





