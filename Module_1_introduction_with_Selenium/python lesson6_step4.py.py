from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/find_xpath_form'
    browser.get(link)

    first_name_input = browser.find_element(By.NAME, 'first_name')
    last_name_input = browser.find_element(By.NAME, 'last_name')
    city_input = browser.find_element(By.CLASS_NAME, 'city')
    country_input = browser.find_element(By.ID, 'country')

    first_name_input.send_keys('Ivan')
    last_name_input.send_keys('Petrov')
    city_input.send_keys('Smolensk')
    country_input.send_keys('Russia')

    submit_button = browser.find_element(By.XPATH,  "//button[@type='submit']")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
