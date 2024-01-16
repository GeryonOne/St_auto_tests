from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def main():
    browser = webdriver.Chrome()

    try:
        link_1 = "https://suninjuly.github.io/selects1.html"
        link_2 = "http://suninjuly.github.io/selects2.html"

        browser.get(link_1)

        first_num = browser.find_element(By.ID, "num1").text
        second_num = browser.find_element(By.ID, "num2").text
        nums_sum = int(first_num) + int(second_num)

        select_list = Select(browser.find_element(By.TAG_NAME, "select"))
        select_list.select_by_value(str(nums_sum))

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    finally:
        time.sleep(8)
        browser.quit()


if __name__ == '__main__':
    main()
