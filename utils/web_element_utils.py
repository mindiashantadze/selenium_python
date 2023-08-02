class WebElementUtils:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_tuple):
        return self.driver.find_element(locator_tuple[0], locator_tuple[1])

    def find_elements(self, locator_tuple):
        return self.driver.find_elements(locator_tuple[0], locator_tuple[1])

    def find_dynamic_element(self, locator_tuple, dynamic_text):
        return self.driver.find_element(locator_tuple[0], locator_tuple[1].format(dynamic_text))

    def find_child_element(self, parent_element, child_locator_tuple):
        return parent_element.find_element(child_locator_tuple[0], child_locator_tuple[1])

    def find_child_elements(self, parent_element, child_locator_tuple):
        return parent_element.find_elements(child_locator_tuple[0], child_locator_tuple[1])

    def find_dynamic_child_element(self, parent_element, child_locator_tuple, option):
        return parent_element.find_element(child_locator_tuple[0], child_locator_tuple[1].format(option))
