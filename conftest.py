import pytest
from locators.base_urls import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def setup_driver():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
