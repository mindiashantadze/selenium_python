from selenium.webdriver.common.by import By

from utils.web_element_utils import WebElementUtils
from pages.BasePage import BasePage


class ProductListingPage(BasePage):
    DIV_RESULTS = (By.CLASS_NAME, "srp-river-results")

    DIV_PRODUCT_INFOs = (By.CLASS_NAME, "s-item__info")
    LBL_PRODUCT_TITLE = (By.CLASS_NAME, "s-item__title")
    LBL_PRODUCT_PRICE = (By.CLASS_NAME, "s-item__price")
    LBL_PRODUCT_SHIPPING_PRICE = (By.CLASS_NAME, "s-item__shipping")
    BTN_SAVE_SEARCH_LINK = (By.CLASS_NAME, "faux-link")
    LBL_NO_RESULT = (By.CLASS_NAME, "srp-save-null-search__heading")

    BTN_CATEGORY = (By.XPATH, "//div[@class='srp-rail__left']//span[text() = '{}']")
    BTN_SORT = (By.XPATH, "//button[@aria-label='Sort selector. Best Match selected.']")
    BTN_SORT_OPTION = (By.XPATH, "//span[text() = '{}']")

    def __init__(self, driver):
        super().__init__(driver)
        self.utils = WebElementUtils(driver)

    def get_product_titles(self):
        div_results = self.utils.find_element(self.DIV_RESULTS)
        lbl_product_titles = self.utils.find_child_elements(div_results, self.LBL_PRODUCT_TITLE)

        for lbl_product_title in lbl_product_titles:
            print(lbl_product_title.text)

        return lbl_product_titles

    def get_product_shipping_prices(self):
        div_results = self.utils.find_element(self.DIV_RESULTS)
        lbl_product_shipping_prices = self.utils.find_child_elements(div_results, self.LBL_PRODUCT_SHIPPING_PRICE)

        for lbl_product_title in lbl_product_shipping_prices:
            print(lbl_product_title.text)

        return lbl_product_shipping_prices

    def get_product_prices(self):
        div_results = self.utils.find_element(self.DIV_RESULTS)
        lbl_product_prices = self.utils.find_child_elements(div_results, self.LBL_PRODUCT_PRICE)

        for lbl_product_title in lbl_product_prices:
            print(lbl_product_title.text)

        return lbl_product_prices

    def click_save_search_link(self):
        self.utils.find_element(self.BTN_SAVE_SEARCH_LINK).click()

    def get_no_result_lbl(self):
        return self.utils.find_element(self.LBL_NO_RESULT)

    def select_category(self, category_name):
        self.utils.find_dynamic_element(self.BTN_CATEGORY, category_name).click()

    def sort_products(self, option):
        sort_button = self.utils.find_element(self.BTN_SORT)
        sort_button.click()
        self.utils.find_dynamic_child_element(sort_button, self.BTN_SORT_OPTION, option).click()
