from pages.order_page import *
from conftest import setup_driver
from pages.main_page import *


class TestOrder:

    def test_order_button(self, setup_driver):
        order = Orders
        order.order_button_click(setup_driver)
        order.check_order_button(setup_driver)

    @pytest.mark.parametrize('first_name,last_name,adress,phone', [["тест", "тест", "улица1", "89999999999"],
                                                                   ["тестт", "тестт", "улица2", "88888888888"]])
    def test_order(self, setup_driver, first_name, last_name, adress, phone):
        order = Orders
        order.order_button_header_click(setup_driver)
        order.make_order(setup_driver, first_name, last_name, adress, phone)

    def test_samokat_button(self, setup_driver):
        samokat = Orders
        samokat.order_button_header_click(setup_driver)
        samokat.click_samokat_button(setup_driver)
        samokat.check_current_url(setup_driver)

    def test_yandex_logo_button(self, setup_driver):
        yandex = MainPageQuestions
        yandex.check_yandex_logo_button(setup_driver)
