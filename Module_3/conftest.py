import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser_instance():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# Для корректной работы нужен валидный пароль в фикстуре
@pytest.fixture(scope="function")
def login(browser_instance):
    print("\nlogging in..")
    link = "https://stepik.org/catalog"
    browser_instance.implicitly_wait(5)

    browser_instance.get(link)

    log_in = "askraizek@yandex.ru"
    password = ""

    login_button = browser_instance.find_element(By.CLASS_NAME, 'navbar__auth_login')

    login_button.click()

    email_field = browser_instance.find_element(By.ID, "id_login_email")
    password_field = browser_instance.find_element(By.ID, "id_login_password")

    email_field.send_keys(log_in)
    password_field.send_keys(password)

    enter_button = browser_instance.find_element(By.CSS_SELECTOR, "button[type='submit']")
    enter_button.click()

    time.sleep(3)

    print("\nLogin successful")

    yield browser_instance  # provide the browser instance to the test
