from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SampleAppPage:
    username_field = (By.CSS_SELECTOR, "input[pb-role='username']")
    password_field = (By.CSS_SELECTOR, "input[pb-role='password']")
    login_button = (By.ID, "login")
    welcome_text = (By.ID, "loginstatus")
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        usename_text_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username_field))
        usename_text_input.send_keys(username)
        password_text_input= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_field))
        password_text_input.send_keys(password)
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        btn.click()

    def is_welcome_text_present(self, username):
        welcome_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.welcome_text)).text
        print(welcome_text)
        return f"Welcome, {username}" in welcome_text