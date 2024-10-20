from locators.main_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_questions import *
from conftest import setup_driver

class MainPageQuestions:

    def __init__(self, setup_driver):
        self.driver = setup_driver

    def click_question(self, button):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*button).click()

    def check_question(self, text_locator, expected):
        actually_value = self.driver.find_element(*text_locator).text
        assert actually_value == expected, f"неверный текст"


    def check_yandex_logo_button(self):
        self.driver.find_element(*MainPage.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logo_zen = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*MainPage.logo_dzen))
        assert logo_zen, 'Неверный URL'
