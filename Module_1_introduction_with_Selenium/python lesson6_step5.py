from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()

try:
    website_link = 'http://suninjuly.github.io/find_link_text'
    browser.get(website_link)
    expression = str(math.ceil(math.pow(math.pi, math.e)*10000))

    search_button = browser.find_element(By.LINK_TEXT, expression)
    search_button.click()

    first_name_input = browser.find_element(By.NAME, 'first_name')
    last_name_input = browser.find_element(By.NAME, 'last_name')
    city_input = browser.find_element(By.CLASS_NAME, 'city')
    country_input = browser.find_element(By.ID, 'country')

    first_name_input.send_keys('Ivan')
    last_name_input.send_keys('Petrov')
    city_input.send_keys('Smolensk')
    country_input.send_keys('Russia')

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
