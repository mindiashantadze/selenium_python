from config.TestData import TestData


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(TestData.BASE_URL)
