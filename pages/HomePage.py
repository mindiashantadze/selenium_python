from selenium.webdriver.common.by import By

from utils.web_element_utils import WebElementUtils
from pages.BasePage import BasePage


class HomePage(BasePage):
    INPT_SEARCH = (By.ID, "gh-ac")
    BTN_SEARCH_PRODUCTS = (By.ID, "gh-btn")
    INPT_CATEGORIES_DROPDOWN = (By.ID, "gh-cat-box")
    BTN_ADVANCED_SEARCH = (By.ID, "gh-as-a")
    BTN_CATEGORY_OPTION = (By.XPATH, "//select[@id = 'gh-cat']/option[text() = '{}']")

    def __init__(self, driver):
        super().__init__(driver)
        self.utils = WebElementUtils(self.driver)

    def type_in_search_field(self, text):
        self.utils.find_element(self.INPT_SEARCH).send_keys(text)

    def click_search_button(self):
        self.utils.find_element(self.BTN_SEARCH_PRODUCTS).click()

    def select_category(self, category_name):
        self.utils.find_element(self.INPT_CATEGORIES_DROPDOWN).click()
        self.utils.find_dynamic_element(self.BTN_CATEGORY_OPTION, category_name).click()
