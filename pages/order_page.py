import pytest
from locators.order_page_locators import *
from locators.main_page_locators import *
from pages.base_page import base_url


class Orders:

    @staticmethod
    def click_samokat_button(setup_driver):
        setup_driver.find_element(*OrderLocators.samokat_button).click()

    @staticmethod
    def check_current_url(setup_driver):
        actuall_url = setup_driver.current_url
        expected_url = base_url
        assert actuall_url == expected_url, 'Неверный URL'

    @staticmethod
    def order_button_header_click(setup_driver):
        setup_driver.find_element(*MainPage.order_header_button).click()

    @staticmethod
    def order_button_click(setup_driver):
        setup_driver.execute_script("window.scrollTo(510, 2617)")
        setup_driver.find_element(*MainPage.order_button).click()

    @staticmethod
    def check_order_button(setup_driver):
        title = setup_driver.find_element(*OrderLocators.title_locator).text
        assert title == 'Для кого самокат', 'Неверный текст'

    @staticmethod
    def enter_first_name(setup_driver, first_name):
        setup_driver.find_element(*OrderLocators.first_name_field).send_keys(first_name)

    @staticmethod
    def enter_last_name(setup_driver, last_name):
        setup_driver.find_element(*OrderLocators.last_name_field).send_keys(last_name)

    @staticmethod
    def enter_adress(setup_driver, adress):
        setup_driver.find_element(*OrderLocators.adress_field).send_keys(adress)

    @staticmethod
    def enter_metro(setup_driver):
        field = setup_driver.find_element(*OrderLocators.station_field)
        field.click()
        setup_driver.find_element(By.XPATH, '//button[@value="1"]').click()

    @staticmethod
    def enter_phone(setup_driver, phone):
        setup_driver.find_element(*OrderLocators.phone_number_field).send_keys(phone)

    @staticmethod
    def click_order_button(setup_driver):
        setup_driver.find_element(*OrderLocators.next_button).click()

    @staticmethod
    def click_date_field(setup_driver):
        setup_driver.find_element(*OrderLocators.date_button).click()
        setup_driver.find_element(*OrderLocators.date).click()

    @staticmethod
    def click_rent_field(setup_driver):
        setup_driver.find_element(*OrderLocators.rent_button).click()
        setup_driver.find_element(*OrderLocators.rent_1).click()

    @staticmethod
    def click_finish_order_button(setup_driver):
        setup_driver.find_element(*OrderLocators.order_button).click()

    @staticmethod
    def click_yes_button(setup_driver):
        setup_driver.find_element(*OrderLocators.yes_button).click()

    @staticmethod
    def check_order(setup_driver):
        actuall_result = setup_driver.find_element(*OrderLocators.order_success).text
        expect_result = 'Посмотреть статус'
        assert actuall_result == expect_result, "Неверный текст"

    @staticmethod
    @pytest.mark.parametrize('first_name,last_name,adress,phone', [["тест", "тест", "улица1", "89999999999"],
                                                                   ["тест1", "тест1", "улица2", "88888888888"]])
    def make_order(setup_driver, first_name, last_name, adress, phone):
        order = Orders
        order.enter_first_name(setup_driver, first_name)
        order.enter_last_name(setup_driver, last_name)
        order.enter_adress(setup_driver, adress)
        order.enter_metro(setup_driver)
        order.enter_phone(setup_driver, phone)
        order.click_order_button(setup_driver)
        order.click_date_field(setup_driver)
        order.click_rent_field(setup_driver)
        order.click_finish_order_button(setup_driver)
        order.click_yes_button(setup_driver)
        order.check_order(setup_driver)
