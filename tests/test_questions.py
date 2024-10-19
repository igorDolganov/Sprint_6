from pages.main_page import *
import pytest

class TestQuestions:

    def test_question1(self, setup_driver):
        question1 = MainPageQuestions(setup_driver)
        question1.click_question1()
        question1.check_question1()

    def test_question2(self, setup_driver):

        question2 = MainPageQuestions(setup_driver)
        question2.click_question2()
        question2.check_question2()

    def test_question3(self, setup_driver):

        question3 = MainPageQuestions(setup_driver)
        question3.click_question3()
        question3.check_question3()

    def test_question4(self, setup_driver):

        question4 = MainPageQuestions(setup_driver)
        question4.click_question4()
        question4.check_question4()

    def test_question5(self, setup_driver):

        question5 = MainPageQuestions(setup_driver)
        question5.click_question5()
        question5.check_question5()

    def test_question6(self, setup_driver):

        question6 = MainPageQuestions(setup_driver)
        question6.click_question6()
        question6.check_question6()

    def test_question7(self, setup_driver):

        question7 = MainPageQuestions(setup_driver)
        question7.click_question7()
        question7.check_question7()

    def test_question8(self, setup_driver):

        question8 = MainPageQuestions(setup_driver)
        question8.click_question8()
        question8.check_question8()
