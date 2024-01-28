import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language',["ru", "en-gb"])
def test_guest_should_see_login_link(browser_instance, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser_instance.get(link)
    browser_instance.find_element(By.CSS_SELECTOR, "#login_link")
