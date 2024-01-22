from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    start_link = "http://suninjuly.github.io/registration1.html"
    browser.get(start_link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')

    first_name.send_keys('Ivan')
    last_name.send_keys('Slomov')
    email.send_keys('Smolov@yandex.ru')

    submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

