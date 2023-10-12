from Pages.HomePage import HomePage
from Pages.LoadDelaysPage import LoadDelaysPage

def test_load_delays(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_load_delay_link()
    load_delays_page = LoadDelaysPage(driver)
    load_delays_page.click_button()
