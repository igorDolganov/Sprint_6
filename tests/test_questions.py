from pages.main_page import *
import pytest

class TestQuestions:

    @pytest.mark.parametrize("button, text_locator, expected", [
        (MainPage.question_1_button, MainPage.question_1_text,
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MainPage.question_2_button, MainPage.question_2_text,
         'Пока что у нас так: один заказ — один самокат.'
          ' Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за '
          'другим.'),
        (MainPage.question_3_button, MainPage.question_3_text,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                          'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                          'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (MainPage.question_4_button, MainPage.question_4_text,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MainPage.question_5_button, MainPage.question_5_text,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MainPage.question_6_button, MainPage.question_6_text,
         'Самокат приезжает к вам с полной зарядкой. '
         'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (MainPage.question_7_button, MainPage.question_7_text,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
         'Все же свои.'),
        (MainPage.question_8_button, MainPage.question_8_text,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_questions(self, setup_driver, button, text_locator, expected):
        question = MainPageQuestions(setup_driver)
        question.click_question(button)
        question.check_question(text_locator, expected)
