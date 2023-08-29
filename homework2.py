# test_1.py

# import yaml
# from module import Site

# with open("testdata.yaml") as f:
#     testdata = yaml.safe_load(f)
# site = Site(testdata["address"])

# def test_step1():
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#     btn_selector = "button"
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
#     err_label = site.find_element("xpath", x_selector3)
#     assert err_label.text == "401"

# testdata.yaml

# address: https://test-stand.gb.ru/login
# browser: chrome
# sleep_time: 1

# module.py

# import yaml
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# with open("testdata.yaml") as f:
#     testdata = yaml.safe_load(f)
#     browser = testdata["browser"]


# class Site:
#     def __init__(self, address):
#         if browser == "firefox":
#             service = Service(executable_path=GeckoDriverManager().install())
#             options = webdriver.FirefoxOptions()
#             self.driver = webdriver.Firefox(service=service, options=options)
#         elif browser == "chrome":
#             service = Service(executable_path=ChromeDriverManager().install())
#             options = webdriver.ChromeOptions()
#             self.driver = webdriver.Chrome(service=service, options=options)
#         self.driver.implicitly_wait(3)
#         self.driver.maximize_window()
#         self.driver.get(address)
#         time.sleep(testdata["sleep_time"])

#     def find_element(self, mode, path):
#         if mode == "css":
#             element = self.driver.find_element(By.CSS_SELECTOR, path)
#         elif mode == "xpath":
#             element = self.driver.find_element(By.XPATH, path)
#         else:
#             element = None
#         return element

#     def get_element_property(self, mode, path, property):
#         element = self.find_element(mode, path)
#         return element.value_of_css_property(property)

#     def close(self):
#         self.driver.close()

# Урок 2. Кроссбраузерное тестирование с Selenium WebDriver
# Задание
# Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста

import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    
    
    #ожидание после входа
    wait = WebDriverWait(site.driver, 10)
    x_selector_post_button = "//button[contains(text(), 'Create Post')]"
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, x_selector_post_button)))
    post_button.click()
    
   
    post_title_input = site.find_element("css", "input#post-title")
    post_title_input.send_keys("Название моего поста")
    post_textarea = site.find_element("css", "textarea#post-content")
    post_textarea.send_keys("Текст моего поста")
    
    
    #кнопка "Create"
    create_button = site.find_element("css", "button[type='submit']")
    create_button.click()

  
    #ожидание после создания поста
    x_selector_post_title = "//h2[@class='post-title']"
    post_title_element = wait.until(EC.visibility_of_element_located((By.XPATH, x_selector_post_title)))

  
    #проверка наличия названия
    assert post_title_element.text == "Название моего поста"
