from locators.main_page_locators import *
from locators.order_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageQuestions:
    @staticmethod
    def click_question1(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_1_button).click()

    @staticmethod
    def click_question2(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_2_button).click()

    @staticmethod
    def click_question3(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_3_button).click()

    @staticmethod
    def click_question4(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_4_button).click()

    @staticmethod
    def click_question5(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_5_button).click()

    @staticmethod
    def click_question6(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_6_button).click()

    @staticmethod
    def click_question7(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_7_button).click()

    @staticmethod
    def click_question8(setup_driver):
        setup_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        setup_driver.find_element(*MainPage.question_8_button).click()

    @staticmethod
    def check_question1(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_1_text).text
        expected_value = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question2(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_2_text).text
        expected_value = ('Пока что у нас так: один заказ — один самокат.'
                          ' Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question3(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_3_text).text
        expected_value = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                          'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                          'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question4(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_4_text).text
        expected_value = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question5(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_5_text).text
        expected_value = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question6(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_6_text).text
        expected_value = ('Самокат приезжает к вам с полной зарядкой. '
                          'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                          'Зарядка не понадобится.')
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question7(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_7_text).text
        expected_value = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                          'Все же свои.')
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_question8(setup_driver):
        actually_value = setup_driver.find_element(*MainPage.question_8_text).text
        expected_value = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actually_value == expected_value, "неверный текст"

    @staticmethod
    def check_yandex_logo_button(setup_driver):
        setup_driver.find_element(*MainPage.yandex_logo).click()
        setup_driver.switch_to.window(setup_driver.window_handles[-1])
        logo_zen = WebDriverWait(setup_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dzen-header"]/div[1]/a')))
        assert logo_zen, 'Неверный URL'
