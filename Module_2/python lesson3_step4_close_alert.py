"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
"""""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def main():
    answer = close_alert()
    stepik_parse(answer)


def compute_math(x):
    x = int(x)
    return math.log(abs(12 * math.sin(x)))


def close_alert():
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/alert_accept.html"

    try:
        browser.get(link)

        # Найти первую кнопку, нажать на нее
        magic_button = browser.find_element(By.XPATH, f"//button[contains(text(), 'I want to go on a magical journey!')]")
        magic_button.click()

        # Выделить модальное окно, подтвердить результат
        confirm = browser.switch_to.alert
        confirm.accept()

        # Решить математическую задачу
        x = browser.find_element(By.ID, "input_value").text
        math_result = compute_math(x)

        # Вставить ответ в поле
        send_answer = browser.find_element(By.ID, "answer")
        send_answer.send_keys(math_result)

        # Подтвердить результат
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Парсинг ответа. Изъять ответ из модального окна
        get_result = browser.switch_to.alert
        alert_text = get_result.text
        answer = alert_text.split(': ')[-1]  # Ответ к задаче. Отправить его на Stepik
        get_result.accept()
        time.sleep(3)

        return answer

    finally:
        time.sleep(4)
        browser.quit()


def stepik_parse(answer):
    browser = webdriver.Chrome()

    try:
        # Открыть Stepik, выполнить авторизацию
        stepik_login = "https://stepik.org/catalog?auth=login"
        browser.get(stepik_login)

        time.sleep(1)

        # Найти поле логина, пароля
        email_field = browser.find_element(By.ID, "id_login_email")
        pass_field = browser.find_element(By.ID, "id_login_password")

        login = "login"
        password = "password"

        # Ввести логин, пароль
        email_field.send_keys(login)
        pass_field.send_keys(password)

        # Подтвердить вход
        confirm_login = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn[type='submit']")
        confirm_login.click()

        time.sleep(3)

        # Перейти по ссылке, вставить ответ сюда:
        stepik_task_link = "https://stepik.org/lesson/184253/step/4?unit=158843"
        browser.get(stepik_task_link)

        time.sleep(3)

        # Найти поле ответа, ввести данные
        input_answer = browser.find_element(By.CSS_SELECTOR, '.string-quiz__textarea')
        input_answer.send_keys(answer)

        # Найти кнопку "Отправить". Отправить ответ
        submit_stepik = browser.find_element(By.CLASS_NAME, "submit-submission")
        submit_stepik.click()

        time.sleep(5)

        # Нажать "Начать заново", чтобы избежать конфликта при запуске скриптов в будущем
        solve_again_button = browser.find_element(By.CSS_SELECTOR, 'button.again-btn.white')
        solve_again_button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
