
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HiddenLayersPage():
    def __init__(self, driver):
        self.driver= driver
        self.GREEN_BUTTON = (By.ID, 'greenButton')



    def click_green_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GREEN_BUTTON)).click()

    def is_green_button_clickable(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GREEN_BUTTON))