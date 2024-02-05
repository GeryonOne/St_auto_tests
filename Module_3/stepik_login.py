import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest  # config module. Need to change password before using program


class TestLinks:
    code_word = ""
    links_arr = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('link', links_arr)
    def test_links(self, browser, login, link):
        current_link = link
        browser = login
        browser.implicitly_wait(5)

        print("\nOpening task page..")

        browser.get(current_link)

        # Также добавил страховку для поиска элемента на странице
        text_area = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'textarea.ember-text-area.ember-view.textarea.string-quiz__textarea')))
        text_area.send_keys(math.log(int(time.time())))

        print("\nSending result...")

        # Кнопка "Отправить" работает с задержкой. Написал подстаховку
        submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))

        submit_button.click()

        print("\nResult submitted. Checking text..")

        # Также подстраховка. На случай, если текст не появится сразу
        result_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        get_res_text = result_text.text
        print(get_res_text)

        try:
            assert get_res_text == "Correct!", f"Error. Expacted result: 'Correct!', got {get_res_text}"
        except AssertionError as e:
            self.code_word += get_res_text
            print(f"Assertion failed: {e}")

    def test_run_all_tests(self):
        print(f"\nCode word after all tests: {self.code_word}")
