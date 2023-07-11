from selenium.webdriver.common.alert import Alert

from Pages.ClassAttributePage import ClassAttributePage

def test_class_attribute(driver):
    page = ClassAttributePage(driver)
    page.navigate()
    page.click_primary_button()

    alert = Alert(driver)
    alert.accept()