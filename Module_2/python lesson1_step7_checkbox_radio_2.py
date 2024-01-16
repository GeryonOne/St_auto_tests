from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Function to calculate the result based on the given mathematical expression
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Create a new Chrome WebDriver instance
browser = webdriver.Chrome()

try:
    # Open the specified URL in the browser
    link = "https://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # Find the element with ID "treasure" and get its "valuex" attribute
    chest_pic = browser.find_element(By.ID, "treasure")
    get_func_value = chest_pic.get_attribute("valuex")

    # Calculate the result using the provided mathematical expression
    result_value = calc(get_func_value)

    # Find the input field, checkbox, radio button, and submit button
    answer_field = browser.find_element(By.ID, "answer")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Enter the calculated result into the answer field
    answer_field.send_keys(result_value)

    # Check the checkbox and select the radio button
    checkbox.click()
    radiobutton.click()

    # Submit the form by clicking the submit button
    submit_button.click()

finally:
    # Add a delay to keep the browser window open for 15 seconds before quitting
    time.sleep(15)
    browser.quit()
