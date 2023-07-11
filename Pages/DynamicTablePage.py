
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DynamicTablePage:
    chrome_cpu_label_locator = (By.CSS_SELECTOR, ".bg-warning")
    def __init__(self, driver):
        self.driver = driver


    def get_chrome_cpu_label(self):
        chrome_cpu_label = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.chrome_cpu_label_locator))
        cpu_label_value = chrome_cpu_label.text.split(': ')[1]
        print(f"CPU label value: {cpu_label_value}")
        return cpu_label_value

    def get_chrome_cpu_load(self):
        cpu_value = self.get_chrome_cpu_label()
        headers = self.driver.find_elements(By.CSS_SELECTOR, "[role='columnheader']")
        cpu_index = None
        for index, header in enumerate(headers):
            if header.text == 'CPU':
                cpu_index = index
                break
        if cpu_index is None:
            print("No CPU column found in the table")
            return None  # return None if no CPU column is found
        rows = self.driver.find_elements(By.CSS_SELECTOR, "[role='row']")
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, "[role='cell']")
            if len(cells) > cpu_index and cells[0].text == 'Chrome':
                cpu_load_value = cells[cpu_index].text
                print(f"CPU load value for Chrome: {cpu_load_value}")
                return cpu_load_value  # get the CPU value for Chrome
        print("No row for Chrome found in the table")
        return None  # return None if no row for Chrome is found