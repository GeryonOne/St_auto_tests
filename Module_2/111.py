from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

try:
    button = driver.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view
    button.click()
    assert True
finally:
    driver.quit()
