from pages.main_page import *
from conftest import setup_driver


class TestQuestions:

    def test_question1(self, setup_driver):

        question1 = MainPageQuestions
        question1.click_question1(setup_driver)
        question1.check_question1(setup_driver)

    def test_question2(self, setup_driver):

        question2 = MainPageQuestions
        question2.click_question2(setup_driver)
        question2.check_question2(setup_driver)

    def test_question3(self, setup_driver):

        question3 = MainPageQuestions
        question3.click_question3(setup_driver)
        question3.check_question3(setup_driver)

    def test_question4(self, setup_driver):

        question4 = MainPageQuestions
        question4.click_question4(setup_driver)
        question4.check_question4(setup_driver)

    def test_question5(self, setup_driver):

        question5 = MainPageQuestions
        question5.click_question5(setup_driver)
        question5.check_question5(setup_driver)

    def test_question6(self, setup_driver):

        question6 = MainPageQuestions
        question6.click_question6(setup_driver)
        question6.check_question6(setup_driver)

    def test_question7(self, setup_driver):

        question7 = MainPageQuestions
        question7.click_question7(setup_driver)
        question7.check_question7(setup_driver)

    def test_question8(self, setup_driver):

        question8 = MainPageQuestions
        question8.click_question8(setup_driver)
        question8.check_question8(setup_driver)
