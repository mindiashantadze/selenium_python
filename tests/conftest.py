import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()

