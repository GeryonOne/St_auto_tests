# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Функция для вычисления значения y по заданной формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Инициализация веб-драйвера (в данном случае, используется Chrome)
browser = webdriver.Chrome()

try:
    # Задание ссылки на страницу
    link = "https://suninjuly.github.io/math.html"
    # Открытие браузера по указанной ссылке
    browser.get(link)

    # Поиск элемента с id "input_value" для получения значения x
    x_element = browser.find_element(By.ID, "input_value")
    # Получение текстового содержимого элемента и преобразование в число
    x = x_element.text
    # Вычисление значения y с использованием функции calc
    y = calc(x)

    # Поиск элементов для ввода результата, чекбокса, радиокнопки и кнопки отправки формы
    result_field = browser.find_element(By.ID, "answer")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Ввод вычисленного значения y в соответствующее поле
    result_field.send_keys(y)
    # Выбор чекбокса "I'm the robot"
    checkbox.click()
    # Выбор радиокнопки "Robots rule!"
    radiobutton.click()
    # Нажатие на кнопку отправки формы
    submit.click()

finally:
    # Пауза для визуализации результата перед закрытием браузера
    time.sleep(10)
    # Закрытие браузера
    browser.quit()