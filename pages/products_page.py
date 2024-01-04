from playwright.sync_api import Page

class ProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.products_list = self.page.locator('.features_items')
        self.first_product_view_btn = self.page.locator('.nav-justified')
        self.search_product_field = self.page.locator('#search_product')
        self.search_btn = self.page.locator('#submit_search')
        self.searched_products_title = self.page.locator('.features_items>h2')
        self.searched_products_names = self.page.locator('.productinfo>p')

    def click_first_product_view_btn(self):
        self.first_product_view_btn.first.click()

    def search_by_product_name(self, product_name):
        self.search_product_field.fill(product_name)
        self.search_btn.click()

    def check_searched_results_by_name(self, product_name):
        results = self.searched_products_names.all_inner_texts()
        assert all(product_name in result for result in results)
