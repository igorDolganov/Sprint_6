from selenium.webdriver.common.by import By


class MainPage:

    question_1_button = [By.ID, 'accordion__heading-0']
    question_2_button = [By.ID, 'accordion__heading-1']
    question_3_button = [By.ID, 'accordion__heading-2']
    question_4_button = [By.ID, 'accordion__heading-3']
    question_5_button = [By.ID, 'accordion__heading-4']
    question_6_button = [By.ID, 'accordion__heading-5']
    question_7_button = [By.ID, 'accordion__heading-6']
    question_8_button = [By.ID, 'accordion__heading-7']

    question_1_text = [By. ID, 'accordion__panel-0']
    question_2_text = [By.ID, 'accordion__panel-1']
    question_3_text = [By.ID, 'accordion__panel-2']
    question_4_text = [By.ID, 'accordion__panel-3']
    question_5_text = [By.ID, 'accordion__panel-4']
    question_6_text = [By.ID, 'accordion__panel-5']
    question_7_text = [By.ID, 'accordion__panel-6']
    question_8_text = [By.ID, 'accordion__panel-7']

    order_header_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_button = [By.XPATH, '(//button[text()="Заказать"])[2]']
    yandex_logo = [By.XPATH, '//img[@alt="Yandex"]']
