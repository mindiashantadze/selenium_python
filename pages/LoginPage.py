from  selenium.webdriver.common.by import By

from utils.web_element_utils import WebElementUtils

from pages.BasePage import BasePage


class LoginPage(BasePage):
    LBL_GREETING_MSG = (By.ID, "greeting-msg")

    def __init__(self, driver):
        super().__init__(driver)
        self.utils = WebElementUtils(self.driver)

    def get_greeting_lbl(self):
        return self.utils.find_element(self.LBL_GREETING_MSG)
