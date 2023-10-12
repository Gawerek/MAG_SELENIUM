from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ClickPage:
    def __init__(self, driver):
        self.driver = driver
        self.bad_button_locator = (By.ID, "badButton")

    def navigate(self, url):
        self.driver.get(url)

    def click_bad_button(self):
        bad_button = self.driver.find_element(*self.bad_button_locator)
        ActionChains(self.driver).click(bad_button).perform()

    def is_button_green(self):
        bad_button = self.driver.find_element(*self.bad_button_locator)
        return "btn-success" in bad_button.get_attribute("class")
