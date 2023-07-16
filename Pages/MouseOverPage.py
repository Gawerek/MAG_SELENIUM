from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class MouseOverPage:
    link_element = (By.CSS_SELECTOR, "a[title='Click me']")
    click_count_element = (By.ID, "clickCount")
    def __init__(self, driver):
        self.driver = driver

    def click_link_twice(self):
        action = ActionChains(self.driver)
        for _ in range(2):
            link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.link_element)
            )
            action.move_to_element(link).click().perform()

    def get_click_count(self):

        count = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_count_element))
        print(count.text)
        return int(count.text)