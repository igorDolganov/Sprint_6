from selenium.webdriver.firefox.options import Options
import pytest
from pages.base_page import *
from selenium import webdriver


@pytest.fixture
def setup_driver():
    # Настройка FirefoxOptions
    options = Options()

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
