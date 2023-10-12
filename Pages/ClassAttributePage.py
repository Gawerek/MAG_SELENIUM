from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.HomePage import HomePage
class ClassAttributePage:
    primary_button_locator = (By.CSS_SELECTOR, '.btn-primary')

    def __init__(self, driver):
        self.driver = driver
    def click_primary_button(self):
        primary_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.primary_button_locator)
        )
        primary_button.click()