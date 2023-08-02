from pages.LoginPage import LoginPage
from tests.test_base import BaseTest

from pages.HomePage import HomePage
from pages.ProductListingPage import ProductListingPage


class TestMain(BaseTest):
    SIGNIN_PAGE_MSG = "Sign in to eBay or create an account"
    PRODUCT_NOT_FOUND_MSG = "No exact matches found"

    SEARCH_DATA = "Ball"
    NON_EXISTENT_PRODUCT = "somenonexistingproduct"
    CATEGORY_SEARCH_DATA = "Golf Balls"
    FREE_INTERNATIONAL_SHIPPING = "Free International Shipping"

    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.SEARCH_DATA)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        for element in product_listing_page.get_product_titles():
            assert self.SEARCH_DATA.lower() in element.text.lower(), "Element does not contain word" + self.SEARCH_DATA

    def test_save_search(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.SEARCH_DATA)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.click_save_search_link()
        login_page = LoginPage(self.driver)
        assert login_page.get_greeting_lbl().text == "Hello"

    def test_no_results(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.NON_EXISTENT_PRODUCT)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        no_result_lbl = product_listing_page.get_no_result_lbl().text
        assert no_result_lbl == self.PRODUCT_NOT_FOUND_MSG

    def test_category(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.SEARCH_DATA)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.select_category(self.CATEGORY_SEARCH_DATA)
        for lbl_product_title in product_listing_page.get_product_titles():
            assert self.CATEGORY_SEARCH_DATA in lbl_product_title.text

    def test_free_shipping(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.SEARCH_DATA)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.select_category(self.FREE_INTERNATIONAL_SHIPPING)
        for shipping_price in product_listing_page.get_product_shipping_prices():
            assert shipping_price.text == self.FREE_INTERNATIONAL_SHIPPING

    def test_sort_by_price(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.type_in_search_field(self.SEARCH_DATA)
        home_page.click_search_button()
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.sort_products("Price + Shipping: lowest first")
        lbl_product_prices = product_listing_page.get_product_prices()
        for i in range(0, len(lbl_product_prices)):
            if i > len(lbl_product_prices):
                print("Iteration finished")
            else:
                lbl_price = lbl_product_prices[i]
                lbl_next_price = lbl_product_prices[i + 1]
                price = lbl_price.text.strip().replace("$", "")
                next_price = lbl_next_price.text.strip().replace("$", "")
                if price == next_price:
                    continue
                assert float(next_price) >= float(price)






