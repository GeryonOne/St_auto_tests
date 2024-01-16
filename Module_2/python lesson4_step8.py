"""
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""""
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calculate(x):
    x = int(x)
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Подождать, пока цена не упадет до 100. Нажать на кнопку
    house_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")
                                                  )

    # Нажать на кнопку book, когда цена упадет до 100
    buy_button = browser.find_element(By.ID, "book")
    buy_button.click()

    # Решить задачку, отправить ответ
    x = browser.find_element(By.ID, "input_value").text
    x_result = calculate(x)

    # Ввести ответ
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(x_result)

    # Подтвердить ответ
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Достать результат из модального окна
    get_result = browser.switch_to.alert
    alert_text = get_result.text
    answer = alert_text.split(": ")[-1]
    print(answer)


finally:
    time.sleep(5)
    browser.quit()
