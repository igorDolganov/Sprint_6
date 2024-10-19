from locators.order_page_locators import *
from locators.main_page_locators import *
from locators.base_urls import base_url


class Orders:

    def __init__(self, setup_driver):
        self.driver = setup_driver

    def click_samokat_button(self):
        self.driver.find_element(*OrderLocators.samokat_button).click()

    def check_current_url(self):
        actuall_url = self.driver.current_url
        expected_url = base_url
        assert actuall_url == expected_url, 'Неверный URL'

    def order_button_header_click(self):
        self.driver.find_element(*MainPage.order_header_button).click()

    def order_button_click(self):
        self.driver.execute_script("window.scrollTo(510, 2617)")
        self.driver.find_element(*MainPage.order_button).click()

    def check_order_button(self):
        title = self.driver.find_element(*OrderLocators.title_locator).text
        assert title == 'Для кого самокат', 'Неверный текст'

    def enter_first_name(self, first_name):
        self.driver.find_element(*OrderLocators.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*OrderLocators.last_name_field).send_keys(last_name)

    def enter_adress(self, adress):
        self.driver.find_element(*OrderLocators.adress_field).send_keys(adress)

    def enter_metro(self):
        field = self.driver.find_element(*OrderLocators.station_field)
        field.click()
        self.driver.find_element(*OrderLocators.station).click()

    def enter_phone(self, phone):
        self.driver.find_element(*OrderLocators.phone_number_field).send_keys(phone)

    def click_order_button(self):
        self.driver.find_element(*OrderLocators.next_button).click()

    def click_date_field(self):
        self.driver.find_element(*OrderLocators.date_button).click()
        self.driver.find_element(*OrderLocators.date).click()

    def click_rent_field(self):
        self.driver.find_element(*OrderLocators.rent_button).click()
        self.driver.find_element(*OrderLocators.rent_date).click()

    def click_finish_order_button(self):
        self.driver.find_element(*OrderLocators.order_button).click()

    def click_yes_button(self):
        self.driver.find_element(*OrderLocators.yes_button).click()

    def check_order(self):
        actuall_result = self.driver.find_element(*OrderLocators.order_success).text
        expect_result = 'Посмотреть статус'
        assert actuall_result == expect_result, "Неверный текст"

    def make_order(self, first_name, last_name, adress, phone):
        order = Orders
        order.enter_first_name(self.driver, first_name)
        order.enter_last_name(self.driver, last_name)
        order.enter_adress(self.driver, adress)
        order.enter_metro(self.driver)
        order.enter_phone(self.driver, phone)
        order.click_order_button(self.driver)
        order.click_date_field(self.driver)
        order.click_rent_field(self.driver)
        order.click_finish_order_button(self.driver)
        order.click_yes_button(self.driver)
        order.check_order(self.driver)
