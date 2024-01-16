"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ
"""""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def main():
    switch_windows()


def calculate(x):
    x = int(x)
    return math.log(abs(12 * math.sin(x)))


def switch_windows():
    browser = webdriver.Chrome()

    try:
        # Перейти по 1-й ссылке
        first_link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(first_link)

        # Нажать на магическую кнопку
        magic_button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
        magic_button.click()

        # Назначить нумерацию 2-м окнам
        first_window = browser.window_handles[0]
        second_window = browser.window_handles[1]

        # Перейти на 2-е окно
        browser.switch_to.window(second_window)

        # Найти, посчитать x
        x = browser.find_element(By.ID, "input_value").text
        x_result = calculate(x)

        # Найти строку для ввода, ввести данные, подтвердить
        input_string = browser.find_element(By.ID, "answer")
        input_string.send_keys(x_result)

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
