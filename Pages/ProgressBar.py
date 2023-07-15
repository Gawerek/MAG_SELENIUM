from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProgressBarPage:
    start_button = (By.ID, "startButton")
    stop_button = (By.ID, "stopButton")
    progress_bar = (By.ID, "progressBar")
    def __init__(self, driver):
        self.driver = driver


    def click_start_button(self):
        start_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.start_button))
        start_btn.click()

    def click_stop_button_when_progress_reaches(self, target):
        stop_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.stop_button))
        while True:
            progress = int(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.progress_bar)).text.strip('%'))
            if progress == target:
                stop_btn.click()
                print(progress)
                break
