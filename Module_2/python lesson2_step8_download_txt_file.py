"""
Напишите скрипт, который будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"
"""""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


def main():

    browser = webdriver.Chrome()

    try:
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        # Определить местоположение текстового файла
        current_dir = os.path.abspath(
            os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'test_file.txt')  # добавляем к этому пути имя файла

        # Достать все поля и кнопки с сайта
        first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
        last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
        email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
        download_file = browser.find_element(By.ID, "file")
        submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Заполнить текстовые поля
        first_name.send_keys("Nikolay")
        last_name.send_keys("Petrov")
        email.send_keys("petrov@inbox.com")

        # прикрепить файл, нажать Submit
        download_file.send_keys(file_path)
        submit.click()

        alert = browser.switch_to.alert
        alert.accept()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
