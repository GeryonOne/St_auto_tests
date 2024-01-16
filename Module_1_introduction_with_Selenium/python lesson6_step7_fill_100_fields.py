from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    open_link = 'http://suninjuly.github.io/huge_form.html'
    browser.get(open_link)

    all_forms = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for form in all_forms:
        form.send_keys('test_text')

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
