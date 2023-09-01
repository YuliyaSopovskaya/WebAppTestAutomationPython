# Урок 3. Тестирование с использованием PageObject
# Задание
# Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета. 
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
# Формат сдачи: В качестве решения принимается написанный нами ранее проект 
# с добавлением шага по проверке Contact Us и правками всех необходимых вспомогательных файлов.
# Что ещё можно почитать:
# Легкое веб-тестирование с Python, Pytest и Selenium WebDriver, часть 5:
# создание теста Page Object Selenium при помощи Python

import time
import pytest
import yaml
from testpage import OperationHelper


def test_contact_form(browser):
    test_page = OperationHelper(browser)
    test_page.go_to_site()
    time.sleep(1)
    
    testdata = None
    with open ("testdata.yaml") as f:
        test_data = yaml.safe_load(f)
        
    assert test_data is not None, "Failed"

    #открываем форму "Contact Us"
    test_page.click_contact()
    time.sleep(1)  
    
    #ввод данных в форму
    test_page.enter_cont_name(test_data["contact name"])
    test_page.enter_cont_email(text = test_data ["contact email"])
    test_page.enter_cont_text(test_data ["test message"])

    #нажимаем кнопку отправки формы
    test_page.click_button()
    time.sleep(1)  
    
    #переключаемся на alert и получаем его текст
    alert = test_page.switch_to_alert()
    alert_text = alert.text

    #проверяем текст alert cвсплыв окно
    expected_alert_text = "Form successfully submitted"
    assert alert_text == expected_alert_text, f"Alert text is not as expected. Expected: '{expected_alert_text}', Actual: '{alert_text}'"

