"""
Скрипт для авторизации на Stepik. Логин и пароль изменены
"""""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    browser = webdriver.Chrome()

    try:
        # Открыть Stepik, выполнить авторизацию
        stepik_homepage = "https://stepik.org/catalog"
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
        input_answer.send_keys(answer)  # Ответ для каждой задачи свой. Скрипт - пример

        # Найти кнопку "Отправить". Отправить ответ
        submit_stepik = browser.find_element(By.CLASS_NAME, "submit-submission")
        submit_stepik.click()

        time.sleep(5)

        # Нажать "Начать заново", чтобы избежать конфликта при запуске скриптов в будущем
        solve_again_button = browser.find_element(By.CSS_SELECTOR, 'button.again-btn.white')
        solve_again_button.click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    main()
