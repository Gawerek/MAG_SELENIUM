# pages/dynamic_id_page_selenium.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  common import BasePage

class DynamicIDPageSelenium:
    dynamic_id_button_locator = (By.XPATH, "//*[contains(text(),'Button with Dynamic ID')]")
    def __init__(self, driver):
        self.driver = driver
    def click_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.dynamic_id_button_locator))
        )
        button.click()

    def get_page_title(self):
        return self.driver.title
