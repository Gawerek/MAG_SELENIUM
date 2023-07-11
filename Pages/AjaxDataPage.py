from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AjaxDataPage:
    loaded_text_locator = (By.CSS_SELECTOR, "p.bg-success")
    ajax_button_locator = (By.ID, "ajaxButton")
    def __init__(self, driver):
        self.driver = driver

    def click_ajax_button(self):
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ajax_button_locator))
        button.click()


    def wait_for_data_loaded(self):
        wait_for_data_loaded =  WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(self.loaded_text_locator, "Data loaded with AJAX get request.")
        )
        assert wait_for_data_loaded