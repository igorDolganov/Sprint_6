from pages.order_page import *
from pages.main_page import *
import pytest

class TestOrder:

    def test_order_button(self, setup_driver):
        order = Orders(setup_driver)
        order.order_button_click()
        order.check_order_button()

    @pytest.mark.parametrize('first_name,last_name,adress,phone', [["тест", "тест", "улица1", "89999999999"],
                                                                   ["тестт", "тестт", "улица2", "88888888888"]])
    def test_order(self, setup_driver, first_name, last_name, adress, phone):
        order = Orders(setup_driver)
        order.order_button_header_click()
        order.make_order(first_name, last_name, adress, phone)

    def test_samokat_button(self, setup_driver):
        samokat = Orders(setup_driver)
        samokat.order_button_header_click()
        samokat.click_samokat_button()
        samokat.check_current_url()

    def test_yandex_logo_button(self, setup_driver):
        yandex = MainPageQuestions(setup_driver)
        yandex.check_yandex_logo_button()
