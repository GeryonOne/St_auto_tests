import time

# webdriver - набор команд для управления браузером
from selenium import webdriver

# Импорт класса By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# Запуск драйвера браузера. После этой команды открывается новое окно браузера
driver = webdriver.Chrome()

# Команда time.sleep устанавливает паузу в 5 секунд. Это позволяет фиксировать, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Поиск поля для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Написать текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найти кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Сказать драйверу, что нужно нажать на кнопку. После этой команды должно быть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий нужно не забыть закрыть окно браузера
driver.quit()
