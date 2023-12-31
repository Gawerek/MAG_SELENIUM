from selenium.webdriver.common.by import By
from common import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    load_delay_link_locator = (By.CSS_SELECTOR, 'a[href="/loaddelay"]')
    ajax_data_link_locator = (By.LINK_TEXT, "AJAX Data")
    scroll_barr_link_locator = (By.CSS_SELECTOR, 'a[href="/scrollbars"]')
    dynamic_table_link_locator = (By.CSS_SELECTOR, 'a[href="/dynamictable')
    verify_text_link_locator = (By.CSS_SELECTOR, 'a[href="/verifytext')
    progress_bar_link_locator = (By.CSS_SELECTOR, 'a[href="/progressbar')
    sample_app_link_locator = (By.CSS_SELECTOR, 'a[href="/sampleapp')
    mouseover_link_locator = (By.CSS_SELECTOR, 'a[href="/mouseover')
    click_link_locator = (By.CSS_SELECTOR, 'a[href="/click')
    classatr_link_locator = (By.CSS_SELECTOR, 'a[href="/classattr')
    hiddenlayers_link_locator = (By.CSS_SELECTOR, 'a[href="/hiddenlayers')
    dynamicid_link_locator = (By.CSS_SELECTOR, 'a[href="/dynamicid')

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

    def click_scroll_barr_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.scroll_barr_link_locator)
        )
        link.click()

    def click_dynamic_table_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dynamic_table_link_locator)
        )
        link.click()

    def click_verify_text_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.verify_text_link_locator)
        )
        link.click()

    def click_progress_bar_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.progress_bar_link_locator)
        )
        link.click()

    def click_sample_app_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sample_app_link_locator)
        )
        link.click()

    def click_mouse_over_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.mouseover_link_locator)
        )
        link.click()

    def click_click_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_link_locator)
        )
        link.click()


    def click_classatr_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.classatr_link_locator)
        )
        link.click()

    def click_hiddenlayers_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.hiddenlayers_link_locator)
        )
        link.click()
    def click_dynamicid_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dynamicid_link_locator)
        )
        link.click()