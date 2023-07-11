from selenium.webdriver.common.by import By
from common import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    load_delay_link_locator = (By.CSS_SELECTOR, 'a[href="/loaddelay"]')
    ajax_data_link_locator = (By.LINK_TEXT, "AJAX Data")
    url = 'http://uitestingplayground.com'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def click_load_delay_link(self):
        delay_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.load_delay_link_locator)
        )
        delay_link.click()

    def click_ajax_data_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ajax_data_link_locator)
        )
        link.click()
