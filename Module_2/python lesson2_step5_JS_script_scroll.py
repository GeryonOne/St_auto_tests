from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def main():
    browser = webdriver.Chrome()

    def math_func(x):
        x = int(x)
        return math.log(abs(12 * (math.sin(x))))

    try:
        link_1 = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link_1)

        # Найти x, посчитать значение
        x = browser.find_element(By.ID, "input_value").text
        x_solve = math_func(x)

        # Скролл страницы вниз, поиск submit
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        text_field = browser.find_element(By.ID, "answer")
        text_field.send_keys(x_solve)

        # Поиск нужных полей, кнопок: Текстовое поле, чек-бокс, радиокнопка
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        checkbox = browser.find_element(By.ID, "robotCheckbox")
        radiobutton = browser.find_element(By.ID, "robotsRule")

        # Нажать на нужные кнопки
        checkbox.click()
        radiobutton.click()
        submit_button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
