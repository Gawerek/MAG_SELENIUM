from selenium.webdriver.common.alert import Alert
from Pages.HomePage import HomePage
from Pages.ClassAttributePage import ClassAttributePage

def test_class_attribute(driver):
    home_page=HomePage(driver)
    home_page.navigate()
    home_page.click_classatr_link()
    class_atribute_page = ClassAttributePage(driver)
    class_atribute_page.click_primary_button()
    alert = Alert(driver)
    alert.accept()