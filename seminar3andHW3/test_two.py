import time

import pytest
from testpage import OperationHelper
username = "GB20230583da08"
password = "a2382aba8d"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("GB20230583da08")
    test_page1.enter_pswd("a2382aba8d")
    test_page1.click_button()
    time.sleep(3)
#Залогинились
    test_page1.click_contact()
    time.sleep(3)
    #Заполняем поля
    test_page1.enter_cont_name("Yuliya")
    test_page1.enter_cont_email("mail@mail.ru")
    test_page1.enter_cont_text("La la la la")
    time.sleep(1)
    #жмякаем кнопку
    test_page1.click_button()
    time.sleep(1)
#проверим текст всплывающего окна
    assert test_page1.get_alert_text() == "Form successfully submitted"
