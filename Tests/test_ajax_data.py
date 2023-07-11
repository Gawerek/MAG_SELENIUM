from Pages.HomePage import HomePage
from Pages.AjaxDataPage import AjaxDataPage

def test_ajax_data(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_ajax_data_link()

    ajax_data_page = AjaxDataPage(driver)
    ajax_data_page.click_ajax_button()
    ajax_data_page.wait_for_data_loaded()
