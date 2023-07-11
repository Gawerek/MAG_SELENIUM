from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScrollbarsPage:
    button_locator = (By.ID, "hidingButton")
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_button_and_click(self):
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.button_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()