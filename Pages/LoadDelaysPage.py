from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import BasePage
class LoadDelaysPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_locator = (By.XPATH, '/html/body/section/div/button')

    def click_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.button_locator)
        )
        button.click()
