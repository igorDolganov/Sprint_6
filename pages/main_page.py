from conftest import setup_driver
from locators.main_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageQuestions:

    def __init__(self, setup_driver):
        self.driver = setup_driver

    def click_question1(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_1_button).click()

    def click_question2(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_2_button).click()

    def click_question3(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_3_button).click()

    def click_question4(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_4_button).click()

    def click_question5(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_5_button).click()

    def click_question6(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_6_button).click()

    def click_question7(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_7_button).click()

    def click_question8(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(*MainPage.question_8_button).click()

    def check_question1(self):
        actually_value = self.driver.find_element(*MainPage.question_1_text).text
        expected_value = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_value == expected_value, "неверный текст"

    def check_question2(self):
        actually_value = self.driver.find_element(*MainPage.question_2_text).text
        expected_value = ('Пока что у нас так: один заказ — один самокат.'
                          ' Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
        assert actually_value == expected_value, "неверный текст"

    def check_question3(self):
        actually_value = self.driver.find_element(*MainPage.question_3_text).text
        expected_value = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                          'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                          'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
        assert actually_value == expected_value, "неверный текст"

    def check_question4(self):
        actually_value = self.driver.find_element(*MainPage.question_4_text).text
        expected_value = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actually_value == expected_value, "неверный текст"

    def check_question5(self):
        actually_value = self.driver.find_element(*MainPage.question_5_text).text
        expected_value = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert actually_value == expected_value, "неверный текст"

    def check_question6(self):
        actually_value = self.driver.find_element(*MainPage.question_6_text).text
        expected_value = ('Самокат приезжает к вам с полной зарядкой. '
                          'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                          'Зарядка не понадобится.')
        assert actually_value == expected_value, "неверный текст"

    def check_question7(self):
        actually_value = self.driver.find_element(*MainPage.question_7_text).text
        expected_value = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                          'Все же свои.')
        assert actually_value == expected_value, "неверный текст"

    def check_question8(self):
        actually_value = self.driver.find_element(*MainPage.question_8_text).text
        expected_value = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actually_value == expected_value, "неверный текст"

    def check_yandex_logo_button(self):
        self.driver.find_element(*MainPage.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logo_zen = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*MainPage.logo_dzen))
        assert logo_zen, 'Неверный URL'
