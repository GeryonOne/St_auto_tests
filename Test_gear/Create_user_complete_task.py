from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация веб-драйвера (предполагается, что у вас установлен ChromeDriver)
driver = webdriver.Chrome()

# Открытие веб-приложения
driver.get("https://your-todo-app.com")

# Регистрация нового пользователя
register_button = driver.find_element(By.LINK_TEXT, "Register")
register_button.click()

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
register_button = driver.find_element(By.NAME, "register_button")

username_input.send_keys("test_user")
password_input.send_keys("password123")
register_button.click()

# Вход под созданным пользователем
login_button = driver.find_element(By.LINK_TEXT, "Login")
login_button.click()

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.NAME, "login_button")

username_input.send_keys("test_user")
password_input.send_keys("password123")
login_button.click()

# Добавление новой задачи
task_input = driver.find_element(By.NAME, "task")
task_input.send_keys("Complete Selenium automation task")
task_input.send_keys(Keys.RETURN)

# Отметка задачи как выполненной
complete_checkbox = driver.find_element(By.XPATH, "//span[text()='Complete Selenium automation task']/../input[@type='checkbox']")
complete_checkbox.click()

# Удаление учетной записи
settings_button = driver.find_element(By.LINK_TEXT, "Settings")
settings_button.click()

delete_account_button = driver.find_element(By.XPATH, "//button[text()='Delete Account']")
delete_account_button.click()

confirm_delete_button = driver.find_element(By.XPATH, "//button[text()='Confirm Delete']")
confirm_delete_button.click()

# Закрытие браузера
driver.quit()