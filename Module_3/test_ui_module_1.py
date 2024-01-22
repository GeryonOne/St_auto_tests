"""
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. 
Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо 
(во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 
"""""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestFirstModule(unittest.TestCase):
    """
    Класс с UI тестами. 1-й корректен, 2-й должен быть завален: 2-я страничка изменена, там некорректные селекторы
    
    Из обоих тестов убраны конструкции try / finally
    """""
    def test_ui_1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        start_link = "http://suninjuly.github.io/registration1.html"

        # try:
        browser.get(start_link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')

        first_name.send_keys('Ivan')
        last_name.send_keys('Slomov')
        email.send_keys('Smolov@yandex.ru')

        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "No 'Congratulations' in welcome text")

        # finally:
        #     time.sleep(10)
        #     browser.quit()

    def test_ui_2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        start_link = "http://suninjuly.github.io/registration2.html"

        # try:
        browser.get(start_link)

        first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')

        first_name.send_keys('Ivan')
        last_name.send_keys('Slomov')
        email.send_keys('Smolov@yandex.ru')

        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "No 'Congratulations' in welcome text")

        # finally:
        #     time.sleep(10)
        #     browser.quit()


if __name__ == '__main__':
    unittest.main()
