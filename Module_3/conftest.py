import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: Chrome or Firefox")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': })
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome" or browser_name == "Chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox" or browser_name == "Firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
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
