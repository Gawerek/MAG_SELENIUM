from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VerifyTextPage:
    locator = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")
    def __init__(self, driver):
        self.driver = driver

    def is_welcome_text_present(self):
        welcome_text_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator))
        print(f"Element text: {welcome_text_element.text}")  # added this line to print the text
        return 'Welcome' in welcome_text_element.text and 'UserName' in welcome_text_element.text
